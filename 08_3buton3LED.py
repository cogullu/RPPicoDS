#3 buton kullanarak 3 LED yakma-söndürme#                     #// 3 farklı butonla 3 farklı LEDi ayrı ayrı yakan-söndüren uygulamadır. //#

from machine import Pin                                                                        
import utime

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
buton_2 = Pin(6, Pin.IN, Pin.PULL_DOWN)
buton_3 = Pin(7, Pin.IN, Pin.PULL_DOWN)
led_k = Pin(2, Pin.OUT)   # Kırmızı
led_s = Pin(3, Pin.OUT)   # Sarı
led_y = Pin(4, Pin.OUT)   # Yeşil

while True:
    if buton_1.value() == 1:
        led_k.toggle()
        utime.sleep(2)
    if buton_2.value() == 1:
        led_s.toggle()
        utime.sleep(2)
    if buton_3.value() == 1:
        led_y.toggle()
        utime.sleep(2)
    


                                         
