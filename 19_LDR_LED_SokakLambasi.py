#LDR ile LED#                    #// LDR ile LED'in parlaklığını ayarlayan uygulamadır.(Karanlıkta daha fazla aydınlatan sokak lambası) //#
# LDR sensörü 0-65535 aralığında ışık değeri ile ters orantılı olarak çalışır. Yani karanlıkta verdiği değer daha yüksektir.
# Aydınlık değeri için LDR'den okunan değerin terslenmesi gerekir.(convert fonksiyonu ile)
from machine import ADC, PWM, Pin, I2C    
import utime

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

ldr = ADC(26)                  # 26 numaralı Analog girişli pini tanımladık.
led_k = PWM(Pin(2))             # Parlaklık değeri ayarlanacak LED
led_k.freq(1000)                # LED' in 1 sn. deki çalışma frekansını ayarladık.

def convert(x, in_min, in_max, out_min, out_max):    # Analog giriş değerini yüzdesel orantılamak için
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True: 
     print("Okunan LDR Değeri=", ldr.read_u16())
     
     lcd.move_to(0, 0)                   # LDRnin aydınlık değeri LCD I2C ekranda yazdırılıyor...
     lcd.putstr("Aydinlik Yuzdesi")
     lcd.move_to(7, 1)
     lcd.putstr(str(convert(ldr.read_u16(), 2000, 61000, 100, 0)))  # Karanlık değerini aydınlık yüzdesi olarak yazdırmak için tersledik.
     # LCD ekranda göstermek için float değeri stringe çeviren str() fonksiyonunu kullandık.
     # Aydınlık değerini yüzdesel olarak göstermek için convert() fonksiyonunu kullandık.
     
     
     led_k.duty_u16(convert(ldr.read_u16(), 2000, 61000, 1000, 65535)) # Kırmızı LED'in yanma seviyesi değeri ayarlanıyor.
     print("-------------------------")
     utime.sleep(1)
     lcd.clear()