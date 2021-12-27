#Park Sensörü#                    #// Araçlardaki park sensörünü sesli ve LED ile simüle eden uygulama //#

from machine import Pin, PWM
import utime
trigger = Pin(8, Pin.OUT)               # Sinyal gönderen pindir.
echo = Pin(9, Pin.IN)                   # Gönderilen sinyali okuyan pindir.

buzzer = PWM(Pin(10))
buzzer.freq(2000);
buzzer.duty_u16(0)

led = Pin(2, Pin.OUT)

def mesafe():                            # Mesafeyi hesaplayan fonksiyon.
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
    print("Uzaklık= ",uzaklik,"cm")
   
    if uzaklik <= 15:         # Mesafe 15 cm den az olursa kesintisiz ışık ve sesli uyarı.
        buzzer.duty_u16(40000)
        led.value(1)
    elif uzaklik <= 25:       # Mesafe 25 cm den az olursa çok hızlı ışık ve sesli uyarı.
        buzzer.duty_u16(40000)
        led.value(1)
        utime.sleep(0.1)
        buzzer.duty_u16(0)
        led.value(0)
        utime.sleep(0.1)

    elif uzaklik <= 35:       # Mesafe 35 cm den az olursa hızlı ışık ve sesli uyarı.
        buzzer.duty_u16(40000)
        led.value(1)
        utime.sleep(0.2)
        buzzer.duty_u16(0)
        led.value(0)
        utime.sleep(0.2)
        
    elif uzaklik <= 50:      # Mesafe 50 cm den az olursa normal ışık ve sesli uyarı.
        buzzer.duty_u16(40000)
        led.value(1)
        utime.sleep(0.4)
        buzzer.duty_u16(0)
        led.value(0)
        utime.sleep(0.4)
        
    elif uzaklik <= 80:     # Mesafe 80 cm den az olursa az ışık ve sesli uyarı.
        buzzer.duty_u16(40000)
        led.value(1)
        utime.sleep(0.6)
        buzzer.duty_u16(0)
        led.value(0)
        utime.sleep(0.6)
    
    elif uzaklik <= 120:    # Mesafe 120 cm den az olursa 1sn aralıklarla sadece sesli uyarı.
        led.value(1)
        utime.sleep(1)
        led.value(0)
        utime.sleep(1)
    else:                   # Mesafe 120 cm den çok olursa uyarı verme.
        buzzer.duty_u16(0)
        led.value(0)
   
while True:
    mesafe()