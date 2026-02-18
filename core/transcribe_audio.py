def transcribe_audio(audio_path, client):
    with open(audio_path, "rb") as audio:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio
        )
    return transcription.text
