import RPi.GPIO as GPIO
from time import sleep

file_path = '/sys/bus/w1/devices/28-3a19706989ff/w1_slave'

LED = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
p = GPIO.PWM(LED, 100)
blink = False
wait = 0
p.start(wait * 100)

try:
    n = 0
    while True:
        wait = 1 - wait
        n += 1
        if blink:
            p.ChangeDutyCycle(100 * wait)
        sleep(0.1)
        if n != 10:
            continue
        n = 0
        f = open(file_path, 'r')
        line = f.readlines()
        f.close()
        if line[0].find('YES') != -1:
            t = line[1].find('t=')
            temp = int(line[1][t+2:])/1000
            print(temp)
            if temp > 28:
                if not blink:
                    [blink, wait] = [True, 0]
            else:
                [blink, wait] = [False, 0]

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
