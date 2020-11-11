import time
import spidev as SPI
import SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
RST = 19
DC = 16
bus = 0
device = 0
disp = SSD1306.SSD1306(rst=RST, dc=DC, spi=SPI.SpiDev(bus, device))

disp.begin()
disp.clear()
disp.display

pku_logo = Image.open('pku.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

font = ImageFont.truetype('NotoMono-Regular.ttf', size=16)
image = Image.new('RGB', (disp.width, disp.height), 'black').convert('1')
draw = ImageDraw.Draw(image)
draw.text((6, 35), 'Hello, world', font = font, fill = 255)
disp.image(image)
disp.display()

