import openai


def summarize_transcript(transcript):
    tldr_tag = "\n tl;dr:"
    openai.organization = 'API KEY org'
    openai.api_key = "your openAI key"
        
    text = transcript + tldr_tag
    response = openai.Completion.create(engine="davinci",prompt=text,temperature=0.3,
        max_tokens=140,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    print(response["choices"][0]["text"])

def main():
    
    transcript = ""
    summarize_transcript(transcript)
    