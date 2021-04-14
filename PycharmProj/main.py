import speech_recognition as sr
import pyaudio
import wave
from gtts import gTTS
from os import path
from playsound import playsound

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SETTINGS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE/CHUNK * RECORD_SETTINGS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(b''.join(frames))
wf.close()

# SPEECH RECOGNITION

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

outputString = r.recognize_google(audio)

try:
    print("Google thinks you said " + outputString)
except sr.UnknownValueError:
    print("Google could not understand audio")
except sr.RequestError as e:
    print("Google error; {0}".format(e))

tts = gTTS(outputString)
tts.save("tts.mp3")
playsound("tts.mp3")