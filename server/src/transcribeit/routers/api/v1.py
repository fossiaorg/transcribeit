from fastapi import APIRouter
from ..transcription import router as transcription_router


router = APIRouter()
router.include_router(transcription_router, prefix="/transcribe")