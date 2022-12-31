from whisper_handler import transcribe_handler 
from gpt3_fine_tuning import format_dataset,run_model 
import os
from dotenv import load_dotenv

def driver(pv_audio_file=None):
    load_dotenv()
    lv_transcript = transcribe_handler.transcribe_handler(pv_audio_file)

    lv_prompt = format_dataset.create_prompt(lv_transcript)
    print("Generating a summary...")
    run_model.run_model(os.getenv('MODEL_NAME'), lv_prompt)

def main():
    curr_filename = os.path.basename(__file__)
    print(f"Running {curr_filename}")

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--audio_file", type=str, required=True
    )
    args = parser.parse_args()
    driver(args.audio_file)

if __name__=="__main__":
    main()