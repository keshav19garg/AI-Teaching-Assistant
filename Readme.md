# How to use this RAG based AI Teaching Assistant for your own course

## 1. Video to Audio Conversion
Convert all your videos to mp3 and put in audios folder

## 2. Audio to Text Conversion
Convert all mp3 files to json by running speechtotext.py


## 3. Text to Vector
Convert json files to vectors to dataframe with embeddings by running text_embed.py

## 4. Prompt Generation and feeding to LLMs
Read the joblib file for dataframe and load it into the memory. Create a relevant prompt as per user query and feed it to LLM

## 5. Run your app
Run the app.py file and on loading of page enter your query and the answer will be prompted.

