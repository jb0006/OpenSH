import speech_recognition as sr
import pyaudio
import wave
from gtts import gTTS
from os import path
from playsound import playsound
import msvcrt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SETTINGS = 3
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Press Esc to start recording")

while 1:
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            break

print("* recording")

frames = []



while 1:
    data = stream.read(CHUNK)
    frames.append(data)
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            break

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

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

tts = gTTS(outputString)
tts.save("tts.mp3")
playsound("tts.mp3")
