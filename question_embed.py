import joblib
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import ollama
from ollama import chat
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

df=joblib.load("Dataframe.joblib")

def create_embedding(text_list):
    result=ollama.embed(
        model='bge-m3',
        input=text_list
    )

    return result["embeddings"]

def inference(prompt):
#    response = chat(
#     model='deepseek-r1',
#     messages=[{'role': 'user', 'content': f'{prompt}'}],
#     think=True,
#     stream=False,
#    )

    response = client.responses.create(
        model="gpt-5.1",
        input=prompt,
        reasoning={
        "effort": "none"
        }
    )

    return response.output_text


question=input("Ask your question buddy!")
question_embedded=create_embedding([question])
similarity=cosine_similarity(question_embedded,np.array(df["embedding"].to_list())).flatten()
#print(similarity.size)
top_results = 3
max_indx = similarity.argsort()[::-1][0:top_results]
new_df=df.iloc[max_indx].drop(["embedding"],axis=1)
print(new_df.columns)

prompt=f'''
I have created a class 10th course and for that I have a teaching assistant. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:
{new_df.to_json()}
Question: {question}
User asked this question related to the video chunks, you have to answer in a human way (don't mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course. and at the end don't ask any question.
'''

with open("prompt.txt","w") as f:
    f.write(prompt)
# print(new_df[["video_number","title","text"]])
# for rec in new_df.index:
#     print(f"Video Number: {new_df.at[rec,"video_number"]}\n Video Title: {new_df.at[rec,"title"]}\n Text: {new_df.at[rec,"text"]}\n")



# print('Thinking:\n', response.message.thinking)
# print('Answer:\n', response.message.content)
print(inference(prompt))