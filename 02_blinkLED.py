#blink LED#                    #// 1 sn aralıklarla yanıp sönen LED uygulaması //#

from machine import Pin        # machine kütüphanesinden sadece "Pin" sınıfını çağırdık.
                               #//Tüm machine fonksiyonunu yüklemediğimiz için hem daha az bellek kullandık,
                               #// hem de artık fonksiyonların başında "machine" ifadesini kullanmak zorunda değiliz.
import utime

led_pin = Pin(2, Pin.OUT)      # Dikkat edin, "Pin" fonksiyonunu başında "machine" kütüphane ismi olmadan kullanabiliyoruz.
# Yukarıda 2 numaralı pini çıkış olarak ayarladık ve led_pin değişkenine aktardık. Artık led_pin değişkeni 2 numaralı pin yerine kullanılacaktır.

while True: 
     led_pin.toggle()          # "toggle" fonksiyonu ilgili pini tersler. Yani bir önceki değeri 0 ise 1 yapar, 1 ise 0 yapar.
     utime.sleep(1)