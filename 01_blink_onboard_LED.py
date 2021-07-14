#blink onboard LED#        #// 1 sn aralıklarla Raspberry Pi Pico üzerindeki yerleşik LED'i yakıp söndüren uygulama //#

import machine             # Piconun temel fonksiyonlarını ve GPIO pinlerini çalıştıran kütüphane dosyasıdır.
import utime               # Zamanla ilgili kütüphane dosyasıdır. Zaman ölçe, bekleme, gecikme vb. için kullanılır.

led_onboard = machine.Pin(25, machine.Pin.OUT)
# led_onboard ismindeki değişkenin Pin numarasını tanımladık ve çıkış olarak ayarladık.
# 25 numaralı pin Pico'nun üzerindeki tümleşik LED'e bağlıdır.

while True:                # Sonsuza kadar sürecek bir döngü oluşturduk. Böylece Pico hiç durmadan "while" bloğu içindeki aynı işlemleri yapacak.
# Aşağıdaki girintilere dikkat edin, 4-5 karakter(ya da 1 tab) boşluk bırakarak hangi yapının içinde olduğumuzu anlıyoruz.
     led_onboard.value(1)  # 25 numaralı GPIO pinine bağlı olan Pico'nun üzerindeki LED'in değerini 1 yaptık. LED yandı...
     utime.sleep(1)        # Pico çalışmasına 1 saniye ara vererek bekliyor.
     led_onboard.value(0)  # Pico tekrar çalışmaya başladı, yerleşik LED'in değerini 0 yaparak LED'i söndürdük...
     utime.sleep(1)        # Pico çalışmasına 1 saniye ara vererek bekliyor.
# "while" döngüsü burada bittiğinden tekrar "while" blogunun başına dönüyor...