# Bluetooth Uygulaması #                     #// Bluetooth ile Pico bağlantısı uygulamasıdır.//#
# Bluetooth çalıştırmak için Bluetooth jumperın takılı olduğundan emin olun.

#Bluetooth kullanmak için önce mobil cihazınız ile DeneySeti üzerindeki HC-05 bluetooth modülünü eşleştirmeniz gerekir.
#// daha sonra ise mobil cihazınıza DeneySetini ve Picoyu kontrol edebilecek bir uygulama kurmanız gerekir.
#// Bunun için PlayStore mağazasındaki "Bluetooth Electronics" (keuwlsoft) uygulamasını kullanabilirsiniz.
#// Uygulamadan kendiniz arayüz tasarlayabileceğiniz gibi, hazır arayüzü indirmek için de uygulamadan "Load From Web Link" bağlantısını kullanabilirsiniz.
#// Hazır arayüz linki "https://raw.githubusercontent.com/cogullu/RPPicoDS/main/Bluetooth/RPPicoDS_Bluetooth.kwl?token=APP4NV4UOVXK5GZBO4SWAATA537CI"
# Bu uygulamda 0-150 cm arası uzaklık baz alınmıştır.

from machine import Pin, UART, PWM, ADC
import utime

uart = UART(0, 9600)           # 0 numaralı UART protokolü üzerinde 9600 hızında veri iletişimi

trigger = Pin(8, Pin.OUT)               # Sinyal gönderen pindir.
echo = Pin(9, Pin.IN)                   # Gönderilen sinyali okuyan pindir.

while True:
    try:

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
       uzaklik1="uzaklik=" + str(uzaklik)
       print("Uzaklık= ",uzaklik,"cm")
       uzaklik_Deger= "*U"+str(uzaklik)+ "*" 
       uart.write(uzaklik_Deger)


    except:
        print("Hay Aksi Birşeyler Yanlış Gitti!")
        

