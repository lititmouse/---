form machine import pin
import utime

anjian = pin (15,pin.IN,pin.PULL_UP)

led = Pin(25,Pin.OUT)
led.off()
while True:
    if(anjian.value()==0):
        utime.sleep(0.01)
        if(anjian.value()==0):
            led.toggle
            utime.sleep(0.01)