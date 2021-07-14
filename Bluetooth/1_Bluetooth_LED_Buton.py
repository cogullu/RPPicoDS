# Bluetooth Uygulaması #                     #// Bluetooth ile Pico bağlantısı uygulamasıdır.//#
# Bluetooth çalıştırmak için Bluetooth jumperın takılı olduğundan emin olun.

#Bluetooth kullanmak için önce mobil cihazınız ile DeneySeti üzerindeki HC-05 bluetooth modülünü eşleştirmeniz gerekir.
#// daha sonra ise mobil cihazınıza DeneySetini ve Picoyu kontrol edebilecek bir uygulama kurmanız gerekir.
#// Bunun için PlayStore mağazasındaki "Bluetooth Electronics" (keuwlsoft) uygulamasını kullanabilirsiniz.
#// Uygulamadan kendiniz arayüz tasarlayabileceğiniz gibi, hazır arayüzü indirmek için de uygulamadan "Load From Web Link" bağlantısını kullanabilirsiniz.
#// Hazır arayüz linki "https://raw.githubusercontent.com/cogullu/RPPicoDS/main/RPPicoDS_Bluetooth.kwl?token=APP4NV3A7USEOAW3TGE53FTA4IEGC"

from machine import Pin, UART
import utime

uart = UART(0, 9600)           # 0 numaralı UART protokolü üzerinde 9600 hızında veri iletişimi

led_k = Pin(2, Pin.OUT)        # Bluetooth üzerinden kontrol edilecek olan ledin bağlı olduğu pin
led_s = Pin(3, Pin.OUT)        # Bluetooth üzerinden kontrol edilecek olan ledin bağlı olduğu pin
led_y = Pin(4, Pin.OUT)        # Bluetooth üzerinden kontrol edilecek olan ledin bağlı olduğu pin

led_k.value(0)
led_s.value(0)
led_y.value(0)

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
buton_2 = Pin(6, Pin.IN, Pin.PULL_DOWN)
buton_3 = Pin(7, Pin.IN, Pin.PULL_DOWN)


while True:
    try:                              # Olası hata durumlarında uygulamanın çökmemesi için.

        if uart.any() > 0:            # Bluetooth ile Picoya bağlı cihazdan herhangi bir veri gelirse
            data = uart.readline()    # Gelen 1 satırlık veriyi data isimli değişkene kaydet, uygulamadan veri okunuyor...

# # # # # # --------------------------------------------K-Y-S LED'ler-------------------------------------------------------------

            if 'K' in data:                  # Gelen veride K karakteri varsa, 
                uart.write("*rR255G0B0*")    # Arayüzdeki Kırmızı LEDi Yak/Söndür, uygulamaya veri gönderiliyor.
                led_k.toggle()
                utime.sleep(0.1)
                
            if 'Y' in data:                  # Gelen veride Y karakteri varsa, 
                uart.write("*gR0G255B0*")    # Arayüzdeki Yeşil LEDi Yak/Söndür, uygulamaya veri gönderiliyor.
                led_y.toggle()
                utime.sleep(0.1)
                
            if 'S' in data:                  # Gelen veride S karakteri varsa, 
                uart.write("*yR255G255B0*")  # Arayüzdeki Sarı LEDi Yak/Söndür, uygulamaya veri gönderiliyor.
                led_s.toggle()
                utime.sleep(0.1)

            
# # # # # # ---------------------------------------3 Buton Kontrol-----------------------------------------------------------------             
        if buton_1.value() == 1:
            print("Buton 1 OK!")
            uart.write("Buton 1 OK! \n")     # Uygulama arayüzündeki seri ekranda yazı yazdırılıyor.
            utime.sleep(0.3)
                
        if buton_2.value() == 1:                    
            print("Buton 2 OK!")
            uart.write("Buton 2 OK! \n")
            utime.sleep(0.3)
                
        if buton_3.value() == 1:                   
            print("Buton 3 OK!")
            uart.write("Buton 3 OK! \n")
            utime.sleep(0.3)

    except:
        print("Hay Aksi Birşeyler Yanlış Gitti!")
        

