import wave
import pyaudio as pa
import RPi.GPIO as GPIO
import sys
from time import sleep

KEY = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)

CHUNK = 512
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100
SECONDS = 1.5

n = 1
while True:
    sleep(0.1)

    record = not GPIO.input(KEY)
    if record:
        p = pa.PyAudio()
        stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK)

# input 0 when pressed
        audio_buf = []
        for i in range(int(RATE / CHUNK * SECONDS)):
            frame = stream.read(CHUNK)
            audio_buf.append(frame)
        wf = wave.open('3' + str(n) + '.wav', 'wb')
        n += 1
        print(n)
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(audio_buf))
        wf.close()
        recording = False
    
        print('done recording')

        stream.stop_stream()
        stream.close()
        p.terminate()
