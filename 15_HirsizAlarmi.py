#Hırsız Alarmı#                     #// PIR Sensörü ile LED ve Sesle Uyarı Veren Hırsız Alarmı Uygulamasıdır. //#

from machine import Pin                                                                        
import utime

led_k = Pin(2, Pin.OUT)   # Alarm Işığı
buzzer = Pin(10, Pin.OUT) # Alarm sireni
PIR = Pin(19, Pin.IN, Pin.PULL_DOWN)

led_k.value(0)
buzzer.value(0) 
   

while True:           
    if PIR.value()==1:                         # PIR Sensörü True(1) olduğunda, yani hareket algıladığında
        print("Bir Cisim Algılandı... :D")
        for j in range(100):
            buzzer.toggle()
            led_k.toggle()
            utime.sleep_ms(70)                 # milisaniye cinsinden bekleme süresi
        
    led_k.value(0)
    buzzer.value(0)
    print("Alarm Çalışmıyor...")
    
    utime.sleep(0.5)                     # Her yarım saniyede kontrol eder.
        
     

    

    


                                         
