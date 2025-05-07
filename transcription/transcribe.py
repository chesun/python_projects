# use Whisper to transcribe voice recordings
import whisper

model = whisper.load_model("turbo")
# result = model.transcribe("test.m4a")

result = model.transcribe("anujit_may_6.m4a")
# print(result["text"])

with open("anujit_may_6_transcription.txt", "w") as file:
    file.write(result["text"])