# MultiCore, _thread #                     #// Pico'nun çekirdeklerinin ayrı ayrı paralel kullanımını gösteren uygulama//#

# Raspberry Pi Piconun 2 adet işlemci çekirdeği(core) vardır. Bu çekirdekleri ayrı ayrı kullanarak birbirinden bağımsız
#// ve birbirini etkilemeyen 2 ayrı işi Pico'ya yaptırabiliriz. Buna _thread denir ve 2 core olduğundan en fazla 2 farklı iş yaptırılabilir.

# Ana "while" blogu içinde kırmızı LED her 1 saniyede yanarken, 2. _thread ile yeşil LED her 2sn. de yanacak.
#// ve bunlar tamamen birbirinden bağımsız çalışacak, birbirini etkileyen herhangi bir durum olmayacak.

from machine import Pin
import utime
import _thread            # _thread kütüphanesi

led_k = Pin(2, Pin.OUT)   # Kırmızı
led_y = Pin(4, Pin.OUT)   # Yeşil

led_k.value(0)
led_y.value(0)

def second_thread():                         # 2. _threadda yapılacak işlemler
    x=1
    while True:
        led_y.toggle()
        utime.sleep(2)
        print("2. _thread {0}. kez çalıştı." .format(x))
        x+=1
        
_thread.start_new_thread(second_thread, ())  # 2. _thread oluşturuldu (3. _thread oluşturulursa çakışma olur, 2 core için en fazla 2 _thread)

while True:                                  # 1. _thread ana döngüyü çalıştırıyor.
    led_k.toggle()
    utime.sleep(1)
    