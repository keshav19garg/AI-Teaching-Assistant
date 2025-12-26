# Here every text is converted into an embedding and seperated all chunks along with their embeddings and stored into dataframe
import ollama
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib

#pip install ollama
#ollama pull bg3-m3

# single=ollama.embed(
#     model='bge-m3',
#     input='My name is Happy'
# )

# print(len(single["embeddings"][0]))

#for every chunk add chunk id and embedding

def create_embedding(text_list):
    result=ollama.embed(
        model='bge-m3',
        input=text_list
    )

    return result["embeddings"]

#text=["My name is Keshav","I am 22 years old"]
my_dict=[]
print("started")

jsons=os.listdir("jsons")
chunk_id=0
tr=False
for file in jsons:
    with open(f"jsons/{file}") as f:
        print(f"writing for file: {f}")
        content=json.load(f)
        embedded_arr=create_embedding([c["text"] for c in content["chunks"]])
        for index,chunk in enumerate(content['chunks']):
            chunk["chunk_id"]=chunk_id
            print(f"formatting for chunk {chunk_id}")
            chunk_id+=1
            chunk["embedding"]=embedded_arr[index]
            my_dict.append(chunk)

# with open("dict.json","w") as f:
#     json.dump(my_dict,f)

df=pd.DataFrame(my_dict)
joblib.dump(df,"Dataframe.joblib")


