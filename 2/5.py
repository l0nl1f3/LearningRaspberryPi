import numpy as np
import RPi.GPIO as GPIO
from time import sleep

n = 2000
x1 = np.random.rand(n) * 10
x2 = np.random.rand(n) * 10
x3 = np.ones((n, ))
[m1, m2, m3] = [0.5, 0.5, 1] 
y = m1 * x1 + m2 * x2 + m3 + np.random.randn(n)
print(y)
w = np.random.rand(3)

Epoch = 1
alpha = 1e-5
print(x3)
def my_callback(ch):
    global Epoch
    Epoch += 1
    print(Epoch)
    d = w[0] * x1 + w[1] * x2 + w[2] * x3 - y
    print(w)
    print(np.sum(d * d))
    for i in range(n):
        w[0] -= alpha * x1[i] * d[i]
        w[1] -= alpha * x2[i] * d[i]
        w[2] -= alpha * x3[i] * d[i]

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(20, GPIO.RISING, callback = my_callback)

while (True):
    sleep(0.05)
