# MultiCore, _thread, baton, senkronize, semafor #      #// Pico'nun çekirdeklerinin senkron kullanımını gösteren uygulama//#

# 1. core ve 2. core birbirinin işi bittikten sonra çalışacak. Paralel çalışmayacak. Böylece global kullanılacak değişkenlerdeki
#// değişimler kontrol altına alınabilir.
# Bu uygulamada kırmızı LED yanar, 1sn sonra yeşil LED yanar, 2sn sonra kırmızı LED söner, 1sn sonra yeşil LED söner, 2sn sonra tekrar kırmızı LED yanar.

from machine import Pin
import utime
import _thread

led_k = Pin(2, Pin.OUT)   # Kırmızı
led_y = Pin(4, Pin.OUT)   # Yeşil

led_k.value(0)
led_y.value(0)

baton = _thread.allocate_lock()              # Seknron çalışma için baton semafor nesnesi oluşturuluyor.

def second_thread():                         # 2. _threadda yapılacak işlemler
    x=1
    while True:
        baton.acquire()                      # Diğer _thread kilitlendi.
        led_y.toggle()
        utime.sleep(2)
        print("2. _thread {0}. kez çalıştı." .format(x))
        x+=1
        baton.release()                      # _thread kilidi açıldı.
        
_thread.start_new_thread(second_thread, ())  # 2. _thread oluşturuldu (3. _thread oluşturulursa çakışma olur, 2 core için en fazla 2 _thread)

while True:                                  # 1. _thread ana döngüyü çalıştırıyor.
    baton.acquire()                          # Diğer _thread kilitlendi.
    led_k.toggle()
    utime.sleep(1)
    baton.release()                          # _thread kilidi açıldı.
    