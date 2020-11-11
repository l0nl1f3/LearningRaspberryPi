import time
import spidev as SPI
import SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime as dt
from time import sleep

RST = 19
DC = 16
bus = 0
device = 0
disp = SSD1306.SSD1306(rst=RST, dc=DC, spi=SPI.SpiDev(bus, device))

disp.begin()
disp.clear()

pku_logo = Image.open('pku.png').resize((42, 42), Image.ANTIALIAS).convert('1')
print(pku_logo.size)

font = ImageFont.truetype('NotoMono-Regular.ttf', size=12)
image = Image.new('RGB', (disp.width, disp.height), 'black').convert('1')
image.paste(pku_logo, (0, 28, pku_logo.size[0], 28 + pku_logo.size[1]))

# draw.text((6, 35), 'Hello, world', font = font, fill = 255)
# disp.image(image)
# disp.display()

now = dt.datetime.now()
target = dt.datetime.strptime('2020-11-12 08:00:00', '%Y-%m-%d %H:%M:%S')

draw = ImageDraw.Draw(image)
# draw.text((0,0), 'T-T', font = font, fill = 1)
# disp.image(image)
# disp.display()

try:
    while True:
        now = dt.datetime.now()
        count_down = target - now
        image = Image.new('RGB', (disp.width, disp.height), 'black').convert('1')
        image.paste(pku_logo, (0, 32, pku_logo.size[0], 32 + pku_logo.size[1]))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), str(count_down)[:-7], font = font, fill = 255)
        disp.image(image)
        disp.display()
        sleep(1)
except KeyboardInterrupt:
    pass
