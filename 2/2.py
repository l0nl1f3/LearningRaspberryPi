import RPi.GPIO as GPIO
from time import sleep
	
KEY = 20
LED = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
p = GPIO.PWM(LED, 50)
p.start(0)
try:
    while(True):
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            sleep(0.05)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            sleep(0.05)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup();
