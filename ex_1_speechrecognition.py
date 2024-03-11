import speech_recognition as sr
import datetime

# Initialize the recognizer
recognizer = sr.Recognizer()

# Open the audio file (replace with your file path)
audio_file_path = "./audio.wav"
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)

# Recognize the speech
print(datetime.datetime.now())
try:
    text = recognizer.recognize_google(audio_data)
    print(f"Transcribed text: {text}")
except sr.UnknownValueError:
    print("Could not understand audio.")

print(datetime.datetime.now())
