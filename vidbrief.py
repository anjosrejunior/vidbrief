import os

from handlers.download_audio_h import run_download_audio
from handlers.resume_transcription_h import run_resume_transcription
from handlers.transcribe_audio_h import run_transcribe_audio


def display_banner():
    """Project name in ASCII Art."""
    os.system("cls" if os.name == "nt" else "clear")

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

        print(" [1] Download Audio (YouTube URL)")
        print(" [2] Transcribe Audio")
        print(" [3] Resume Audio")
        print(" [4] Download, Transcribe & Summarize")
        print(" [0] Exit")
        print("\n" + "_" * 40)

        choice = input("\n[VidBrief] Select an option: ").strip()

        if choice == "1":
            print("\n" + "=" * 40)
            url = input("[VidBrief] Enter YouTube URL: ")

            print(f"\n[VidBrief] Initializing process for: {url}")
            print("[VidBrief] Please wait... Download Audio")
            run_download_audio(url)
            print("[VidBrief] ✅ Audio Downloaded")

            input("\n[VidBrief] Process finished. Press Enter to return to menu...")
            
        elif choice == "2":
            print("\n" + "=" * 40)
            url = input("[VidBrief] Enter YouTube URL: ")
            print(f"\n[VidBrief] Initializing process for: {url}")
            print("[VidBrief] Please wait... Download Audio")
            run_download_audio(url)

            print("\n[VidBrief] Please wait... Transcribing audio...")
            run_transcribe_audio()
            print("\n[VidBrief] ✅ Audio Transcribed")

            input("\n[VidBrief] Process finished. Press Enter to return to menu...")

        elif choice == "3":
            print("\n" + "=" * 40)
            print("\n[VidBrief] Please wait... Resuming transcription...")
            run_resume_transcription()
            print("\n[VidBrief] ✅ Transcription resumed")

            input("\n[VidBrief] Process finished. Press Enter to return to menu...")
            
        elif choice == "4":
            print("\n" + "=" * 40)
            url = input("[VidBrief] Enter YouTube URL: ")
            print(f"\n[VidBrief] Initializing process for: {url}")
            print("[VidBrief] Please wait... Downloading Audio")
            run_download_audio(url)
            print("[VidBrief] ✅ Audio Downloaded")

            print("\n[VidBrief] Transcribing audio...")
            run_transcribe_audio()
            print("\n[VidBrief] ✅ Audio Transcribed")

            print("\n[VidBrief] Resuming transcription...")
            run_resume_transcription()            
            print("\n[VidBrief] ✅ Transcription resumed")

            input("\n[VidBrief] Process finished. Press Enter to return to menu...")

        elif choice == "0":
            print("\n[VidBrief] Exiting VidBrief... See you soon!")
            break

        else:
            input("\n[VidBrief] Invalid option! Press Enter to try again...")


if __name__ == "__main__":
    main_menu()
