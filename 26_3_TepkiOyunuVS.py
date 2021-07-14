#Buton Tepki Oyunu, 2 Kişilik, kesme, intrrupt#                     #// LED yandığında buton basışı tepki süresini ölçen uygulamadır. 2 Kişilik versiyon //#

from machine import Pin                                                                        
import utime
import urandom            # Rastgele sayı üretmeyi sağlayan kütüphanedir.

pressed = False

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
buton_3 = Pin(7, Pin.IN, Pin.PULL_DOWN)
led_k = Pin(2, Pin.OUT)   # Kırmızı LED
buzzer = Pin(10, Pin.OUT)


#------------------------------------------Pin Kesmesi İşlemleri-------------------------------------------------#
def buton_1_handler(pin):
    global pressed
    if not pressed:
        pressed= True
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print("1. Buton Kazandı. Tepki Süren=" + str(timer_reaction) + "ms")
        print("Tekrar dene...")
        buzzer.value(0)
    
def buton_3_handler(pin):
    global pressed
    if not pressed:
        pressed= True
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print("3. Buton Kazandı. Tepki Süren=" + str(timer_reaction) + "ms")
        print("Tekrar dene...")
        buzzer.value(0)
        
buton_1.irq(trigger=Pin.IRQ_RISING, handler=buton_1_handler)
buton_3.irq(trigger=Pin.IRQ_RISING, handler=buton_3_handler)
#---------------------------------------------------------------------------------------------------------------#
while True:
    for i in range(3):
        led_k.value(1)
        buzzer.value(1)
        utime.sleep(0.5)
        led_k.value(0)
        buzzer.value(0)
        utime.sleep(0.5)

    
    print("5-10 sn sonra LED yanacak...")
    utime.sleep(urandom.uniform(5,10))
    
    pressed = False
    timer_start = 0
    
    led_k.value(1)
    buzzer.value(1)
    print("ŞİMDİ")
    timer_start = utime.ticks_ms()

    utime.sleep(2)
    


    

    


                                         
