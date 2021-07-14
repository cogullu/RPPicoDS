# Sıcaklık Dosya Kayıt, time#                    #// Dahili sıcaklık sensöründen gelen değerleri dosyaya zaman ile kaydeden uygulamadır. //#
# Raspberry Pico üzerinde RTC olmadığından harici güç ile besleyerek bu programı çalıştırdığınızda tarihleri yanlış kaydedecektir.
# Bilgisayar ile kullanıldığında sorunsuz kullanılır.
from machine import ADC, Pin
import utime

sicaklik_Pini = ADC(4)              # RP2040 mikrokontrolcüsünün dahili sıcaklık sensörü analog GP4 pinidir.
donusturme_carpani = 3.3 / (65535)

olcumAraligi=1                      # Ne kadar sürede(sn) periyodik olarak sıcaklık değerinin dosyaya yazdırılacağı.
 
while True:
    okunan = sicaklik_Pini.read_u16() * donusturme_carpani
    sicaklik_Degeri = 27 - (okunan - 0.706)/0.001721
    
    zaman = utime.gmtime()          # UTC formatında zaman bilgileri zaman değişkenine tuple türünde aktarılıyor.
#     (Yıl, Ay, Gün, Saat, Dakika, Saniye, Haftanın Kaçıncı Günü, Yılın Kaçıncı Günü)
    tarihSaat= str(zaman[2]) + "/" + str(zaman[1]) + "/" + str(zaman[0]) + " - " + str(zaman[3]) + ":" + str(zaman[4]) + "." + str(zaman[5])
    with open("sicaklik.txt", "a+") as dosya:   # Pico'nun içine sicaklik.txt isminde dosya oluşturuluyor ve dosya objesine aktarılıyor. Dosya Pico' nun içine kaydediliyor.
        dosya.write("{0} ----- : {1}°\n".format(tarihSaat, sicaklik_Degeri))   # Tarihle birlikte sıcaklık değeri formatlı bir şekilde dosyaya yazdırılıyor.

    utime.sleep(olcumAraligi)
    