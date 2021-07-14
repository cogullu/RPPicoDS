#POT ile LED, ADC, PWM#                    #// Potansiyometre kullanarak LED' in parlaklığını ayarlayan uygulamadır //#

from machine import ADC, PWM, Pin     # machine kütüphanesinden PWM sınıfını pinlerden verilecek gerilimi ayarlamak için kodumuza dahil ettik.
# PWM olarak kullanılabilecek pinler için pin diyagramına bakmalısınız. Aynı PWM pinini birden fazla kullanmamalısınız.
import utime

pot = ADC(27)                  # 27 numaralı Analog girişli pini tanımladık.
led1 = PWM(Pin(2))             # Parlaklık değeri ayarlanacak LED
led1.freq(1000)                # LED' in 1 sn. deki çalışma frekansını ayarladık.

while True: 
     print("LED'in Parlaklık Değeri=", pot.read_u16())    # Potansiyometreden gelen değeri "read()" ile okuduk, u16 fonksiyonu ile de 16 bitlik formata çevirdik.  
     led1.duty_u16(pot.read_u16())                        # Pin çıkışlarını ayarlıyoruz, Potansiyometreden okunan değer kadar LED'in parlaklığını değiştirdik.
     # Hem analog değeri okurken hem de PWM çıkışı verirken u16 kullandık. Böylece okunan ve çıkan değerler arasında özdeşleştirme yaptık.
     utime.sleep(1)        