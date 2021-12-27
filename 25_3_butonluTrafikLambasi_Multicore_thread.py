#butonlu Trafik Lambası, Multicore, _thread#                     #// Yayalara buton ile çalışan Trafik lambası simülasyonu uygulamasıdır. //#
# Daha önce kesme ile yaptığımız uygulamayı şimdi _thread ile yapacağız.

from machine import Pin                                                                        
import utime
import _thread

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

butonDurum = False                     # Butona basılıp basılmadığını bu değişkenin değeri ile öğreneceğiz.
# butonDurum = False olduğu sürece "while" blogu içerisindeki "if" blogu çalışacak. Ne zamanki butona basılıp
#// butonDurum = True olacak, o zaman "else" blogu çalışacak ve yayalar geçmeye başlayacak.


#------------------------------------------Multicore, _thread İşlemleri-------------------------------------------------#
def butona_okuma_thread():                         # 2. _threadda yapılacak işlemler, butona basılıp basılmadığı kontrol edilecek.
    global butonDurum
    while True:
        if buton_1.value() == 1:
            print("Butona basıldı, yayalar hazırlanıyor...")
            butonDurum=True
        utime.sleep(0.1)                           # Sistem kararlılığı için 0.1 sn bekliyoruz.           
        
_thread.start_new_thread(butona_okuma_thread, ())  # 2. _thread oluşturuldu.
#------------------------------------------------------------------------------------------------------------------------#

while True:
   
    if butonDurum == False:               # butonDurum False yani butona basılmamışsa...
        led_y.value(1)                    # Araçlara yeşil ışık yanıyor
        yayaRGB_red.value(1)              # Yayalara kırmızı yanıyor
        print("Araçlar geçiyor...Yayalar bekliyor")
        utime.sleep(aracGecisSure)        # Araçlar geçiş süresi boyunca geçerler...
        
    else:                                 # butonDurum = True ise yani butona basılmışsa...
        print("Yavaşla araçlara kırmızı yanacak...")
        for i in range(10):
            led_y.toggle()              
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
    
        butonDurum = False                # Araçların tekrar geçiş yapabilmesi için butonun durumu sıfırlanıyor.

        


    

    


                                         
