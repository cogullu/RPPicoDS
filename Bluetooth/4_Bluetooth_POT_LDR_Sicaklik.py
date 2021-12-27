# Bluetooth Uygulaması #                     #// Bluetooth ile Pico bağlantısı uygulamasıdır.//#
# Bluetooth çalıştırmak için Bluetooth jumperın takılı olduğundan emin olun.

#Bluetooth kullanmak için önce mobil cihazınız ile DeneySeti üzerindeki HC-05 bluetooth modülünü eşleştirmeniz gerekir.
#// daha sonra ise mobil cihazınıza DeneySetini ve Picoyu kontrol edebilecek bir uygulama kurmanız gerekir.
#// Bunun için PlayStore mağazasındaki "Bluetooth Electronics" (keuwlsoft) uygulamasını kullanabilirsiniz.
#// Uygulamadan kendiniz arayüz tasarlayabileceğiniz gibi, hazır arayüzü indirmek için de uygulamadan "Load From Web Link" bağlantısını kullanabilirsiniz.
#// Hazır arayüz linki "https://raw.githubusercontent.com/cogullu/RPPicoDS/main/Bluetooth/RPPicoDS_Bluetooth.kwl?token=APP4NV4UOVXK5GZBO4SWAATA537CI"

from machine import Pin, UART, ADC
import utime

uart = UART(0, 9600)           # 0 numaralı UART protokolü üzerinde 9600 hızında veri iletişimi

pot = ADC(27)
ldr = ADC(26)
sicaklik_Pini = ADC(4)              
donusturme_carpani = 3.3 / (65535)


def convert(x, in_min, in_max, out_min, out_max):    # Analog giriş değerini yüzdesel orantılamak için
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


while True:
    try:
       
# # # # # # ---------------------------------------Potansiyometre Kontrol----------------------------------------------------------------- 
        potdeger= convert(pot.read_u16(), 0, 65535, 0, 100)   # Pot değeri hesaplanıyor.
        potdeger1= "*D"+str(potdeger)+ "*"                    # uygulamaya göndermek için gerekli formata çevriliyor.
        uart.write(potdeger1)                                 # uygulamaya gönderiliyor.
        potdeger2 = "*P" +  str(potdeger) + "*"               # uygulama arayüzündeki pot değeri gösteren Text için uygun formata çevriliyor
        uart.write(potdeger2)                                 # uygulamaya gönderiliyor.
            
# # # # # # ---------------------------------------Dahili Sıcaklık Kontrol-----------------------------------------------------------------            
        okunan = sicaklik_Pini.read_u16() * donusturme_carpani
        sicaklik_Degeri = int(27 - (okunan - 0.706)/0.001721) # Sıcaklık hesaplandı
        sicaklikDegeri1="*E" + str(sicaklik_Degeri) + "*"     # uygulamaya göndermek için gerekli formata çevriliyor. 
        uart.write(sicaklikDegeri1)                           # uygulamaya gönderiliyor.
        
        sicaklikDegeri2="*T" + str(sicaklik_Degeri) + "*"     # uygulama arayüzündeki Sıcaklık değeri gösteren Text için uygun formata çevriliyor
        uart.write(sicaklikDegeri2)                           # uygulamaya gönderiliyor.
                     
# # # # # # ---------------------------------------LDR Kontrol-----------------------------------------------------------------
        ldrDeger =  convert(ldr.read_u16(), 0, 65535, 100, 0) # LDR yüzdesel hesaplanıyor
        ldrDeger1 = convert(ldrDeger, 100, 0, 100, 0)         # LDR aydınlık olarak gösterilmesi için tersleniyor.
        ldrDeger2 = ldrDeger1                                 # Bu değeri daha sonra kullanmak için başka bir değişkende saklıyoruz.
        ldrDeger1 = "*L" + str(ldrDeger1) + "*"               # uygulamaya göndermek için gerekli formata çevriliyor.
        uart.write(ldrDeger1)                                 # uygulamaya gönderiliyor.
        
        ldrDeger2 = "*A" + str(ldrDeger2) + "*"               # uygulama arayüzündeki LDR aydınlık değeri gösteren Text için uygun formata çevriliyor
        uart.write(ldrDeger2)                                 # uygulamaya gönderiliyor.        
        
        print("Pot=", potdeger, end="---")
        print("Sıcaklık=", sicaklik_Degeri, end="---")
        print("LDR=", ldrDeger)
        print("-----------------------------------")
                    
        utime.sleep(0.2)

    except:
        print("Hay Aksi Birşeyler Yanlış Gitti!")
        

