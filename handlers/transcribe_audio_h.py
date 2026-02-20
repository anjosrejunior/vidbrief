from dotenv import load_dotenv
from openai import OpenAI
from pydantic import SecretStr
from core.transcribe_audio import transcribe_audio
from core.fallbacks import resolve_api_key, resolve_audio_path

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