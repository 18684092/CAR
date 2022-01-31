from machine import Pin, ADC

battery = ADC(Pin(35))
battery.atten(ADC.ATTN_11DB)

def getBattery():

     #Full range: 3.3v
    return battery.read()
