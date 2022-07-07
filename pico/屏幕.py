from machine import Pin
from machine import I2C

ic2= machine.I2C(id=0,scl=Pin(17),sda=Pin(16),)
print(ic2.scan())
