import os
from pathlib import Path
from core.resume_transcription import call_agent
from core.fallbacks import resolve_api_key

def run_resume_transcription():
    openai_api_key = resolve_api_key()
    
    transcription_env = os.environ.get("TRANSCRIPTION")
    if transcription_env:
        transcription = str(transcription_env)
        print("---------------------------------")
        print("[VidBrief] ENV transcription is load")
    else:
        transcription_path = Path(__file__).parent.parent / "transcription.txt"
        if transcription_path.exists():
            transcription = str(transcription_path.read_text(encoding="utf-8"))
            print("---------------------------------")
            print("[VidBrief] ✅ Path transcription is load")
        else:
            raise ValueError("[VidBrief] Error: Transcription not found.")
    
    system_path = Path(__file__).parent.parent / "prompts" / "system_prompt.md"
    if system_path.exists():
        system_prompt = system_path.read_text(encoding="utf-8")
    else:
        raise ValueError("[VidBrief] Error: System Prompt not found")
    
    human_prompt = f"[VidBrief] Resume this transcription: {transcription}"
    
    print("---------------------------------")
    print("[VidBrief] ✅ Creating summary file...")    
    try: 
        with open("resume.md", "w", encoding="utf-8") as f:
            f.write(call_agent(system_prompt, human_prompt, transcription, openai_api_key))
    except Exception as e:
        print("[VidBrief] ❌ Critical Error during summary process")
        print(f"[VidBrief] 👉 Details: {e}")
        raise
    else: 
        print("---------------------------------")
        print("[VidBrief] ✅ File created successfully")
        
if __name__ == "__main__":
    run_resume_transcription()