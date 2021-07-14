#AraçYaya Trafik Lambası#                     #// Araçlar ve Yayalar için Trafik lambası simülasyonu uygulamasıdır. //#

from machine import Pin                                                                        
import utime

led_k = Pin(2, Pin.OUT)   # Araç Kırmızı Işık
led_s = Pin(3, Pin.OUT)   # Araç Sarı Işık
led_y = Pin(4, Pin.OUT)   # Araç Yeşil Işık

yayaRGB_green = Pin(18, Pin.OUT)   # Yaya Yeşil Işık,
yayaRGB_red = Pin(17, Pin.OUT)     # Yaya Kırmızı Işık

aracGecisSure=15
aracBeklemeSure=10

led_k.value(0)                    # Tüm ışıkları söndürdük
led_s.value(0)                    
led_y.value(0)                   
yayaRGB_red.value(0)              
yayaRGB_green.value(0)    

while True:        
    
    led_y.value(1)                    # Araçlara yeşil ışık yanıyor
    yayaRGB_red.value(1)              # Yayalara kırmızı yanıyor
    print("Araçlar geçiyor... Yayalar bekliyor...")
    utime.sleep(aracGecisSure)        # Araçların geçiş süresi
    print("Yavaşla kırmızı yanacak...")
 
    #// Işığa hızlı gelen araçların yavaşlaması için "for" döngüsü ile yeşil ışık 5 kez fasılalı yanıp sönecek.
    for i in range(5):               # range() fonksiyonu aralık belirtir. Burada 0-5 aralığında(0 dahil 5 dahil değil), i'nin 0-1-2-3 ve 4 değerleri için döngü 5 kez tekrarlanır.
        # Girintiye dikkat, for BAŞLADI...
        led_y.value(0)               
        utime.sleep(0.5)
        led_y.value(1)
        utime.sleep(0.5)
        # Girintiye dikkat, for BİTTİ...

    led_y.value(0)                    # Yeşil Söner
    utime.sleep(0.5)
    
    led_s.value(1)                    # Sarı ışık yanar
    print("Dikkat kırmızı yanacak...")
    utime.sleep(2)                    # Sarı ışık 2 sn yanar
    led_s.value(0)                    # Sarı söner
    
    led_k.value(1)                    # Araçlara kırmızı yanar
    utime.sleep(2)                    # Işıkta duramayan arabalar ihtimaline karşı 2 sn. daha bekleyip yayalara yeşil yakalım
    yayaRGB_red.value(0)              # Yaya kırmızı söner
    yayaRGB_green.value(1)            # Yayalara yeşil yanar
    print("Araçlar bekliyor...Yayalar geçiyor")
    
    utime.sleep(aracBeklemeSure)      # Araçlar kırmızı ışığı bekler
    yayaRGB_green.value(0)            # Yaya yeşil ışık söner
    yayaRGB_red.value(1)              # Yayalara kırmızı yanar
    utime.sleep(3)                    # Yaya geçidinde kalanlar için biraz daha bekleyelim
    led_s.value(1)                    # araçlara kırmızı ile birlikte sarı yanar
    print("Araçlar hazırlanır, araçlara yeşil yanacak...")
    utime.sleep(4)                    # Kırmızı ve sarı 2 saniye yanık kalır
    led_k.value(0)                    # Kırmızı söner
    led_s.value(0)                    # Sarı söner
    

    


                                         
