from python_speech_features import mfcc
from hmmlearn import hmm
import numpy as np
from scipy.io import wavfile
import wave
import pyaudio as pa
import RPi.GPIO as GPIO
from time import sleep

def compute_mfcc(file):
    fs, audio = wavfile.read(file)
    mfcc_feat = mfcc(audio)
    return mfcc_feat

class Model():
    def __init__(self, CATEGORY=None, n_comp=3, n_mix = 3, cov_type='diag', n_iter=1000):
        super(Model, self).__init__()
        self.CATEGORY = CATEGORY
        self.category = len(CATEGORY)
        self.n_comp = n_comp
        self.n_mix = n_mix
        self.cov_type = cov_type
        self.n_iter = n_iter
        # 关键步骤，初始化models，返回特定参数的模型的列表
        self.models = []
        for k in range(self.category):
            model = hmm.GMMHMM(n_components=self.n_comp, n_mix = self.n_mix, covariance_type=self.cov_type, n_iter=self.n_iter)
            self.models.append(model)
    def train(self, wavdict, labeldict):
        # mfcc_feat = compute_mfcc(wavdict[x])
        for x in wavdict.keys():
            mfcc_feat = compute_mfcc(wavdict[x])
            n = int(labeldict[x])
            model = self.models[n]
            model.fit(mfcc_feat)
    def score(self, mfcc):
        re = []
        for x in range(self.category):
            re.append(self.models[x].score(mfcc))
        return re
names = ['01', '02', '03', '04', '05', '11', '12', '13', '14', '15', '16', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '36']

wavdict = dict()
labeldict = dict()

for idx in names:
    cat = idx[0]
    fn = idx + '.wav'
    wavdict[idx] = fn
    labeldict[idx] = cat

model = Model([0, 1, 2, 3])
model.train(wavdict, labeldict)

print('train down!!')
for x in wavdict.keys():
    mfcc_feat = compute_mfcc(wavdict[x])
    re = model.score(mfcc_feat)
    print(np.array(re).argmax())

KEY = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)

CHUNK = 512
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100
SECONDS = 1.5

name = ['open', 'close', 'blink', 'faster']

while True:
    record = not GPIO.input(KEY)
    if record:
        print('begin recording..')
        p = pa.PyAudio()
        stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK)

# input 0 when pressed
        audio_buf = []
        recording = False
        n = 1

        for i in range(int(RATE / CHUNK * SECONDS)):
            record = not GPIO.input(KEY)
            frame = stream.read(CHUNK)
            audio_buf.append(frame)

        wf = wave.open('temp.wav', 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(audio_buf))
        wf.close()
        re = model.score(compute_mfcc('temp.wav'))
        print(name[np.array(re).argmax()])
        print(re)
        print('end recording')

        stream.stop_stream()
        stream.close()
        p.terminate()
