#Mesafe Sensörü Kullanımı#                    #// HC-SR04 ultrasonic mesafe sensörü kullanımı ile mesafe ölçen uygulama //#
# HC-SR04 mesafe sönsörü yaklaşık 8 cm nin altındaki değerlerde hatalı ölçüm yapabilir!
# Ölçüm aralığı teorik 2cm- 400cm, uygulamada yaklaşık 10 cm - 250 cm dir.
from machine import Pin, I2C
import utime

trigger = Pin(8, Pin.OUT)               # Sinyal gönderen pindir.
echo = Pin(9, Pin.IN)                   # Gönderilen sinyali okuyan pindir.

#-----------------------LCD I2C ekranı çalıştırmak için gerekli kodlar.------------------------------------------#
from lcd_api import LcdApi          # LCD komutlarını çalıştıran kütüphane, Piconun içinde mutlaka olmalıdır.
from pico_i2c_lcd import I2cLcd     # LCD komutlarını çalıştıran kütüphane, Piconun içinde mutlaka olmalıdır.
I2C_ADDR     = 0x27                 # LCD I2C ekran adresi, farklı olabilir, datasheet bakmak gerekir
I2C_NUM_ROWS = 2                    # LCD I2C ekran satır sayısı
I2C_NUM_COLS = 16                   # LCD I2C ekran sütun sayısı

sda=Pin(20)                         # LCD I2C ekranın SDA bağlantı pini
scl=Pin(21)                         # LCD I2C ekranın SCL bağlantı pini

i2c = I2C(0, sda=sda, scl=scl, freq=400000)              # Hata alırsanız frekansı değiştirin.(100000, 200000, 300000, 400000 vs.)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
#-------------------------------------------------------------#

def mesafe():                           # Mesafeyi hesaplayan fonksiyon.
   trigger.low()                        # trig pinini kapattık.
   utime.sleep_us(2)                    # 2 mikrosnaiye kapalı bekledik.
   trigger.high()                       # trig pinini açtık.
   utime.sleep_us(5)                    # trig pinini 5 mikrosnaiye açık bıraktık, böylece mesafeyi ölçmek için 5 mikrosaniye sinyal gönderdik.
   trigger.low()                        # Sinyali gönderdikten sonra trig pinini tekrar kapattık.
   # Aşağıda echo pini ile trigden gönderdiğimiz sinyali okuyacağız. 
   while echo.value() == 0:             # Burada sinyal almadığı zaman ölçülüyor.
       sinyalKapali = utime.ticks_us()
   while echo.value() == 1:             # Burada sinyal aldığı zaman ölçülüyor.
       sinyalAcik = utime.ticks_us()
   gecenZaman = sinyalAcik - sinyalKapali    # İki sinyal arasındaki geçen zaman hesaplanıyor.
   uzaklik = (gecenZaman * 0.0343) / 2 # Uzaklık ölçülen zaman göre hesaplanıyor. Formül HC-SR04' ün çalışma prensibidir.
   print("Uzaklık= ",uzaklik,"cm")
   
   lcd.move_to(4, 0)                   # Uzaklık değeri LCD I2C ekranda yazdırılıyor...
   lcd.putstr("Uzaklik")
   lcd.move_to(4, 1)
   lcd.putstr(str(uzaklik))            # LCD ekranda göstermek için float değeri stringe çeviren str() fonksiyonunu kullandık.
   lcd.move_to(14, 1)
   lcd.putstr("cm")
   
while True:
   mesafe()
   utime.sleep(1)                       # Her 1 sn. aralıklarla mesafe ölçülüyor.
   lcd.clear()