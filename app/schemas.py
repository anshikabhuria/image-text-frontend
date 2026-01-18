from pydantic import BaseModel
from typing import List


class NLPResult(BaseModel):
    targets: List[str]
    protected: List[str]


class VisionDetection(BaseModel):
    species: str
    bbox: List[float]   # [x_min, y_min, x_max, y_max]
    confidence: float


class UploadResponse(BaseModel):
    id: int
    text: str
    image_path: str
    nlp: NLPResult
    vision: List[VisionDetection]
