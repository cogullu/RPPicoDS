#buton ile LED Durum Değiştirme#                     #// butona tıklandığında LEDin durumunu(Açık-Kapalı) değiştiren uygulamadır. //#

from machine import Pin                                                                        
import utime

buton = Pin(5, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

while True: 
     if buton.value() == 1:
          led.toggle()        
          utime.sleep(2)
                                         
