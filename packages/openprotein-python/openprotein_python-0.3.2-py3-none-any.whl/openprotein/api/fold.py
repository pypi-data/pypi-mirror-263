from openprotein.base import APISession
from openprotein.api.jobs import (
    Job,
    MappedAsyncJobFuture,
    job_get,
)
from openprotein.errors import InvalidJob
import openprotein.config as config
from openprotein.api.jobs import load_job
from openprotein.models import (
    ModelDescription,
    TokenInfo,
    ModelMetadata,
    FoldedSequence,
)
from openprotein.jobs import MultiJob, JobType,JobStatus 
from openprotein.api.poet import validate_msa, MSAFuture
import pydantic
from typing import Optional, List, Tuple, Dict, Union, Any


PATH_PREFIX = "v1/fold"


def fold_models_get(session: APISession) -> List[str]:
    """
    List available fold models.

    Args:
        session (APISession): API session

    Returns:
        List[str]: list of model names.
    """

    endpoint = PATH_PREFIX + "/models"
    response = session.get(endpoint)
    result = response.json()
    return result


# alias fold_models_list_get to fold_models_get
fold_models_list_get = fold_models_get


def fold_model_get(session: APISession, model_id: str) -> ModelMetadata:
    endpoint = PATH_PREFIX + f"/models/{model_id}"
    response = session.get(endpoint)
    result = response.json()
    return ModelMetadata(**result)


def fold_get(session: APISession, job_id: str) -> Job:
    """
    Get Job associated with the given request ID.

    Parameters
    ----------
    session : APISession
        Session object for API communication.
    job_id : str
        job ID to fetch

    Returns
    -------
    job: Job
    """

    endpoint = PATH_PREFIX + f"/{job_id}"
    response = session.get(endpoint)
    return MultiJob.parse_obj(response.json())


def fold_get_sequences(session: APISession, job_id: str) -> List[bytes]:
    """
    Get results associated with the given request ID.

    Parameters
    ----------
    session : APISession
        Session object for API communication.
    job_id : str
        job ID to fetch

    Returns
    -------
    sequences : List[bytes]
    """
    endpoint = PATH_PREFIX + f"/{job_id}/sequences"
    response = session.get(endpoint)
    return pydantic.parse_obj_as(List[bytes], response.json())


def fold_get_sequence_result(
    session: APISession, job_id: str, sequence: bytes
) -> bytes:
    """
    Get encoded result for a sequence from the request ID.

    Parameters
    ----------
    session : APISession
        Session object for API communication.
    job_id : str
        job ID to retrieve results from
    sequence : bytes
        sequence to retrieve results for

    Returns
    -------
    result : bytes
    """
    sequence = sequence.decode()
    endpoint = PATH_PREFIX + f"/{job_id}/{sequence}"
    response = session.get(endpoint)
    return response.content

class FoldResultFuture(MappedAsyncJobFuture):
    """Future Job for manipulating results"""
    def __init__(
        self,
        session: APISession,
        job: Job,
        sequences=None,
        max_workers=config.MAX_CONCURRENT_WORKERS,
    ):
        super().__init__(session, job, max_workers)
        self._sequences = sequences

    @property
    def sequences(self):
        if self._sequences is None:
            self._sequences = fold_get_sequences(self.session, self.job.job_id)
        return self._sequences

    @property
    def id(self):
        return self.job.job_id

    def keys(self):
        return self.sequences

    def get_item(self, sequence: bytes) -> bytes:
        """
        Get fold results for specified sequence.

        Args:
            sequence (bytes): sequence to fetch results for

        Returns:
            np.ndarray: fold
        """
        data = fold_get_sequence_result(self.session, self.job.job_id, sequence)
        return data # 


def fold_model_post(session: APISession,
                    model_id: str,
                    sequences: List[bytes],
                    **kwargs):
    """
    POST a request for folds from the given model ID. Returns a Job object referring to this request
    that can be used to retrieve results later.

    Parameters
    ----------
    session : APISession
        Session object for API communication.
    model_id : str
        model ID to request results from
    sequences : List[bytes]
        sequences to request results for

    Returns
    -------
    job : Job
    """
    endpoint = PATH_PREFIX + f"/models/{model_id}"
    sequences = [s.decode() for s in sequences]
    body = {
        "sequences": sequences,
    }
    body.update(kwargs)
    response = session.post(endpoint, json=body)
    return MultiJob.parse_obj(response.json())


class FoldModel:
    """
    Class providing inference endpoints for protein fold models served by OpenProtein.
    """

    def __init__(self, session, model_id, metadata=None):
        self.session = session
        self.id = model_id
        self._metadata = metadata

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.id

    @property
    def metadata(self):
        return self.get_metadata()

    def get_metadata(self) -> ModelMetadata:
        """
        Get model metadata for this model.

        Returns
        -------
            ModelMetadata
        """
        if self._metadata is not None:
            return self._metadata
        self._metadata = fold_model_get(self.session, self.id)
        return self._metadata

    def fold(self, sequences: List[bytes], msa_id: Optional[Union[str, MSAFuture]] = None, **kwargs):
        """
        Fold sequences using this model.

        Parameters
        ----------
        sequences : List[bytes]
            sequences to fold

        Returns
        -------
            FoldResultFuture
        """
        if msa_id and not isinstance(msa_id, str):
            msa_id = validate_msa(msa_id)

        job = fold_model_post(self.session,
                              model_id=self.id,
                              sequences=sequences,
                              msa_id=msa_id,
                              **kwargs)
        return FoldResultFuture(self.session, job, sequences=sequences)


class FoldAPI:
    """
    This class defines a high level interface for accessing the fold API.
    """

    def __init__(self, session: APISession):
        self.session = session

    def list_models(self) -> List[FoldModel]:
        """list models available for creating folds of your sequences"""
        models = []
        for model_id in fold_models_list_get(self.session):
            models.append(FoldModel(self.session, model_id))
        return models

    def get_model(self, model_id: str) -> FoldModel:
        """
        Get model by model_id. 

        FoldModel allows all the usual job manipulation: \
            e.g. making POST and GET requests for this model specifically. 


        Parameters
        ----------
        model_id : str
            the model identifier

        Returns
        -------
        FoldModel
            The model

        Raises
        ------
        HTTPError
            If the GET request does not succeed.
        """
        return FoldModel(self.session, model_id)

    def fold(self,
             model: Union[FoldModel, str],
             sequences: List[bytes],
             msa_id: Optional[Union[str, MSAFuture]] = None, 
             **kwargs):

        if msa_id and not isinstance(msa_id, str):
            msa_id = validate_msa(msa_id)
                    
        if isinstance(model, FoldModel):
            model_id = model.id
            job = fold_model_post(
                self.session, model_id, sequences, msa_id=msa_id, **kwargs
            )
        else:
            # we assume model is the model_id
            model_id = model
            job = fold_model_post(
                self.session, model_id, sequences, msa_id=msa_id, **kwargs
            )
        return FoldResultFuture(self.session, job, sequences=sequences)

    def get_results(self, job) -> FoldResultFuture:
        """
        Retrieves the results of a fold job.

        Parameters
        ----------
        job : Job
            The fold job whose results are to be retrieved.

        Returns
        -------
        FoldResultFuture
            An instance of FoldResultFuture
        """
        return FoldResultFuture(self.session, job)

    def load_job(self, job_id: str) -> FoldResultFuture:
        """
        Reload a Submitted job to resume from where you left off!

        Parameters
        ----------
        job_id : str
            The identifier of the job whose details are to be loaded.

            
        Returns
        -------
        Job
            Job

        """
        job_details = load_job(self.session, job_id)
        sequences = fold_get_sequences(self.session, job_id=job_id)
        if "fold" not in job_details.job_type:
            raise InvalidJob(
                f"Job {job_id} is of type {job_details.job_type} not fold"
            )
        if len(sequences) == 0:
            raise InvalidJob(f"Unable to load sequences for job {job_id}")
        return FoldResultFuture(self.session, job_details, sequences=sequences)

