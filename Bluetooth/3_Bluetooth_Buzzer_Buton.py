# Bluetooth Uygulaması #                     #// Bluetooth ile Pico bağlantısı uygulamasıdır.//#
# Bluetooth çalıştırmak için Bluetooth jumperın takılı olduğundan emin olun.

#Bluetooth kullanmak için önce mobil cihazınız ile DeneySeti üzerindeki HC-05 bluetooth modülünü eşleştirmeniz gerekir.
#// daha sonra ise mobil cihazınıza DeneySetini ve Picoyu kontrol edebilecek bir uygulama kurmanız gerekir.
#// Bunun için PlayStore mağazasındaki "Bluetooth Electronics" (keuwlsoft) uygulamasını kullanabilirsiniz.
#// Uygulamadan kendiniz arayüz tasarlayabileceğiniz gibi, hazır arayüzü indirmek için de uygulamadan "Load From Web Link" bağlantısını kullanabilirsiniz.
#// Hazır arayüz linki "https://raw.githubusercontent.com/cogullu/RPPicoDS/main/Bluetooth/RPPicoDS_Bluetooth.kwl?token=APP4NV4UOVXK5GZBO4SWAATA537CI"

from machine import Pin, UART, PWM
import utime

uart = UART(0, 9600)           # 0 numaralı UART protokolü üzerinde 9600 hızında veri iletişimi

buzzer = PWM(Pin(10))          # Buzzer Pin
buzzer.freq(2000);
buzzer.duty_u16(0)

while True:
    try:

        if uart.any() > 0:            # Bluetooth ile Picoya bağlı cihazdan herhangi bir veri gelirse
            data = uart.readline()    # Gelen 1 satırlık veriyi data isimli değişkene kaydet
            
# # # # # # ---------------------------------------Reset Butonu-----------------------------------------------------------------   
            if 'Q' in data:           # Gelen veride Q karakteri varsa, "Ses Çal" Butonu
                buzzer.duty_u16(40000)
                uart.write("*S*")     # Buzzer
                
                utime.sleep(2)
                buzzer.duty_u16(0)
    except:
        print("Hay Aksi Birşeyler Yanlış Gitti!")
        

