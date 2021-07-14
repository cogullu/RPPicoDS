#butona basildigi sürece LED Yakma#                     #// buton basılı iken LED yanan butondan çekilince LED sönen uygulamadır. //#

from machine import Pin                                                                        
import utime

buton = Pin(5, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

while True:
    if buton.value() == 1:
        led.value(1)
    else:
        led.value(0)

                                         
