from machine import Pin
import utime
jidianqi = machine.Pin(29,mode=Pin.OUT,)

while True:
    jidianqi.off()
    utime.sleep(1)
    jidianqi.on()
    utime.sleep(1)
