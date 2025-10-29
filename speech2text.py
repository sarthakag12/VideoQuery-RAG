import whisper

model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audios/Conclusion & where to go from here.mp3", 
                          language="hi",
                          task="translate" )

print(result["text"])