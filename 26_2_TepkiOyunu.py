#Buton Tepki Oyunu, kesme, interreupt#                     #// LED yandığında buton basışı tepki süresini ölçen uygulamadır. //#

from machine import Pin                                                                        
import utime
import urandom            # Rastgele sayı üretmeyi sağlayan kütüphanedir.

pressed = False           # Butona basılıp basılmadığını anlayacağımız boolean türünde değişken.

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
led_k = Pin(2, Pin.OUT)   # Kırmızı LED
buzzer = Pin(10, Pin.OUT)


#------------------------------------------Pin Kesmesi İşlemleri-------------------------------------------------#
def buton_1_handler(pin):
    global pressed
    if not pressed:   #pressed
        pressed= True
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print("Tepki Süren=" + str(timer_reaction) + "ms")
        print("Tekrar dene...")
        buzzer.value(0)
        
buton_1.irq(trigger=Pin.IRQ_RISING, handler=buton_1_handler)
#---------------------------------------------------------------------------------------------------------------#



while True:
    print("Hazırlan...")
    for i in range(3):
        led_k.value(1)
        buzzer.value(1)
        utime.sleep(0.5)
        led_k.value(0)
        buzzer.value(0)
        utime.sleep(0.5)


    print("5-10 sn sonra LED yanacak...")
    utime.sleep(urandom.uniform(5,10))    #5-10 sn aralığında rastgele bekler.
    
    led_k.value(1)
    buzzer.value(1)
    print("ŞİMDİ")
    
    pressed = False       # Butona daha önceden basılmışsa sıfırlanıyor.
    timer_start = 0       # Önceki oyundan kalan tepki süresi sıfırlanıyor.
    timer_start = utime.ticks_ms()
      
    utime.sleep(2)    # 2 sn. tepki vermezse tekrar oyun başa döner.
    


    

    


                                         
