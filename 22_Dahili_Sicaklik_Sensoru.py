#Onboard Sıcaklık#                    #// 4 numaralı analog pine bağlı olan dahili sıcaklık sensörünün kullanımını gösteren uygulama //#
from machine import ADC, Pin, I2C
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

sicaklik_Pini = ADC(4)              # RP2040 mikrokontrolcüsünün dahili sıcaklık sensörü analog GP4 pinidir.
donusturme_carpani = 3.3 / (65535)

while True:
    okunan = sicaklik_Pini.read_u16() * donusturme_carpani
    sicaklik_Degeri = 27 - (okunan - 0.706)/0.001721
    # Buradaki formül RP2040 mikrokontrolcüsünün dahili sıcaklık sensörünün hesaplama formülüdür.
    print(sicaklik_Degeri)
    
    lcd.move_to(4, 0)                   # Sıcaklık değerini LCD I2C ekranda yazdıralım.
    lcd.putstr("Sicaklik")
    lcd.move_to(4, 1)
    lcd.putstr(str(sicaklik_Degeri))   # LCD ekranda göstermek için float değeri stringe çeviren str() fonksiyonunu kullandık.
    
    utime.sleep(2)
    lcd.clear()

