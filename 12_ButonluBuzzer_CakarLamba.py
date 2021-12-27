#Araç ButonBuzzer Çakar Lamba, thread#                     #// Araçlar için butona basıldığında ses çıkararak çakar lambayı durduran uygulama //#
# Butonun anında tepki vermesi için kesme yada multi_thread kullanılmalıdır.

from machine import Pin,PWM                                                                        
import utime

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)

RGB_red = Pin(18, Pin.OUT)     # RGB Kırmızı Işık
RGB_blue = Pin(16, Pin.OUT)    # RGB Mavi Işık

buzzer = PWM(Pin(10))
buzzer.freq(2000);
buzzer.duty_u16(0)
                 
RGB_red.value(0)              
RGB_blue.value(0)

LED_time = 0.09               # LED animasyon hızı
LED_count = 5                 # LED yanıp, sönme sayısı

while True:
    
    if buton_1.value() == 1:
        print("Çakar Durduruldu")
        buzzer.duty_u16(40000)
    else:
        buzzer.duty_u16(0)
        
        for i in range(LED_count):
            RGB_red.value(1)         # Kırmızı LED
            utime.sleep(LED_time)
            RGB_red.value(0)
            utime.sleep(LED_time)
        
        for i in range(LED_count):   
            RGB_blue.value(1)        # Mavi LED
            utime.sleep(LED_time)
            RGB_blue.value(0)
            utime.sleep(LED_time)
        
    
    

    
    
    

    


                                         
