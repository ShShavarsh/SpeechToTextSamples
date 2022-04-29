import os
import speech_recognition as sr


c5 = "C:\\Users\\Shavarsh\\MyProjects\\BuildUP\\Projects\\x.wav"

r = sr.Recognizer()
with sr.AudioFile(c5) as source:
    audio = r.record(source,duration=10)

sFinalResult = r.recognize_google(audio,language = 'en-US')#show_all = True
print(sFinalResult)







