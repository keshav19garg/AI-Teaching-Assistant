import os
from pydub import AudioSegment

videos=os.listdir("videos")
os.makedirs("audios",exist_ok=True)

for index,video in enumerate(videos):
    name=os.path.splitext(video)
    audio = AudioSegment.from_file(f"videos/{video}", format=f"{name[1].split('.')[1]}")
    filename=f"{index+1:02d}_{name[0]}.mp3"
    audio.export(f"audio/{filename}", format="mp3")

