import whisper


def transcribe(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)

    transcript = result["text"]
    print(transcript)

def main():
    audio_file = "test.mp3"
    transcribe(audio_file)