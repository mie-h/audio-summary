import whisper
import os

def transcribe_handler(pv_audio_file):
    """Return a transcipt of a given audio file."""

    print(f"Given {pv_audio_file}, transcribe the file using Whisper.")
    lv_model = whisper.load_model("base")
    lv_result = lv_model.transcribe(pv_audio_file)

    lv_transcript = lv_result["text"]
    print(f"Transcript output: {lv_transcript}")
    return lv_transcript

def main():
    curr_filename = os.path.basename(__file__)
    print(f"Running {curr_filename}")

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--audio_file", type=str
    )
    args = parser.parse_args()
    transcribe_handler(args.audio_file)