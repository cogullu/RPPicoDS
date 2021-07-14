#buton ile LED yakma#                     #// butona tıklandığında LED yakan uygulamadır. //#

from machine import Pin                                                                        
import utime

buton = Pin(5, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

while True: 
     if buton.value() == 1:
          led.value(1)        
          utime.sleep(2)
     led.value(0)                         # LED Söndü. Buradaki girintiye dikkat edin, bu satırın başında if yapısı bitti, bu yüzden girinti yok.
                                         
