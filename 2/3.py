import RPi.GPIO as GPIO
from time import sleep
	
KEY = 20
LED = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
p = GPIO.PWM(LED, 50)
dc = 100
p.start(dc)

def callback_f(ch):
    print('KEY_PRESS')
    global dc
    p.ChangeDutyCycle(100 - dc)
    dc = 100 - dc

GPIO.add_event_detect(KEY, GPIO.RISING, callback = callback_f, bouncetime = 200)

try:
    while(True):
        sleep(0.1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup();
