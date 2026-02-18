import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import SecretStr
from core.transcribe_audio import transcribe_audio

def run_transcribe_audio():
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(dotenv_path=env_path)
    
    audio_sys_path = Path(__file__).parent.parent / "audio_temp.m4a"
    env_audio = os.environ.get("AUDIO_PATH")
    audio_path = env_audio if env_audio else str(audio_sys_path)    
    if not Path(audio_path).exists():
        raise ValueError("Configuration error: AUDIO_PATH is not defined in environment variables or .env file.")
        
    raw_api_key = os.environ.get("OPENAI_API_KEY")
    if not raw_api_key: 
        raise ValueError("Authentication error: OPENAI_API_KEY not found.")
    
    str_openai_api_key = SecretStr(raw_api_key)
    client = OpenAI(api_key=str_openai_api_key.get_secret_value())
    
    print("---------------------------------")
    print("✅ Transcribing audio...")
    try:
        temp_transcription = transcribe_audio(audio_path, client)
    except FileNotFoundError:
        print("❌ Critical error: audio file doesn't exist.")
        print(f"👉 Audio path: {audio_path}")
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
    run_transcribe_audio()