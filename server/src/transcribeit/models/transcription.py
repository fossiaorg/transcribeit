from typing import Optional, List
from pydantic import BaseModel


class URLTranscriptionRequest(BaseModel):
    url: str


class TranscriptionResponse(BaseModel):
    success: bool = False
    message: str
    data: Optional[List[dict]] = None
