
from pydantic import BaseModel, ConfigDict
from enum import Enum


class NewModel(BaseModel):
    pass 
    
class JobType(str, Enum):
    """
    Type of job.

    Describes the types of jobs that can be done.
    """

    stub = "stub"

    preprocess = "/workflow/preprocess"
    train = "/workflow/train"
    embed_umap = "/workflow/embed/umap"
    predict = "/workflow/predict"
    predict_single_site = "/workflow/predict/single_site"
    crossvalidate = "/workflow/crossvalidate"
    evaluate = "/workflow/evaluate"
    design = "/workflow/design"

    align = "/align/align"
    align_prompt = "/align/prompt"
    prots2prot = "/poet"
    prots2prot_single_site = "/poet/single_site"
    prots2prot_generate = "/poet/generate"

    embeddings = "/embeddings/embed"
    svd = "/embeddings/svd"
    attn = "/embeddings/attn"
    logits = "/embeddings/logits"
    reduced = "/embeddings/embed_reduced"

    svdfit = "/svd/fit"
    svdembed = "/svd/embed"

    fold = '/embeddings/fold'

class JobStatus(str, Enum):
    PENDING: str = "PENDING"
    RUNNING: str = "RUNNING"
    SUCCESS: str = "SUCCESS"
    FAILURE: str = "FAILURE"
    RETRYING: str = "RETRYING"
    CANCELED: str = "CANCELED"

    def done(self):
        return (
            (self is self.SUCCESS) or (self is self.FAILURE) or (self is self.CANCELED)
        )  # noqa: E501

    def cancelled(self):
        return self is self.CANCELED
