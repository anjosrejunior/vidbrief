import os
from pathlib import Path
from core.resume_transcription import call_agent

def run_resume_transcription():
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("Authentication error: OPENAI_API_KEY not found.")
    
    transcription_env = os.environ.get("TRANSCRIPTION")
    if transcription_env:
        transcription = str(transcription_env)
        print("---------------------------------")
        print("ENV transcription is load")
    else:
        transcription_path = Path(__file__).parent.parent / "transcription.txt"
        if transcription_path.exists():
            transcription = str(transcription_path.read_text(encoding="utf-8"))
            print("---------------------------------")
            print("Path transcription is load")
        else:
            raise ValueError("Error: Transcription not found.")
    
    system_path = Path(__file__).parent.parent / "prompts" / "system_prompt.md"
    if system_path.exists():
        system_prompt = system_path.read_text(encoding="utf-8")
    else:
        raise ValueError("Error: System Prompt not found")
    
    human_prompt = f"Resume this transcription: {transcription}"
    
    print("---------------------------------")
    print("✅ Creating summary file...")    
    try: 
        with open("resume.md", "w", encoding="utf-8") as f:
            f.write(call_agent(system_prompt, human_prompt, transcription, openai_api_key))
    except Exception as e:
        print("❌ Critical Error during summary process")
        print(f"👉 Details: {e}")
        raise
    else: 
        print("---------------------------------")
        print("✅ File created successfully")
        
if __name__ == "__main__":
    run_resume_transcription()