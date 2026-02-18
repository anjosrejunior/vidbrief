import yt_dlp
from typing import Any

def download_audio(url):    
    ydl_opts: dict[str, Any] = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': 'audio_temp.m4a',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore[arg-type]
        ydl.download([url])
    return "audio_temp.m4a"