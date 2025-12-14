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
    
    # FIX 1: specific check for empty or missing uploads_dir
    # If config is empty, default to a 'downloads' folder in the current directory
    base_dir = config.env.uploads_dir if config.env.uploads_dir else "downloads"
    
    # FIX 2: Ensure the directory actually exists before writing to it
    # This prevents "No such file or directory" errors
    os.makedirs(base_dir, exist_ok=True)
    
    # FIX 3: Use os.path.join for safer path construction
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
        "outtmpl": output_path, # yt-dlp will append .mp3 automatically
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download([url]) # yt-dlp expects a list
            
            # The final file will have the extension appended by the postprocessor
            final_path = f"{output_path}.mp3"
            
            return final_path, error_code
            
    except DownloadError as dle:
        # It's often better to log the error rather than just re-raising with a generic message
        print(f"Download error: {dle}") 
        raise DownloadError(f"Failed to download video file: {dle}")
