import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import SecretStr
from core.transcribe_audio import transcribe_audio

def resolve_audio_path():
    if path := os.environ.get("AUDIO_PATH"):
        audio = Path(path)
        if audio.exists():
            return audio

    cwd_path = Path.cwd() / "audio_temp.m4a"
    if cwd_path.exists():
        return cwd_path

    script_path = Path(__file__).parent.parent / "audio_temp.m4a"
    if script_path.exists():
        return script_path
        
    raise FileNotFoundError("audio_temp.m4a not found in any known location")
    
def resolve_api_key():
    environ_api_key = os.environ.get("OPENAI_API_KEY")
    if environ_api_key: 
        return environ_api_key
        
    load_dotenv()
    env_api_key = os.getenv("OPENAI_API_KEY")
    if env_api_key:
        return env_api_key
    
    raise ValueError("[VidBrief] Error: OPENAI_API_KEY not found.")

def run_transcribe_audio():
    api_key = resolve_api_key()
    openai_api_key = SecretStr(api_key)
    client = OpenAI(api_key=openai_api_key.get_secret_value())
    
    print("---------------------------------")
    print("[VidBrief] ✅ Transcribing audio...")
    try:
        temp_transcription = transcribe_audio(resolve_audio_path(), client)
    except FileNotFoundError as f:
        print("[VidBrief] ❌ Critical error: audio file doesn't exist.")
        print(f"[VidBrief] 👉 Details: {f}")
        raise
    except Exception as e:
        print("[VidBrief] ❌ Error during transcription")
        print(f"[VidBrief] 👉 Details: {e}")
        raise
    else:
        print("---------------------------------")
        print("[VidBrief] ✅ Transcription completed successfully")
    
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(temp_transcription)
    
    print("---------------------------------")
    print("[VidBrief] ✅ Transcription file generated")
    
    return temp_transcription
    
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    audio_path = resolve_audio_path()
    
    run_transcribe_audio()