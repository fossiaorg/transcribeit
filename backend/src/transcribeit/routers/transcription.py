import logging
import os
from fastapi import APIRouter
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
from yt_dlp.utils import DownloadError
from ..config import AppConfig, get_config
from ..constants.download import YOUTUBE_URL_PREFIX
from ..models.transcription import URLTranscriptionRequest, TranscriptionResponse
from ..services.download.youtube import download_from_youtube
from ..services.download.local import download_to_fs
from ..services.transcription import transcribe_audio


router = APIRouter(tags=["Transcription"])
config: AppConfig = get_config()


@router.post("/url")
async def get_transcription_from_url(payload: URLTranscriptionRequest):
    url = payload.url
    try:
        # Check if URL matches YouTube prefixes
        for yt_prefix in YOUTUBE_URL_PREFIX:
            if url.startswith(yt_prefix):
                logging.info(f"Downloading from YouTube: {url}")
                output_path, error = download_from_youtube(url)
                
                if error or not output_path:
                    return JSONResponse(
                        status_code=500,
                        content=TranscriptionResponse(
                            success=False,
                            message="Failed to download YouTube video due to an internal error.",
                            data=None # Fixed: Added missing field
                        ).dict(),
                    )
                
                segment_data = transcribe_audio(output_path)
                return JSONResponse(
                    status_code=200,
                    content=TranscriptionResponse(
                        success=True,
                        message="Transcription from URL successful",
                        data=segment_data,
                    ).dict(),
                )

    except DownloadError as dle:
        return JSONResponse(
            status_code=500, # Fixed: changed 'status' to 'status_code'
            content=TranscriptionResponse(
                success=False,
                message=f"Failed to download video due to the following error: {dle}",
                data=None # Fixed: Added missing field
            ).dict(),
        )

    except Exception as exc:
        return JSONResponse(
            status_code=500, # Fixed: changed 'status' to 'status_code'
            content=TranscriptionResponse(
                success=False,
                message=f"Failed to transcribe video from URL due to the following error: {exc}",
                data=None # Fixed: Added missing field
            ).dict(),
        )


@router.post("/file")
async def get_transcription_from_file(file: UploadFile = File(...)):
    try:
        # Fixed: Passed 'file' instead of undefined 'url'
        output_path, error = download_to_fs(file) 
        
        if error or not output_path:
            return JSONResponse(
                status_code=500,
                content=TranscriptionResponse(
                    success=False,
                    message="Failed to save uploaded file due to an internal error.",
                    data=None # Fixed: Added missing field
                ).dict(),
            )
            
        segment_data = transcribe_audio(output_path)
        return JSONResponse(
            status_code=200,
            content=TranscriptionResponse(
                success=True,
                message="Transcription from file successful",
                data=segment_data,
            ).dict(),
        )

    except Exception as exc:
        return JSONResponse(
            status_code=500, # Fixed: changed 'status' to 'status_code'
            content=TranscriptionResponse(
                success=False,
                message=f"Failed to transcribe video from file due to the following error: {exc}",
                data=None # Fixed: Added missing field
            ).dict(),
        )
