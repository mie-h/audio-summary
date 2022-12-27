FROM python:3.7-slim

WORKDIR /python-docker

RUN apt-get update && apt-get install git -y
RUN pip3 install "git+https://github.com/openai/whisper.git" 
RUN apt-get install -y ffmpeg

COPY test.py .
COPY test.mp3 .

EXPOSE 80

CMD ["python", "test.py"]