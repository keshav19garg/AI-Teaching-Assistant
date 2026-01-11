# RAG Based AI Teaching Assistant

This project is a Retrieval-Augmented Generation (RAG) based AI Teaching Assistant designed to help users quickly locate where a specific topic is taught within long courses of any kind taught in any language. Instead of manually searching through lectures, users can ask questions in natural language and receive relevant video segments with exact timestamps, along with clear explanations.

The system is **domain-agnostic** and works for any course, regardless of subject or level.

# How to use this RAG based AI Teaching Assistant for your own course

## 1. Video to Audio Conversion
Convert all your videos to mp3 and save them in audios folder using the naming format ("filenumber","_","filename"). Eg:- 01_FileName

## 2. Audio to Text Conversion
Convert all mp3 files to json by running speechtotext.py


## 3. Text to Vector
Convert json files to vectors to dataframe with embeddings by running text_embed.py

## 4. Prompt Generation and feeding to LLMs
Read the joblib file for dataframe and load it into the memory. Create a relevant prompt as per user query and feed it to LLM

## 5. Run your app
Run the app.py file and on loading of page enter your query and the answer will be prompted.

