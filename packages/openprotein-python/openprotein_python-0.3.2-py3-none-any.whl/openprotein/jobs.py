from datetime import datetime
from typing import List, Optional, Union, Literal
import time
from enum import Enum
from openprotein.models import Prediction, PoetScoreResult, PoetSSPResult, CVItem
from pydantic.error_wrappers import ValidationError

from pydantic import BaseModel, Field, root_validator, validator 
from openprotein.errors import TimeoutException
from openprotein.base import APISession
import openprotein.config as config
import tqdm 

from openprotein.schemas import NewModel, JobStatus, JobType

class Job(NewModel):
    status: JobStatus
    job_id: str
    #new emb service get doesnt have job_type
    job_type: Optional[Literal[tuple(member.value for member in JobType.__members__.values())] ] #type: ignore 
    created_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    prerequisite_job_id: Optional[str]  = None
    progress_message: Optional[str] = None
    progress_counter: Optional[int] = 0
    num_records: Optional[int] = None
    sequence_length: Optional[int] = None


    def refresh(self, session: APISession):
        """refresh job status"""
        return job_get(session, self.job_id)

    def done(self) -> bool:
        """Check if job is complete"""
        return self.status.done()

    def cancelled(self) -> bool:
        """check if job is cancelled"""
        return self.status.cancelled()

    def _update_progress(self, job) -> int:
        """update rules for jobs without counters"""
        progress = job.progress_counter
        #if progress is not None:  # Check None before comparison
        if progress is None:
            if job.status == JobStatus.PENDING:
                progress = 5
            if job.status == JobStatus.RUNNING:
                progress = 25
        if job.status in [JobStatus.SUCCESS, JobStatus.FAILURE]:
            progress = 100
        return progress or 0 # never None

    def wait(
        self,
        session: APISession,
        interval: int = config.POLLING_INTERVAL,
        timeout: Optional[int] = None,
        verbose: bool = False,
    ):
        """
        Wait for a job to finish, and then get the results.

        Args:
            session (APISession): Auth'd APIsession
            interval (int): Wait between polls (secs). Defaults to POLLING_INTERVAL
            timeout (int): Max. time to wait before raising error. Defaults to unlimited.
            verbose (bool, optional): print status updates. Defaults to False.

        Raises:
            TimeoutException: _description_

        Returns:
            _type_: _description_
        """
        start_time = time.time()

        def is_done(job: Job):
            if timeout is not None:
                elapsed_time = time.time() - start_time
                if elapsed_time >= timeout:
                    raise TimeoutException(
                        f"Wait time exceeded timeout {timeout}, waited {elapsed_time}"
                    )
            return job.done()

        pbar = None
        if verbose:
            pbar = tqdm.tqdm(total=100, desc="Waiting", position=0)

        job = self.refresh(session)
        while not is_done(job):
            if verbose:
                #pbar.update(1)
                #pbar.set_postfix({"status": job.status})
                progress = self._update_progress(job)
                pbar.n = progress
                pbar.set_postfix({"status": job.status})
                #pbar.refresh()
                # print(f'Retry {retries}, status={self.job.status}, time elapsed {time.time() - start_time:.2f}')
            time.sleep(interval)
            job = job.refresh(session)

        if verbose:
            #pbar.update(1)
            #pbar.set_postfix({"status": job.status})
            
            progress = self._update_progress(job)
            pbar.n = progress
            pbar.set_postfix({"status": job.status})
            #pbar.refresh()

        return job

    wait_until_done = wait



class Jobplus(Job):
    sequence_length: Optional[int] = None

class JobDetails(NewModel):
    job_id: str
    job_type: str
    status: str


class MSAJob(Job):
    msa_id: Optional[str] = None
    job_type: Literal[JobType.align] = JobType.align

    @root_validator
    def set_msa_id(cls, values):
        if not values.get('msa_id'):
            values['msa_id'] = values.get('job_id')
        return values
    
class PromptJob(MSAJob):
    prompt_id: Optional[str] = None
    job_type: Literal[JobType.align_prompt] = JobType.align_prompt

    @root_validator
    def set_prompt_id(cls, values):
        if not values.get('prompt_id'):
            values['prompt_id'] = values.get('job_id')
        return values


class PoetScoreJob(Job):
    parent_id: Optional[str] = None
    s3prefix: Optional[str] = None
    page_size: Optional[int] = None
    page_offset: Optional[int] = None
    num_rows: Optional[int] = None
    result: Optional[List[PoetScoreResult]] = None
    n_completed: Optional[int] = None

    job_type: Literal[JobType.prots2prot] = JobType.prots2prot

class PoetSSPJob(PoetScoreJob):
    parent_id: Optional[str] = None
    s3prefix: Optional[str] = None
    page_size: Optional[int] = None
    page_offset: Optional[int] = None
    num_rows: Optional[int] = None
    result: Optional[List[PoetSSPResult]] = None
    n_completed: Optional[int] = None

    job_type: Literal[JobType.prots2prot_single_site] = JobType.prots2prot_single_site

class PoetGenerateJob(Job):
    parent_id: Optional[str] = None
    s3prefix: Optional[str] = None
    page_size: Optional[int] = None
    page_offset: Optional[int] = None
    num_rows: Optional[int] = None
    result: Optional[List[PoetScoreResult]] = None
    n_completed: Optional[int] = None

    job_type: Literal[JobType.prots2prot_generate] = JobType.prots2prot_generate


class PredictJobBase(Job):
    """Shared properties for predict job outputs."""

    # might be none if just fetching
    job_id: Optional[str] = None
    job_type: str
    status: JobStatus

class DesignJob(Job):
    job_id: Optional[str] = None
    job_type: Literal[JobType.design] = JobType.design

class PredictJob(PredictJobBase):
    """Properties about predict job returned via API."""

    class SequencePrediction(NewModel):
        """Sequence prediction."""

        sequence: str
        predictions: List[Prediction] = []

    result: Optional[List[SequencePrediction]] = None
    job_type: Literal[JobType.predict] = JobType.predict


class PredictSingleSiteJob(PredictJobBase):
    """Properties about single-site prediction job returned via API."""

    class SequencePrediction(NewModel):
        """Sequence prediction."""

        position: int
        amino_acid: str
        # sequence: str
        predictions: List[Prediction] = []

    result: Optional[List[SequencePrediction]] = None
    job_type: Literal[JobType.predict_single_site] = JobType.predict_single_site


class SVDJob(Job):
    job_type: Literal[JobType.svd, JobType.svdfit, JobType.svdembed] = JobType.svd

class MultiJob(BaseModel):
    """Polymorphic class for  Jobs."""

    __root__: Union[PredictSingleSiteJob,
                    PredictJob,
                    DesignJob,
                    PoetGenerateJob,
                    PoetSSPJob,
                    PoetScoreJob,
                    PromptJob,
                    MSAJob,
                    SVDJob] = Field(discriminator="job_type", default_factory=Job)

    @classmethod
    def parse_obj(cls, obj, **kwargs):
        try:
            return super().parse_obj(obj, **kwargs).__root__
        except ValidationError as e :
            return Job.parse_obj(obj, **kwargs)
    

class SpecialPredictJob(Job):
    """special case of Job for predict that doesnt require job_id"""
    job_id: Optional[str] = None



def job_args_get(session: APISession, job_id) -> dict:
    """Get job."""
    endpoint = f"v1/jobs/{job_id}/args"
    response = session.get(endpoint)
    return dict(**response.json())

def job_get(session: APISession, job_id) -> Job:
    """Get job."""
    endpoint = f"v1/jobs/{job_id}"
    response = session.get(endpoint)
    return MultiJob.parse_obj(response.json())

class CVResults(Job):
    num_rows: int
    page_size: int
    page_offset: int
    result: List[CVItem]