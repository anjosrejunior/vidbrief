import os
from handlers.download_audio_h import run_download_audio
from handlers.transcribe_audio_h import run_transcribe_audio
from handlers.resume_transcription_h import run_resume_transcription


def display_banner():
    """Exibe o nome do projeto em ASCII Art estilizado."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = """
    __     ___     _ ____  _     _      __ 
    \ \   / (_) __| | __ )| \__(_) ___ / _|
     \ \ / /| |/ _` |  _ \| '__| |/ _ \ |_ 
      \ V / | | (_| | |_) | |  | |  __/  _|
       \_/  |_|\__,_|____/|_|  |_|\___|_|  
                                           
    >>> Video Intelligence Tool <<<
    """
    print(banner)

def main_menu():
    while True:
        display_banner()
        
        print(" [1] Transcribe Audio (YouTube URL)")
        print(" [0] Exit")
        print("\n" + "_"*40)
        
        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            print("\n" + "="*40)
            url = input("Enter YouTube URL: ")
            
            # Aqui você chamará suas funções de processamento:
            print(f"\n[VidBrief] Initializing process for: {url}")
            print("[VidBrief] Please wait...")
            
            run_download_audio(url)
            run_transcribe_audio()
            run_resume_transcription()
            
            input("\nProcess finished. Press Enter to return to menu...")
            
        elif choice == '0':
            print("\nExiting VidBrief... See you soon!")
            break
        else:
            input("\nInvalid option! Press Enter to try again...")

if __name__ == "__main__":
    main_menu()