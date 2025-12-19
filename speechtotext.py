from pydub import AudioSegment
from openai import OpenAI
from dotenv import load_dotenv
import json
import os
load_dotenv()

client=OpenAI()

audios=os.listdir("audios")
for audio in audios:
    audio_path=f"audios/{audio}"
    chunk_len_ms=20000
    audio_file=AudioSegment.from_file(audio_path)
    audio_duration_ms=len(audio_file)
    segments=[]
    base_name = os.path.splitext(audio)[0]
    parts = base_name.split('_')    
    video_number = parts[0]
    title = parts[1] if len(parts) > 1 else ""
    chunks=os.makedirs("chunks",exist_ok=True)
    jsons=os.makedirs("jsons",exist_ok=True)
   
    for i in range(0,audio_duration_ms,chunk_len_ms):
        start_ms=i
        end_ms=min(i+chunk_len_ms,audio_duration_ms)
        chunk=audio_file[start_ms:end_ms]
        chunk_file = f"chunks/{base_name}_{i//chunk_len_ms}.mp3"
        chunk.export(chunk_file, format="mp3")

        try:
            with open(chunk_file, "rb") as f:
             result = client.audio.translations.create(
                file=f,
                model="whisper-1"
            )

        except Exception as e:
            print(f"Failed chunk {i//chunk_len_ms}: {e}")
            continue

        segments.append({"video_number":f"{video_number}","title":f"{title}","start":f"{(start_ms/1000)/60}","end":f"{(end_ms/1000)%60}","text":f"{result.text}"})

    final_json={"chunks":segments,"full_text":" ".join(s["text"] for s in segments)}
        
    with open(f"jsons/{base_name}.json","w",encoding="utf-8") as f:
        json.dump(final_json,f,ensure_ascii=False, indent=2)

        # folder_name=f"chunkedaudios/{audio.split("_")[0]}"
        # os.makedirs(folder_name,exist_ok=True)
        # chunk_file=f"{folder_name}/{i//chunk_len_ms}.mp3"
        # chunk.export(chunk_file,format="mp3")
