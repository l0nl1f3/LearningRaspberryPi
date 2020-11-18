#!/usr/bin/env python3
import smbus
import spidev as SPI
from time import sleep
from threading import Thread,Lock

import SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



#mylock = Lock()
delta = 5
value = 0
adj_value = 0
address = 0x48
A0= 0x40
bus=smbus.SMBus(1)

def da_led():
    val=0
    global delta
    while True:
        # print(delta)
        while val+delta<256:
            bus.write_byte_data(address,0x40,val)
            val+=delta
            sleep(0.05)
        while val-delta>=0:
            bus.write_byte_data(address,0x40,val)
            val-=delta
            sleep(0.05)


RST = 19
DC = 16
bus_id = 0
device = 0
disp = SSD1306.SSD1306(rst=RST, dc=DC, spi=SPI.SpiDev(bus_id, device))
disp.begin();
disp.clear();
font = ImageFont.truetype('NotoMono-Regular.ttf', size=12)


def da_oled():
    global value, adj_value
    while True:
        # print(value, adj_value)
        image = Image.new('RGB', (disp.width, disp.height), 'black').convert('1')
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), 'Voltage: ' + str(round(adj_value, 2)), font = font, fill = 255)
        draw.text((0, 24), 'Digital = ' + str(value), font = font, fill = 255)
        freq = round(1.0 / (0.05 * 512 / delta), 2)
        draw.text((0, 48), 'Freq = ' + str(freq),  font = font, fill = 255); 
        disp.image(image)
        disp.display()
        sleep(0.5)

mythread = Thread(target=da_led)
mythread.setDaemon(True)
mythread.start()

OLEDthread = Thread(target=da_oled);
OLEDthread.setDaemon(True)
OLEDthread.start();

bus.write_byte(address,A0)
while True:
    value = bus.read_byte(address)
    adj_value = (value/255.0)*3.3
    delta = int(value / 2)
    # print(adj_value,'V')
    sleep(0.1)
