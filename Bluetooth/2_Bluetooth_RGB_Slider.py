# Bluetooth Uygulaması #                     #// Bluetooth ile Pico bağlantısı uygulamasıdır.//#
# Bluetooth çalıştırmak için Bluetooth jumperın takılı olduğundan emin olun.

#Bluetooth kullanmak için önce mobil cihazınız ile DeneySeti üzerindeki HC-05 bluetooth modülünü eşleştirmeniz gerekir.
#// daha sonra ise mobil cihazınıza DeneySetini ve Picoyu kontrol edebilecek bir uygulama kurmanız gerekir.
#// Bunun için PlayStore mağazasındaki "Bluetooth Electronics" (keuwlsoft) uygulamasını kullanabilirsiniz.
#// Uygulamadan kendiniz arayüz tasarlayabileceğiniz gibi, hazır arayüzü indirmek için de uygulamadan "Load From Web Link" bağlantısını kullanabilirsiniz.
#// Hazır arayüz linki "https://raw.githubusercontent.com/cogullu/RPPicoDS/main/Bluetooth/RPPicoDS_Bluetooth.kwl?token=APP4NV4UOVXK5GZBO4SWAATA537CI"

from machine import Pin, UART, PWM, ADC
import utime

uart = UART(0, 9600)           # 0 numaralı UART protokolü üzerinde 9600 hızında veri iletişimi

RGB_blue = PWM(Pin(16))    # RGB Mavi LED
RGB_red = PWM(Pin(17))     # RGB Kırmızı LED
RGB_green = PWM(Pin(18))   # RGB Yeşil LED
RGB_red.freq(1000)
RGB_green.freq(1000)
RGB_blue.freq(1000) 

Rdeger, Gdeger, Bdeger ="0","0","0"
Rdeger1, Gdeger1, Bdeger1 = 0, 0, 0
Rdeger2, Gdeger2, Bdeger2 = 0, 0, 0

def convert(x, in_min, in_max, out_min, out_max):    # Analog giriş değerini yüzdesel orantılamak için
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    try:

        if uart.any() > 0:            # Bluetooth ile Picoya bağlı cihazdan herhangi bir veri gelirse
            data = uart.read()        # Gelen tüm veriyi data isimli değişkene kaydet
                        
# # # # # # ---------------------------------------RGB LED'ler-----------------------------------------------------------------         
            if 'R' in data:           # Gelen veride R karakteri varsa
                gecici = str(data)    # Gelen veriyi stringe çevir
                for i in range(len(gecici)-4,0,-1):  # R'den sonra gelen 2 karakteri almak için sondan 4. karakterden başa doğru R'yi ara
                    if gecici[i] == "R":
                        Rdeger= gecici[i+1]+gecici[i+2]   #R karakterinden sonraki 2 değeri deger değişkenine aktar
                        print("RGB Kırmızı Değeri=", Rdeger)
                        Rdeger1 = convert(int(Rdeger), 10, 99, 0, 65530)
                        RGB_red.duty_u16(Rdeger1)
                        Rdeger2 = convert(int(Rdeger), 10, 99, 0, 255)
                        RGBDeger= "*LR" + str(Rdeger2) + "G" + str(Gdeger2) + "B" + str(Bdeger2) + "*"
                        uart.write(RGBDeger)
                        break
                    
            if 'G' in data:           # Gelen veride G karakteri varsa
                gecici = str(data)    # Gelen veriyi stringe çevir
                for i in range(len(gecici)-4,0,-1):  # G'den sonra gelen 2 karakteri almak için sondan 4. karakterden başa doğru G'yi ara
                    if gecici[i] == "G":
                        Gdeger= gecici[i+1]+gecici[i+2]   #G karakterinden sonraki 2 değeri deger değişkenine aktar
                        print("RGB Yeşil Değeri=", Gdeger)
                        Gdeger1 = convert(int(Gdeger), 10, 99, 0, 65530)
                        RGB_green.duty_u16(Gdeger1)
                        Gdeger2 = convert(int(Gdeger), 10, 99, 0, 255)
                        RGBDeger= "*LR" + str(Rdeger2) + "G" + str(Gdeger2) + "B" + str(Bdeger2) + "*"
                        uart.write(RGBDeger)
                        break
            if 'B' in data:           # Gelen veride B karakteri varsa
                gecici = str(data)    # Gelen veriyi stringe çevir
                for i in range(len(gecici)-4,0,-1):  # B'den sonra gelen 2 karakteri almak için sondan 4. karakterden başa doğru B'yi ara
                    if gecici[i] == "B":
                        Bdeger= gecici[i+1]+gecici[i+2]   #B karakterinden sonraki 2 değeri deger değişkenine aktar
                        print("RGB Mavi Değeri=", Bdeger)
                        Bdeger1 = convert(int(Bdeger), 10, 99, 0, 65530)
                        RGB_blue.duty_u16(Bdeger1)
                        Bdeger2 = convert(int(Bdeger), 10, 99, 0, 255)
                        RGBDeger= "*LR" + str(Rdeger2) + "G" + str(Gdeger2) + "B" + str(Bdeger2) + "*"
                        uart.write(RGBDeger)
                        break

    except:
        print("Hay Aksi Birşeyler Yanlış Gitti!")
        

