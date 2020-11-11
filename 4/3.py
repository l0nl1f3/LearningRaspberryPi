import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import time
import spidev as SPI
import SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime as dt

RST = 19
DC = 16
bus = 0
device = 0
disp = SSD1306.SSD1306(rst=RST, dc=DC, spi=SPI.SpiDev(bus, device))

disp.begin()
disp.clear()
font = ImageFont.truetype('NotoMono-Regular.ttf', size=24)
digits = datasets.load_digits()
with_label = list(zip(digits.images, digits.target))

for index, (image, label) in enumerate(with_label[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

n_samples = len(digits.images)
print (n_samples)
data = digits.images.reshape((n_samples, -1))

classifier = svm.SVC(C = 1, gamma = 0.001)
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

print("Classifier result %s:\n%s\n" % (classifier, metrics.classification_report(expected, predicted)))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:10]):
    digit = Image.fromarray((image*8).astype(np.uint8), mode='L').resize((48,48)).convert('1')
    img = Image.new('1',(disp.width,disp.height),'black')
    img.paste(digit, (0, 16, digit.size[0], digit.size[1]+16))
    draw = ImageDraw.Draw(img)
    print(prediction)
    draw.text((64, 32), str(prediction), font = font, fill = 255)
    disp.clear()
    disp.image(img)
    disp.display()
    time.sleep(1) 
# plt.show()
