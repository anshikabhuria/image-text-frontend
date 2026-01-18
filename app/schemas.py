from pydantic import BaseModel
from typing import List


class NLPResult(BaseModel):
    targets: List[str]
    protected: List[str]


class VisionDetection(BaseModel):
    label: str
    confidence: float


class UploadResponse(BaseModel):
    id: int
    text: str
    image_path: str
    nlp: NLPResult
    vision: List[VisionDetection]
