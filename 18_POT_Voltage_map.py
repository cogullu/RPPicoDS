#POT Voltaj,LCD, mapping#                    #// Potansiyometre ile voltajı LCD ekrana yazdıran uygulama //#
# LCD I2C çalıştırmak için LCD Jumperın takılı olduğundan emin olun.
# LcdApi ve I2cLcd kütüphaneleri LCD/Library klasöründe mevcuttur. Bu kütüphaneleri Piconun kök klasörü içine...
#// LcdApi kütüphanesini "lcd_api.py", I2cLcd kütüphanesini "pico_i2c_lcd.py" isminde kaydedin. İsimlerde değişiklik yapmayın!
from machine import ADC, Pin, I2C
import utime

pot = ADC(27)
donusturme_carpani = 3.3 / (65535)        # Analog girişten okunan 65535 değerin her bir baremi için çarpan katsayısı

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


def convert(x, in_min, in_max, out_min, out_max):    # Analog giriş değerini yüzdesel orantılamak için kullanılan fonksiyon
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    voltage = pot.read_u16() * donusturme_carpani
    print("Voltaj=", voltage)
    print("Yüzde= ", convert(pot.read_u16(), 1000, 65535, 0, 100))     # Voltajın yüzdesi seri ekranda yazdırılıyor...
    print("--------------------------")
    
    lcd.move_to(5, 0)                   # Voltajın değeri LCD I2C ekranda yazdırılıyor...
    lcd.putstr("Voltaj")
    lcd.move_to(4, 1)
    lcd.putstr(str(voltage))            # LCD ekranda göstermek için float değeri stringe çeviren str() fonksiyonunu kullandık.
    
    utime.sleep(2)
    lcd.clear()
    
