# # import os

# # files=os.listdir("audios")
# # index=1

# # for file in files:
# #     print(f"{index}. {file} \n")
# #     index+=1

# # whisper is an open source python library by open ai 

# # import whisper

# # model = whisper.load_model("t")

# # result = model.transcribe(audio = "audios/motivation.mp3") 
# #                         #   language="hi",
# #                         #   task="translate" )

# # print(result["text"])

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# ans={}


# client = OpenAI()

# with open("audios/6_Railway Tracks Konsi Reaction Se Judte Hai Class 10th - Thermit Reaction in 4 Min.mp3", "rb") as audio:
#     result = client.audio.translations.create(
#         file=audio,
#         model="whisper-1",
#     )
    
#     print(result.text)

# import os
# import json

# files=os.listdir("jsons")
# for file in files:
#     with open(f"jsons/{file}","r+") as f:
#         content=json.load(f)
#         i=0
#         arr=content["chunks"]
#         for obj in arr:
#             obj["start"]=f"{i//60}:{i%60:02d}"
#             i+=20
#             obj["end"]=f"{i//60}:{i%60:02d}"
#         f.seek(0)
#         json.dump(content,f)
