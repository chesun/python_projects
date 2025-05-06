# use Whisper to transcribe voice recordings
import whisper

model = whisper.load_model("turbo")
# result = model.transcribe("test.m4a")

result = model.transcribe("lunch_talk.m4a")
# print(result["text"])

with open("lunch_talk_transcription.txt", "w") as file:
    file.write(result["text"])