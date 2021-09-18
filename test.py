import time
from machine import Pin, I2C
from mics6814 import MICS6814

i2c = I2C(1,scl=Pin(22),sda=Pin(21),freq=100000)
gas = MICS6814(i2c)

try:
    while True:
        readings = gas.read_all()
        time.sleep(1.0)
        print(readings)
except KeyboardInterrupt:
    pass