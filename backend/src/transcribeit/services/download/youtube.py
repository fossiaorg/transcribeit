import os 
from uuid import uuid4
from typing import List
import yt_dlp
from yt_dlp.utils import DownloadError
from ...config import AppConfig, get_config
from ...helpers.filename import get_filename_hash


config: AppConfig = get_config()


def download_from_youtube(url: List[str]):
    filename = f"{str(uuid4())}"
    base_dir = config.env.uploads_dir
    os.makedirs(base_dir, exist_ok=True)
    output_path = os.path.join(base_dir, filename)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }
        ],
        "outtmpl": output_path,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(url)
            return f"{output_path}.mp3", error_code
    except DownloadError as dle:
        print(f"Download error: {dle}") 
        raise DownloadError(f"Failed to download video file: {dle}")