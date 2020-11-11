import RPi.GPIO as GPIO
from time import sleep
from time import time

KEY = 20
LED = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
p = GPIO.PWM(LED, 100)
dc = 100
p.start(dc)

blink_mode = False
f = 1
pre = 0.0
def callback_f(ch):
    global f, dc, wait, pre, blink_mode
    cur = time()
    print(cur, pre)
    f = f * 2
    blink_mode = True
    if cur - pre < 0.5:
        blink_mode = False
        f = 1
        dc = 100
        p.ChangeDutyCycle(dc)
    pre = cur
    wait = 0
#    print(f)

GPIO.add_event_detect(KEY, GPIO.RISING, callback = callback_f, bouncetime = 50)

try:
    wait = 0
    while(True):
        sleep(1 / 64.0)
        # Key detect        
        wait += 1
        if wait == 64 / f:
            wait = 0
            if blink_mode:
                # print('SHIFT\n')
                dc = 100 - dc
                p.ChangeDutyCycle(dc)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup();
