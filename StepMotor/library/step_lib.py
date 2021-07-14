# 28byj-48 Step Motor Kütüphanesidir#
# Bu kütüphane dosyasını açtıktan sonra, farklı kaydet diyerek Pico'nun içine "step_lib.py" isminde kaydedin.
# Parametreler pozitif tam sayı olarak girilmelidir.
# İlk parametre tur sayısı(varsayılan=1) , 2. parametre tur hızı (1-100 aralığında, varsayılan=100)
# adimSayIleri ve adimSayGeri fonksiyonu İlk parametre adım tur sayısı(varsayılan=64) , 2. parametre tur hızı (1-100 aralığında, varsayılan=100)

# # # # Bu kütüphane Ankara Kanuni MTAL - Atölye Ankara Ekibi Öğretmenleri tarafından yazılmıştır. # # # #
# # # # https://atolyeankara.com/ # # # #

from machine import Pin
import utime

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

def convert(x, in_min, in_max, out_min, out_max):    # Girilen hızı yüzdesel olarak terslemek için kullanılacak.
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
 
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

def yarimTurIleri(turSayisi=1, hiz=100):
    if turSayisi<=0 or isinstance(turSayisi, int)==False or isinstance(hiz, int)==False or hiz<=0 or hiz>100:   # Girilen parametrelerin doğruluğu kontrol ediliyor.
        print("yarimTurIleri Fonksiyonu İçin Geçersiz Parametre")
        return
    hiz= convert(hiz, 1, 100, 100, 1)       # Bekleme süresi tersleniyor, böylece hız arttırılıyor.

    for t in range(turSayisi):
        for z in range(256):
            for i in range(8):
                for j in range(4):
                    Pinler[j].value(Adimlar[i][j])
                utime.sleep_ms(hiz)
        
def yarimTurGeri(turSayisi=1, hiz=100):
    if turSayisi<=0 or isinstance(turSayisi, int)==False or isinstance(hiz, int)==False or hiz<=0 or hiz>100:   # Girilen parametrelerin doğruluğu kontrol ediliyor.
        print("yarimTurGeri Fonksiyonu İçin Geçersiz Parametre")
        return
    hiz= convert(hiz, 1, 100, 100, 1)       # Bekleme süresi tersleniyor, böylece hız arttırılıyor.

    for t in range(turSayisi):
        for z in range(256):
            for i in range(7,-1,-1):
                for j in range(4):
                    Pinler[j].value(Adimlar[i][j])
                utime.sleep_ms(hiz)
        
def ceyrekTurIleri(turSayisi=1, hiz=100):
    if turSayisi<=0 or isinstance(turSayisi, int)==False or isinstance(hiz, int)==False or hiz<=0 or hiz>100:   # Girilen parametrelerin doğruluğu kontrol ediliyor.
        print("ceyrekTurIleri Fonksiyonu İçin Geçersiz Parametre")
        return
    hiz= convert(hiz, 1, 100, 100, 1)       # Bekleme süresi tersleniyor, böylece hız arttırılıyor.

    for t in range(turSayisi):
        for z in range(128):
            for i in range(8):
                for j in range(4):
                    Pinler[j].value(Adimlar[i][j])
                utime.sleep_ms(hiz)
        
def ceyrekTurGeri(turSayisi=1, hiz=100):
    if turSayisi<=0 or isinstance(turSayisi, int)==False or isinstance(hiz, int)==False or hiz<=0 or hiz>100:   # Girilen parametrelerin doğruluğu kontrol ediliyor.
        print("ceyrekTurGeri Fonksiyonu İçin Geçersiz Parametre")
        return
    hiz= convert(hiz, 1, 100, 100, 1)       # Bekleme süresi tersleniyor, böylece hız arttırılıyor.

    for t in range(turSayisi):
        for z in range(128):
            for i in range(7,-1,-1):
                for j in range(4):
                    Pinler[j].value(Adimlar[i][j])
                utime.sleep_ms(hiz)
                
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
                
    
    
# tamTurIleri(1,90)
# tamTurGeri(1,100)
# yarimTurIleri(1,100)
# yarimTurGeri(1,100)
# ceyrekTurIleri(1,100)
# ceyrekTurGeri(1,100)

    
