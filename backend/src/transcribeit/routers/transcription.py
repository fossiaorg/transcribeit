import logging
import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from yt_dlp.utils import DownloadError
from ..config import AppConfig, get_config
from ..constants.download import YOUTUBE_URL_PREFIX
from ..models.transcription import TranscriptionRequest, TranscriptionResponse
from ..services.download.youtube import download_from_youtube


router = APIRouter(tags=["Transcription"])
config: AppConfig = get_config()


@router.post("/url")
async def download_from_url(payload: TranscriptionRequest):
    url = payload.url
    try:
        for yt_prefix in YOUTUBE_URL_PREFIX:
            if url.startswith(yt_prefix):
                logging.info(f"Downloading from YouTube: {url}")
                output_path, error = download_from_youtube(url)
                if error or not output_path:
                    return JSONResponse(
                        status_code=500,
                        content=TranscriptionResponse(
                            message=f"Failed to download YouTube video due to an internal error."
                        ).dict()
                    )
                segments, info = config.whisper_model.transcribe(output_path)
                logging.info(f"Result: {result}")
                segment_data = []
                for segment in segments:
                    segment_data.append({"start": segment.start, "end": segment.end, "text": segment.text})
                os.remove(output_path)
                return JSONResponse(
                    status_code=200,
                    content=TranscriptionResponse(
                        success=True,
                        message="Transcription from URL successful",
                        data=segments
                    ).dict()
                )

    except DownloadError as dle:
        return JSONResponse(
            status=500,
            content=TranscriptionResponse(
                message=f"Failed to download video due to the following error: {dle}"
            ).dict()
        )

    except Exception as exc:
        return JSONResponse(
            status=500,
            content=TranscriptionResponse(
                message=f"Failed to transcribe video from URL due to the following error: {exc}"
            ).dict()
        )