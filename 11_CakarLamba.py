#Araç Çakar Lamba#                     #// Araçlar için RGB LED çakar lamba uygulamasıdır. //#

from machine import Pin                                                                        
import utime

RGB_red = Pin(18, Pin.OUT)     # RGB Kırmızı Işık
RGB_blue = Pin(16, Pin.OUT)    # RGB Mavi Işık
                 
RGB_red.value(0)              
RGB_blue.value(0)

LED_time = 0.09               # LED animasyon hızı
LED_count = 5                 # LED yanıp, sönme sayısı

while True:
    
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
    

    
    
    

    


                                         
