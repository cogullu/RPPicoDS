#POT Kullanımı, ADC#                    #// Potansiyometre değerlerini seri ekrana yazdıran uygulama //#

from machine import ADC            # machine kütüphanesinden ADC sınıfını analog değerleri okumak için kodumuza dahil ettik.                                       
import utime

pot = ADC(27)                      # 27 numaralı Analog girişli pini tanımladık.
# Raspberry Pi Pico' da sadece 26,27 ve 28 numaralı pinler analog giriş olarak ayarlanabilir.

while True: 
     print("Potansiyometre Değeri=", pot.read_u16())    # potansiyometreden gelen değeri "read()" ile okuduk, u16 fonksiyonu ile de 16 bitlik formata çevirdik.
     # Raspberry Pi Pico analog girişleri 12 bitliktir. En fazla 4096 değeri okunabilmesi gerekirken, u16 ile 16 bit yani 65536'ya kadar simüle edilebiliyor.
     utime.sleep(1)                # 1 sn. aralıklarla değer okutuyoruz.