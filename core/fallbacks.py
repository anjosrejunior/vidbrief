import os
from pathlib import Path
from dotenv import load_dotenv

def resolve_audio_path():
    if path := os.environ.get("AUDIO_PATH"):
        audio = Path(path)
        if audio.exists():
            return audio
            
    load_dotenv()
    env_audio_path = os.getenv("AUDIO_PATH")
    if env_audio_path and env_audio_path.strip():
        return Path(env_audio_path.strip())
    
    cwd_path = Path.cwd() / "audio_temp.m4a"
    if cwd_path.exists():
        return cwd_path

    script_path = Path(__file__).parent.parent / "audio_temp.m4a"
    if script_path.exists():
        return script_path
        
    raise FileNotFoundError("[VidBrief] audio_temp.m4a not found in any known location")
    
def resolve_api_key():
    environ_api_key = os.environ.get("OPENAI_API_KEY")
    if environ_api_key: 
        return environ_api_key
        
    load_dotenv()
    env_api_key = os.getenv("OPENAI_API_KEY")
    if env_api_key:
        return env_api_key
    
    raise ValueError("[VidBrief] Error: OPENAI_API_KEY not found.")