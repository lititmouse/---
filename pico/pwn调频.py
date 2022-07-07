from machine import Pin
from machine import PWM 
import utime


LED  = PWM(Pin(25))
kongzhikou20 = machine.Pin(15,Pin.IN,Pin.PULL_UP)
kongzhikou19 = machine.Pin(14,Pin.IN,Pin.PULL_UP)

LED.freq(5000)

LED_duty = 0
LED_direction = 1
action = 1
while True :
    if action == 1:
        LED_duty += LED_direction
        if LED_duty >= 100:
            LED_duty = 100
            LED_direction = -1
        elif LED_duty <= 0:
            LED_duty = 0
            LED_direction = 1
        LED.duty_u16(int(LED_duty * 655.36))
    
    if kongzhikou20.value() == 0 :
        action = 1
    if kongzhikou19.value () == 0 :
        action = 0
        LED.duty_u16(0)
    if LED_duty%5 == 0:
        print(LED_duty)
    utime.sleep(0.01)
