#PIR Kullanımı#                     #// PIR Sensörü Kullanımı. //#
import utime
from machine import Pin, PWM
# PIR sensörü 5m'ye kadar olan cisimlerin hareketini algılar.
# PIR üzerindeki Sx potansiyometresi ile algılama mesafesini 3m-5m olarak değiştiriken
# Tx potansiyometresi ile sensör algılama sonrası ne kadar lojik 1  göndereceği ile ilgilidir.
# Potansiyometrelerin kesik kısımları birbirine bakacak şekilde ayarlandığında stabil çalışmaktadır.
# Sensörün seri-ani değişimlere çok hızlı tepki vermeyeceğini unutmayın.

PIR= Pin(19, Pin.IN, Pin.PULL_DOWN)   # PULL_DOWN olursa sensör algıladığında lojik 1, PULL_UP olursa lojik 0 verir.

buzzer = PWM(Pin(10))
buzzer.freq(2000);
buzzer.duty_u16(0)

while True:
    if PIR.value() == 1:
        print ("PIR Çalışıyor...")
        buzzer.duty_u16(40000)
        utime.sleep(1)
        buzzer.duty_u16(0)
    else:
        print("Hareket bekleniyor...")
        
    utime.sleep(0.5)                   # Her yarım saniyede kontrol eder.