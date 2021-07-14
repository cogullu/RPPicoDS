#buton ile LED Durum Değiştirme ve Yazdırma#                     #// butona tıklandığında LEDin durumunu(Açık-Kapalı) değiştiren ve bunu ekrana yazdıran uygulamadır. //#

from machine import Pin                                                                        
import utime

buton = Pin(5, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

while True:
    if buton.value() == 1:
        led.toggle()
        if led.value() == 1:
            print("LED Yandı")
        else:
            print("LED Söndü")
        utime.sleep(2)
                                         
