from uuid import uuid4
from typing import List
import yt_dlp
from yt_dlp.utils import DownloadError
from ...helpers.filename import get_filename_hash

def download_from_youtube(url: List[str]):
    filename = f"{str(uuid4())}"
    output_path = f"/home/matt/Documents/{filename}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'outtmpl': output_path,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(url)
            return f"{output_path}.mp3", error_code
    except DownloadError as dle:
        raise DownloadError("Faied to download video file")