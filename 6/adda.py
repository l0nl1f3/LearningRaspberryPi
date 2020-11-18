import smbus
import time # 包含相关库文件
address = 0x48
A0 = 0x40
bus = smbus.SMBus(1) # 初始化 i2c Bus
value = 0
while True:
    bus.write_byte(address,A0)
    # value = bus.read_byte(address) # 循环读出
    bus.write_byte_data(address, A0, min(value, 511 - value))
    print(min(value, 511 - value))
    value = (value + 8) % 512
    time.sleep(0.05)
