import os
from pathlib import Path
from dotenv import load_dotenv
from core.download_audio import download_audio

def run_download_audio(video_url):
    print("---------------------------------")
    print("[VidBrief] ✅ Downloading audio...")

    try:
        file = download_audio(video_url)
        output = Path(file)
        print("[VidBrief] 📦 File exists:", output.exists())
        if output.exists():
            print("[VidBrief] 📦 File size:", output.stat().st_size)
    except Exception as e:
        print("[VidBrief] ❌ Critical error during audio download")
        print(f"[VidBrief] 👉 Details: {e}")
        print("[VidBrief] CWD at failure:", Path.cwd())
        raise
    else:
        print("---------------------------------")
        print(f"[VidBrief] ✅ Audio saved to: {file}")

    return file
     
if __name__ == "__main__":
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(dotenv_path=env_path)
    
    video_url_env = os.environ.get("VIDEO_URL")
    if not video_url_env:
        raise ValueError(
            "Configuration error: VIDEO_URL not found. "
            "Please check if the environment variable is set in Kestra or your .env file."
        )
    run_download_audio(video_url_env)