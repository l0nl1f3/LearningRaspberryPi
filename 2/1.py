import RPi.GPIO as GPIO
from time import sleep
	
KEY = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_UP)

print("Key Test:")

def callback_fun(ch):
    print("KEY PRESS")
    sleep(2)
GPIO.add_event_detect(KEY, GPIO.RISING, callback = callback_fun, bouncetime = 200)

while True:
    sleep(0.1)
GPIO.clean();
