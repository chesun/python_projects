# use Whisper to transcribe voice recordings
import whisper

model = whisper.load_model("large")
# result = model.transcribe("test.m4a")

result = model.transcribe("For Christina.m4a")
# print(result["text"])

with open("patience-hopkins_transcription.txt", "w") as file:
    file.write(result["text"])
