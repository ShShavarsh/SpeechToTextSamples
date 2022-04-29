
#pip install pipwin
#pipwin install pyaudio
#pipwin install pocketsphinx

import os
import speech_recognition as sr

command2mp3 = "ffmpeg -i C:\\Users\\Shavarsh\\MyProjects\\BuildUP\\Projects\\DesignReview.mp4 C:\\Users\\Shavarsh\\MyProjects\\BuildUP\\Projects\\DesignReview.mp3"
command2wav = "ffmpeg -i C:\\Users\\Shavarsh\\MyProjects\\BuildUP\\Projects\\x.mp3 C:\\Users\\Shavarsh\\MyProjects\\BuildUP\\Projects\\x.wav"
c5 = "C:\\Users\\Shavarsh\\MyProjects\\BuildUP\\Projects\\x.wav"

os.system(command2wav)

r = sr.Recognizer()
with sr.AudioFile(c5) as source:
    audio = r.record(source,duration=10)

sFinalResult = r.recognize_sphinx(audio,language = 'en-US')#, show_all = True
print(sFinalResult)







