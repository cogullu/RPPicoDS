#Hırsız Alarmı#                     #// PIR Sensörü ile LED ve Sesle Uyarı Veren Hırsız Alarmı Uygulamasıdır. //#

from machine import Pin,PWM                                                                        
import utime

led_k = Pin(2, Pin.OUT)   # Alarm Işığı
PIR = Pin(19, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(10))
buzzer.freq(2000);
buzzer.duty_u16(0)

led_k.value(0)
buzzer.duty_u16(0)
   

while True:           
    if PIR.value()==1:                         # PIR Sensörü True(1) olduğunda, yani hareket algıladığında
        print("Bir Cisim Algılandı... :D")
        for j in range(100):
            buzzer.duty_u16(40000)
            led_k.toggle()
            utime.sleep_ms(70)                 # milisaniye cinsinden bekleme süresi
            buzzer.duty_u16(0)
        
    led_k.value(0)
    buzzer.duty_u16(0)
    print("Alarm Çalışmıyor...")
    
    utime.sleep(0.5)                     # Her yarım saniyede kontrol eder.
        
     

    

    


                                         
