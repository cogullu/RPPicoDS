# Bluetooth Uygulaması #                     #// Bluetooth ile Pico bağlantısı uygulamasıdır.//#
# Bluetooth çalıştırmak için Bluetooth jumperın takılı olduğundan emin olun.

#Bluetooth kullanmak için önce mobil cihazınız ile DeneySeti üzerindeki HC-05 bluetooth modülünü eşleştirmeniz gerekir.
#// daha sonra ise mobil cihazınıza DeneySetini ve Picoyu kontrol edebilecek bir uygulama kurmanız gerekir.
#// Bunun için PlayStore mağazasındaki "Bluetooth Electronics" (keuwlsoft) uygulamasını kullanabilirsiniz.
#// Uygulamadan kendiniz arayüz tasarlayabileceğiniz gibi, hazır arayüzü indirmek için de uygulamadan "Load From Web Link" bağlantısını kullanabilirsiniz.
#// Hazır arayüz linki "https://raw.githubusercontent.com/cogullu/RPPicoDS/main/RPPicoDS_Bluetooth.kwl?token=APP4NV3A7USEOAW3TGE53FTA4IEGC"

from machine import Pin, UART, PWM, ADC
import utime

uart = UART(0, 9600)           # 0 numaralı UART protokolü üzerinde 9600 hızında veri iletişimi

led_k = Pin(2, Pin.OUT)        # Bluetooth üzerinden kontrol edilecek olan ledin bağlı olduğu pin
led_s = Pin(3, Pin.OUT)        # Bluetooth üzerinden kontrol edilecek olan ledin bağlı olduğu pin
led_y = Pin(4, Pin.OUT)        # Bluetooth üzerinden kontrol edilecek olan ledin bağlı olduğu pin

buzzer = Pin(10, Pin.OUT)      # Buzzer Pin
pot = ADC(27)
potdeger=0
potdeger1="0"

RGB_blue = PWM(Pin(16))    # RGB Mavi LED
RGB_red = PWM(Pin(17))     # RGB Kırmızı LED
RGB_green = PWM(Pin(18))   # RGB Yeşil LED
RGB_red.freq(1000)
RGB_green.freq(1000)
RGB_blue.freq(1000) 

Rdeger, Gdeger, Bdeger ="0","0","0"
Rdeger1, Gdeger1, Bdeger1 = 0, 0, 0
Rdeger2, Gdeger2, Bdeger2 = 0, 0, 0

led_k.value(0)
led_s.value(0)
led_y.value(0)

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)
buton_2 = Pin(6, Pin.IN, Pin.PULL_DOWN)
buton_3 = Pin(7, Pin.IN, Pin.PULL_DOWN)

PIR = Pin(19, Pin.IN, Pin.PULL_DOWN)
ldr = ADC(26)
sicaklik_Pini = ADC(4)              
donusturme_carpani = 3.3 / (65535)


def convert(x, in_min, in_max, out_min, out_max):    # Analog giriş değerini yüzdesel orantılamak için
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


trigger = Pin(8, Pin.OUT)               # Sinyal gönderen pindir.
echo = Pin(9, Pin.IN)                   # Gönderilen sinyali okuyan pindir.

#----------------------------------Buton 3'e basıldığında mesafeyi ölçen fonksiyon------------------------------------------#
def mesafe():                           # Mesafeyi hesaplayan fonksiyon.
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
   uart.write(uzaklik1)
#------------------------------------------------------------------------------------#
   
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

def tamTurIleri(turSayisi=1, hiz=100):              # tur sayısı kadar saat yönünde ileri tam tur atar.
    if turSayisi<=0 or isinstance(turSayisi, int)==False or isinstance(hiz, int)==False  or hiz<=0 or hiz>100:   # Girilen parametrelerin doğruluğu kontrol ediliyor.
        print("tamTurIleri Fonksiyonu İçin Geçersiz Parametre")
        return
    hiz= convert(hiz, 1, 100, 100, 1)       # Bekleme süresi tersleniyor, böylece hız arttırılıyor.
    
    for t in range(turSayisi):
        for z in range(512):
            for i in range(8):
                for j in range(4):
                    Pinler[j].value(Adimlar[i][j])
                utime.sleep_ms(hiz)
        
def tamTurGeri(turSayisi=1, hiz=100):       # tur sayısı kadar saat yönünde geri tam tur atar.
    if turSayisi<=0 or isinstance(turSayisi, int)==False or isinstance(hiz, int)==False or hiz<=0 or hiz>100:   # Girilen parametrelerin doğruluğu kontrol ediliyor.
        print("tamTurGeri Fonksiyonu İçin Geçersiz Parametre")
        return
    hiz= convert(hiz, 1, 100, 100, 1)       # Bekleme süresi tersleniyor, böylece hız arttırılıyor.

    for t in range(turSayisi):
        for z in range(512):
            for i in range(7,-1,-1):
                for j in range(4):
                    Pinler[j].value(Adimlar[i][j])
                utime.sleep_ms(hiz)
#------------------------------------------------------------------------------------#



while True:
    try:

        if uart.any() > 0:            # Bluetooth ile Picoya bağlı cihazdan herhangi bir veri gelirse
            data = uart.readline()    # Gelen 1 satırlık veriyi data isimli değişkene kaydet
            
# # # # # # ---------------------------------------Reset Butonu-----------------------------------------------------------------   
            if 'Q' in data:           # Gelen veride Q karakteri varsa, Reset Butonu
                buzzer.value(1)
                uart.write("*S*")     # Buzzer
                
                uart.write("*rR0G0B0*")  # uygulamdaki kırmızı ledi söndür
                led_k.value(0)
                uart.write("*gR0G0B0*")  # uygulamdaki yeşil ledi söndür
                led_s.value(0)
                uart.write("*yR0G0B0*")  # uygulamdaki sarı ledi söndür
                led_y.value(0)
                uart.write("*LR0G0B0*")  # uygulamdaki RGB ledi söndür
                RGB_red.duty_u16(0)
                RGB_green.duty_u16(0)
                RGB_blue.duty_u16(0)
                
                utime.sleep(2)
                buzzer.value(0)
 
# # # # # # ---------------------------------------Step Motorlar----------------------------------------------------------------- 
            if 'F' in data:
                tamTurIleri(1,100)
            if 'V' in data:
                tamTurGeri(1,100)
                
                
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

# # # # # # --------------------------------------------K-Y-S LED'ler-------------------------------------------------------------

            if 'K' in data:           # Gelen veride K karakteri varsa, 
                uart.write("*rR255G0B0*")  # Kırmızı Ledi Yak/Söndür
                led_k.toggle()
                if PIR.value():                         # PIR Sensörü Kontrolü
                    uart.write("PIR OK!\n")
                else:
                    uart.write("PIR NOT\n")
                utime.sleep(2)
                
            if 'Y' in data:           # Gelen veride Y karakteri varsa, 
                uart.write("*gR0G255B0*")  # Yeşil Ledi Yak/Söndür
                led_y.toggle()
                ldrDeger =  ldr.read_u16()   # LDR Kontrolü
                ldrDeger1 = "LDR=" + str(ldrDeger)
                uart.write(ldrDeger1)
                utime.sleep(2)
                
            if 'S' in data:           # Gelen veride S karakteri varsa, 
                uart.write("*yR255G255B0*")  # Sarı Ledi Yak/Söndür
                led_s.toggle()
#                 mesafe()                     # HC-SR04 Ultrasonic Kontrolü
                utime.sleep(2)

# # # # # # ---------------------------------------Potansiyometre Kontrol----------------------------------------------------------------- 
            potdeger= convert(pot.read_u16(), 0, 65535, 0, 100)
            potdeger1="*D"+str(potdeger)+"*"
            uart.write(potdeger1)
            print("pot=", potdeger)
            
# # # # # # ---------------------------------------Dahili Sıcaklık Kontrol-----------------------------------------------------------------            
            okunan = sicaklik_Pini.read_u16() * donusturme_carpani
            sicaklik_Degeri = int(27 - (okunan - 0.706)/0.001721)
            sicaklikDegeri1=str(sicaklik_Degeri)
            print("Sıcaklık=", sicaklikDegeri1)
            sicaklikDegeri1="*E" + sicaklikDegeri1 + "*"
            uart.write(sicaklikDegeri1)    
         
            utime.sleep(0.2)
            
# # # # # # ---------------------------------------3 Buton Kontrol-----------------------------------------------------------------             
        if buton_1.value() == 1:
            print("Buton 1 OK!")
            uart.write("Buton 1 OK! \n")
            utime.sleep(1)
                
        if buton_2.value() == 1:                    
            print("Buton 2 OK!")
            uart.write("Buton 2 OK! \n")
            utime.sleep(1)
                
        if buton_3.value() == 1:                   
            print("Buton 3 OK!")
            uart.write("Buton 3 OK! \n")
            utime.sleep(1)

    except:
        print("Hay Aksi Birşeyler Yanlış Gitti!")
        

