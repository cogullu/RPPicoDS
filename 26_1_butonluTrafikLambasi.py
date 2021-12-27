#butonlu Trafik Lambası, kesmeler, interrupt#                     #// Yayalara buton ile çalışan Trafik lambası simülasyonu uygulamasıdır. //#

from machine import Pin                                                                        
import utime

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)

led_k = Pin(2, Pin.OUT)   # Araç Kırmızı Işık
led_s = Pin(3, Pin.OUT)   # Araç Sarı Işık
led_y = Pin(4, Pin.OUT)   # Araç Yeşil Işık

yayaRGB_green = Pin(17, Pin.OUT)   # Yaya Yeşil Işık,
yayaRGB_red = Pin(18, Pin.OUT)     # Yaya Kırmızı Işık

aracGecisSure=15
aracBeklemeSure=10                 # Değişken ismi olarak "yayaGecisSure" de kullanabilirdik.

led_k.value(0)                     # Tüm ışıkları söndürdük
led_s.value(0)                    
led_y.value(0)                   
yayaRGB_red.value(0)              
yayaRGB_green.value(0)

butonDurum = 0                     # Butona basılıp basılmadığını bu değişkenin değeri ile öğreneceğiz.
# butonDurum = 0 olduğu sürece "while" blogu içerisindeki "if" blogu çalışacak. Ne zamanki butona basılıp
#// butonDurum = 1 olacak, o zaman "else" blogu çalışacak ve yayalar geçmeye başlayacak.




#------------------------------------------Pin Kesmesi İşlemleri-------------------------------------------------#
# Butona basıldığında bekleme olmaksızın gerçekleşecek işlemler bu "kesme(interrupt)" altında tanımlanıyor.
# Kesmeler "while" ve diğer tüm blok ve fonksionlardan bağımsız olarak basıldığı anda gerçekleşir.
# Çok çeşitli kesme türleri bulunmaktadır. Burada pin kesmesini uygulayacağız.
def int_handler(pin):
    buton_1.irq(handler=None)
    print("Yaya butonuna basıldı...")
    global butonDurum              # "global" ifadesi ile bu fonksiyon içinde tanımlanmayan "butonDurum" değişkeninin değerini değiştiriyoruz.
    butonDurum = 1                 # butonDurum=1 yapıldı, böylece butona basıldığında "while" blogu içindeki "else" bloguna geçilecek.
    
    buton_1.irq(handler=int_handler)
 
buton_1.irq(trigger=Pin.IRQ_RISING, handler=int_handler)   # pin kesmesi ile ilgili işlemler
#-----------------------------------------------------------------------------------------------------------#



while True:
   
    if butonDurum == 0:                   # butonDurum sıfırsa yani butona basılmamışsa...
        led_y.value(1)                    # Araçlara yeşil ışık yanıyor
        yayaRGB_red.value(1)              # Yayalara kırmızı yanıyor
        print("Araçlar geçiyor...")
        utime.sleep(aracGecisSure)        # Araçlar geçiş süresi boyunca geçerler...
        
    else:                                 # butonDurum = 1 ise yani butona basılmışsa...
        print("Yavaşla kırmızı yanacak...")
        for i in range(5):
            led_y.value(0)               
            utime.sleep(0.5)
            led_y.value(1)
            utime.sleep(0.5)

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
    
        butonDurum = 0                    # Araçların tekrar geçiş yapabilmesi için butonun durumu sıfırlanıyor.

        


    

    


                                         
