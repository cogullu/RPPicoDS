# Bluetooth Uygulaması #                     #// Bluetooth ile Pico bağlantısı uygulamasıdır.//#
# Bluetooth çalıştırmak için Bluetooth jumperın takılı olduğundan emin olun.

#Bluetooth kullanmak için önce mobil cihazınız ile DeneySeti üzerindeki HC-05 bluetooth modülünü eşleştirmeniz gerekir.
#// daha sonra ise mobil cihazınıza DeneySetini ve Picoyu kontrol edebilecek bir uygulama kurmanız gerekir.
#// Bunun için PlayStore mağazasındaki "Bluetooth Electronics" (keuwlsoft) uygulamasını kullanabilirsiniz.
#// Uygulamadan kendiniz arayüz tasarlayabileceğiniz gibi, hazır arayüzü indirmek için de uygulamadan "Load From Web Link" bağlantısını kullanabilirsiniz.
#// Hazır arayüz linki "https://raw.githubusercontent.com/cogullu/RPPicoDS/main/RPPicoDS_Bluetooth.kwl?token=APP4NV3A7USEOAW3TGE53FTA4IEGC"
# Bu uygulamada slider bir adım ile 2 tur arasında değişir.

from machine import Pin, UART, PWM, ADC
import utime

uart = UART(0, 9600)           # 0 numaralı UART protokolü üzerinde 9600 hızında veri iletişimi

pot = ADC(27)

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
buton_2 = Pin(6, Pin.IN, Pin.PULL_DOWN)


def convert(x, in_min, in_max, out_min, out_max):    # Analog giriş değerini yüzdesel orantılamak için
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


   
#--------------------------------------Step Motorlar----------------------------------------#   
in_1 = Pin(11, Pin.OUT)
in_2 = Pin(12, Pin.OUT)
in_3 = Pin(13, Pin.OUT)
in_4 = Pin(14, Pin.OUT)

Pinler = [in_1, in_2, in_3, in_4]

Adimlar =[
  [1,0,0,0],
  [1,1,0,0], 
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
  ]

def adimSayIleri(adimSayisi=64, hiz=100):  # Step motor adım sayısına göre 512 birim hassas döndürme, adimSayisi 1-512 aralığında olmalıdır.
    if adimSayisi<=0 or isinstance(adimSayisi, int)==False or isinstance(hiz, int)==False  or hiz<=0 or hiz>100:   # Girilen parametrelerin doğruluğu kontrol ediliyor.
        print("tamTurIleri Fonksiyonu İçin Geçersiz Parametre")
        return
    hiz= convert(hiz, 1, 100, 100, 1)       # Bekleme süresi tersleniyor, böylece hız arttırılıyor.

    for z in range(adimSayisi):
        for i in range(8):
            for j in range(4):
                Pinler[j].value(Adimlar[i][j])
            utime.sleep_ms(hiz)
            
def adimSayGeri(adimSayisi=64, hiz=100):  # Step motor adım sayısına göre 512 birim hassas döndürme, adimSayisi 1-512 aralığında olmalıdır.
    if adimSayisi<=0 or isinstance(adimSayisi, int)==False or isinstance(hiz, int)==False  or hiz<=0 or hiz>100:   # Girilen parametrelerin doğruluğu kontrol ediliyor.
        print("tamTurIleri Fonksiyonu İçin Geçersiz Parametre")
        return
    hiz= convert(hiz, 1, 100, 100, 1)       # Bekleme süresi tersleniyor, böylece hız arttırılıyor.

    for z in range(adimSayisi):
        for i in range(7,-1,-1):
            for j in range(4):
                Pinler[j].value(Adimlar[i][j])
            utime.sleep_ms(hiz)
#------------------------------------------------------------------------------------#

Rdeger1 = 64

while True:
    try:
# # # # # # ---------------------------------------Potansiyometre Kontrol----------------------------------------------------------------- 
        potdeger= convert(pot.read_u16(), 0, 65535, 0, 100)
        potdeger1="*D"+str(potdeger)+"*"
        uart.write(potdeger1)
        print("pot=", potdeger)
        potdeger2 = "*P" +  str(potdeger) + "*"               # uygulama arayüzündeki pot değeri gösteren Text için uygun formata çevriliyor
        uart.write(potdeger2)                                 # uygulamaya gönderiliyor.

        if uart.any() > 0:            # Bluetooth ile Picoya bağlı cihazdan herhangi bir veri gelirse
            data = uart.readline()    # Gelen 1 satırlık veriyi data isimli değişkene kaydet
            
            if 'A' in data:           # Gelen veride A karakteri varsa
                gecici = str(data)    # Gelen veriyi stringe çevir
                for i in range(len(gecici)-4,0,-1):  # R'den sonra gelen 2 karakteri almak için sondan 4. karakterden başa doğru R'yi ara
                    if gecici[i] == "A":
                        Rdeger= gecici[i+1]+gecici[i+2]   #R karakterinden sonraki 2 değeri deger değişkenine aktar
                        print("Adım Sayısı=", Rdeger)
                        Rdeger1 = convert(int(Rdeger), 10, 99, 64, 1024)
                        break

# # # # # # ---------------------------------------Step Motorlar----------------------------------------------------------------- 
            if 'F' in data:
                adimSayIleri(Rdeger1,potdeger)
            if 'V' in data:
                adimSayGeri(Rdeger1,potdeger)
            if 'I' in data:
                adimSayIleri(512,100)
            if 'G' in data:
                adimSayGeri(512,100)
            
             
# # # # # # --------------------------------------- Butonla Kontrol-----------------------------------------------------------------             
        if buton_1.value() == 1:
            adimSayIleri(512,100)
            print("Buton 1 OK!")
            uart.write("Buton 1 OK! \n")
            utime.sleep(1)
                
        if buton_2.value() == 1:
            adimSayGeri(512,100)
            print("Buton 2 OK!")
            uart.write("Buton 2 OK! \n")
            utime.sleep(1)

    except:
        print("Hay Aksi Birşeyler Yanlış Gitti!")
        

