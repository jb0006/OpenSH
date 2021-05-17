import speech_recognition as sr
from gtts import gTTS
from os import path
from playsound import playsound

import sm_recordAudio
sm_recordAudio.record()

# Speech Recognition

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# outputString = r.recognize_google(audio).lower()
outputString = r.recognize_bing(audio).lower()
print(outputString)

import response_database as rs

responseString = ""
codeToRun = ""

#for res in rs.all:
#    responseString, codeToRun = res.Procedure(outputString)
#    if responseString is not "":
#        break

responseString = rs.EvaluateSpeech(outputString)

if responseString is not "":
    tts = gTTS(responseString)
    tts.save("tts.mp3")
    playsound("tts.mp3")
    # if codeToRun != "":
    #    exec(codeToRun)
