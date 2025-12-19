
# audio_path="audios/motivation.mp3"
# chunk_len_ms=20000

# audio=AudioSegment.from_file(audio_path)
# audio_duration_ms=len(audio)

# for i in range(0,audio_duration_ms,chunk_len_ms):
#     start_ms=i
#     end_ms=min(i+chunk_len_ms,audio_duration_ms)
#     chunk=audio[start_ms:end_ms]

#     chunk_file = f"temp_chunk_{i//chunk_len_ms}.mp3"
#     chunk.export(chunk_file, format="mp3")