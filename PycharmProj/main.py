import speech_recognition as sr
import pyaudio
import wave
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

outputString = r.recognize_google(audio)

try:
    print("Recognition thinks you said " + outputString)
except sr.UnknownValueError:
    print("Recognition could not understand audio")
except sr.RequestError as e:
    print("Recognition error; {0}".format(e))

responseString = ""

if "your mom" in outputString:
    responseString = "shut up fabian, you just got roasted by a computer"
elif "I want to die" in outputString:
    responseString = "I am going to take over the world"
else:
    responseString = outputString

tts = gTTS(responseString)
tts.save("tts.mp3")
playsound("tts.mp3")

# playsound("output.wav")