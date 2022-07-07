from machine import Pin 
import utime


key4 = machine.Pin(3,mode=Pin.IN,pull= Pin.PULL_UP)
key5 = machine.Pin(4,mode=Pin.IN,pull= Pin.PULL_UP)
key6 = machine.Pin(5,mode=Pin.IN,pull= Pin.PULL_UP)
key7 = machine.Pin(6,mode=Pin.IN,pull= Pin.PULL_UP)
relation = machine.Pin(29,mode=Pin.OUT)
jidianqi = machine.Pin(16,mode=Pin.OUT)
relation.off()
while True:
    if(key4.value()==0):
        utime.sleep(0.1)
        if(key4.value()==0):
            relation.toggle()
            utime.sleep(0.5)
