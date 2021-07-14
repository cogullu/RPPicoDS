#Araç Trafik Lambası#                     #// Araçlar için Trafik lambası simülasyonu uygulamasıdır. //#

from machine import Pin                                                                        
import utime

led_k = Pin(2, Pin.OUT)   # Kırmızı
led_s = Pin(3, Pin.OUT)   # Sarı
led_y = Pin(4, Pin.OUT)   # Yeşil

aracGecisSure=5
aracBeklemeSure=5

led_k.value(0)                    # Kırmızı söner
led_s.value(0)                    # Sarı söner
led_y.value(0)                    # Yeşil Söner

while True:

    
    led_y.value(1)                    # Araçlara yeşil ışık yanıyor
    print("Araçlara yeşil yanıyor, araçlar geçiyor...")
    utime.sleep(aracGecisSure)        # Araçların geçiş süresi
    print("Yavaşla araçlara kırmızı yanacak...")


    led_y.value(0)                    # Işığa hızlı gelen araçların yavaşlaması için yeşil ışık fasılalı yanıp sönecek.
    utime.sleep(0.5)
    led_y.value(1)
    utime.sleep(0.5)
    led_y.value(0)
    utime.sleep(0.5)
    led_y.value(1)
    utime.sleep(0.5)
    led_y.value(0)
    utime.sleep(0.5)
    led_y.value(1)
    utime.sleep(0.5)
    led_y.value(0)
    utime.sleep(0.5)
    led_y.value(1)
    utime.sleep(0.5)                  # Burada aynı işlemleri tekraren yazmak kodun okunabilirliğini azaltıyor.
                                      #// bir sonraki uygulamada burayı "for" döngüsü ile yapacağız.
    
    led_y.value(0)                    # Yeşil Söner
    utime.sleep(0.5)
    
    
    led_s.value(1)                    # Sarı ışık yanar
    print("Dikkat araçlara kırmızı yanacak...")
    utime.sleep(2)                    # Sarı ışık 2 sn yanar
    led_s.value(0)                    # Sarı söner
    
    led_k.value(1)                    # Araçlara kırmızı yanar
    print("Araçlara kırmızı yanıyor, araçlar bekliyor...")
    utime.sleep(aracBeklemeSure)      # Araçlar kırmızı ışığı bekler
    led_s.value(1)                    # Kırmızı ile birlikte sarı yanar
    print("Hazırlan araçlara yeşil yanacak...")
    utime.sleep(3)                    # Kırmızı ve sarı 2 saniye yanık kalır
    led_k.value(0)                    # Kırmızı söner
    led_s.value(0)                    # Sarı söner
    

    


                                         
