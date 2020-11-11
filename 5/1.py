from time import sleep
import datetime as dt
import smbus

def DEC2BCD(x):
    return x // 10 * 16 + x % 10

now = dt.datetime.now() 
print(now.year)

FixTime = [DEC2BCD(now.second), DEC2BCD(now.minute), DEC2BCD(now.hour), 0x03, DEC2BCD(now.day), DEC2BCD(now.month), DEC2BCD(now.year - 2000)]
Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

address = 0x68
register = 0x00
bus = smbus.SMBus(1)

def SetTime():
    bus.write_i2c_block_data(address, register, FixTime)
def ReadTime():
    return bus.read_i2c_block_data(address, register, 7)
def BCD2DEC(x):
    return (x // 16) * 10 + x % 16

SetTime()
try:
    while True:
        y = ReadTime()[::-1]
        for i in range(7):
            y[i] = BCD2DEC(y[i])
        print(y)
        sleep(1)
except KeyboardInterrupt:
    exit()
