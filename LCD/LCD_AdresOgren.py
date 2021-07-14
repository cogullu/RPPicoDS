from machine import Pin, I2C
sda=Pin(20)                                  # LCD I2C ekranın SDA bağlantı pini
scl=Pin(21)                                  # LCD I2C ekranın SCL bağlantı pini
i2c=I2C(0,sda=sda, scl=scl, freq=200000)     # Hata alırsanız frekansı değiştirin.(100000, 200000, 300000, 400000 vs.)
print(i2c.scan())
# Seri ekranda LCD I2C ekran adresi decimal(ondalık) olarak yazar, bunu hexadecimal(16'lık) sisteme çevirmek gerekiyor.