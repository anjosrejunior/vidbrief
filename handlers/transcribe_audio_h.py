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

def run_transcribe_audio():
    raw_api_key = os.environ.get("OPENAI_API_KEY")
    if not raw_api_key: 
        raise ValueError("Authentication error: OPENAI_API_KEY not found.")
    
    str_openai_api_key = SecretStr(raw_api_key)
    client = OpenAI(api_key=str_openai_api_key.get_secret_value())
    
    print("---------------------------------")
    print("✅ Transcribing audio...")
    try:
        temp_transcription = transcribe_audio(resolve_audio_path(), client)
    except FileNotFoundError as f:
        print("❌ Critical error: audio file doesn't exist.")
        print(f"👉 Details: {f}")
        raise
    except Exception as e:
        print("❌ Error during transcription")
        print(f"👉 Details: {e}")
        raise
    else:
        print("---------------------------------")
        print("✅ Transcription completed successfully")
    
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(temp_transcription)
    
    print("---------------------------------")
    print("✅ Transcription file generated")
    
    return temp_transcription
    
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    run_transcribe_audio()