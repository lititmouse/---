from machine import Pin,ADC
import utime

wenduchuanganqi = machine.ADC(4)

while True:
    wendu_shuzhi = wenduchuanganqi.read_u16()*3.3/65535
    wendu = 17-(wendu_shuzhi-0.706)/0.001721
    print("现在温度为{0:.1f}".format(wendu))
    utime.sleep(1)

vbn