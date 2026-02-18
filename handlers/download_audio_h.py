import os
from pathlib import Path
from dotenv import load_dotenv
from core.download_audio import download_audio

def run_download_audio(video_url):
    print("---------------------------------")
    print("✅ Downloading audio...")
    try:
        file = download_audio(video_url)
    except Exception as e:
        print("❌ Critical error during audio download")
        print(f"👉 Details: {e}")
        raise
    else:
        print("---------------------------------")
        print(f"✅ Audio saved to: {file}")
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