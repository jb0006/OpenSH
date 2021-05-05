import pyaudio
import msvcrt
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SETTINGS = 3
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
stream = None

stop_recording = False

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


def record():

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SETTINGS)):
        data = stream.read(CHUNK)
        frames.append(data)

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



def record_with_buttons():

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
