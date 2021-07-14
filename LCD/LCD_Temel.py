# LCD I2C çalıştırmak için LCD Jumperın takılı olduğundan emin olun.
# LcdApi ve I2cLcd kütüphaneleri LCD/Library klasöründe mevcuttur. Bu kütüphaneleri Piconun kök klasörü içine...
#// LcdApi kütüphanesini "lcd_api.py", I2cLcd kütüphanesini "pico_i2c_lcd.py" isminde kaydedin. İsimlerde değişiklik yapmayın!

#LCD I2C ekran kullanımını anlatan uygulamadır.

import utime

#import machine
from machine import I2C, Pin
from lcd_api import LcdApi          # LCD komutlarını çalıştıran kütüphane
from pico_i2c_lcd import I2cLcd     # LCD komutlarını çalıştıran kütüphane

I2C_ADDR     = 0x27                 # LCD I2C ekran adresi, farklı olabilir, datasheet bakmak gerekir
I2C_NUM_ROWS = 2                    # LCD I2C ekran satır sayısı
I2C_NUM_COLS = 16                   # LCD I2C ekran sütun sayısı

sda=Pin(20)                         # LCD I2C ekranın SDA bağlantı pini
scl=Pin(21)                         # LCD I2C ekranın SCL bağlantı pini

i2c = I2C(0, sda=sda, scl=scl, freq=200000)              # Hata alırsanız frekansı değiştirin.(100000, 200000, 300000, 400000 vs.)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("Test...")                   # LCD ekranda yazı yazdırma, Türkçe karakterler görünmeyecektir
utime.sleep(5)                          # Yazı ekranda 5 sn görünecek
lcd.move_to(5, 1)                       # İmleci istenilen konuma taşır. (Sütun, Satır)
utime.sleep(2)
lcd.show_cursor()                       # İmleci gösterir
utime.sleep(2)
lcd.hide_cursor()                       # İmleci kapatır
utime.sleep(2)
lcd.blink_cursor_on()                   # İmleç yanıp söner
utime.sleep(2)
lcd.blink_cursor_off()                  # İmleç yanıp sönmesi durur
utime.sleep(2)
lcd.backlight_off()                     # LCD ekran arka ışığı kapatır
utime.sleep(2)
lcd.backlight_on()                      # LCD ekran arka ışığı açar
utime.sleep(2)
lcd.display_off()                       # LCD ekran komutlarını kapatır,  tekrar on yapana kadar
utime.sleep(2)
lcd.display_on()                        # LCD ekranı komutlara cevap verecek şekilde açar
utime.sleep(2)
lcd.clear()                             # LCD ekranı temizler ve imleci sol üste götürür


# LCD ekranda özel karakterler göstermek için,
# https://maxpromer.github.io/LCD-Character-Creator/
# sitesinden I2C ve Hex seçilip karakterler oluşturulur, sonra elde edilen değerler aşağıdaki şekilde LCD ekrana aktarılır.

lcd.custom_char(0, bytearray([ 0x03,
  0x04,
  0x0A,
  0x10,
  0x14,
  0x0B,
  0x04,
  0x03]))

lcd.custom_char(1, bytearray([ 0x18,   # Baştaki numara her karakterde 1 artar
  0x04,
  0x0A,
  0x01,
  0x05,
  0x1A,
  0x04,
  0x18]))

lcd.move_to(0, 0)
lcd.putchar(chr(0))                    # LCD ekranda özel karakter gösterme komutu
lcd.move_to(1, 0)
lcd.putchar(chr(1))


