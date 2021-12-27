#Kara Şimşek LED#                     #// LED leri karaşimşek animasyonu ile sırayla yakma //#

from machine import Pin                                                                        
import utime

led_k = Pin(2, Pin.OUT)   # Kırmızı LED
led_s = Pin(3, Pin.OUT)   # Sarı LED
led_y = Pin(4, Pin.OUT)   # Yeşil LED

RGB_blue = Pin(16, Pin.OUT)    # RGB Mavi LED
RGB_green = Pin(17, Pin.OUT)   # RGB Yeşil LED
RGB_red = Pin(18, Pin.OUT)     # RGB Kırmızı LED



led_k.value(0)                    #Tüm ışıkları söndürdük
led_s.value(0)                    
led_y.value(0)                   
RGB_red.value(0)              
RGB_green.value(0)
RGB_blue.value(0)

LED_time = 0.12    # LED ler arası animasyon zamanı
#LED_tepkiZamani = 0.05   # LED lerin tepki süresi için kullanılabilir.

while True:        
    
    led_k.value(1)
    utime.sleep(LED_time)
    led_k.value(0)
    #utime.sleep(LED_tepkiZamani)
    
    led_s.value(1)
    utime.sleep(LED_time)
    led_s.value(0)
    #utime.sleep(LED_tepkiZamani)
    
    led_y.value(1)
    utime.sleep(LED_time)
    led_y.value(0)
    #utime.sleep(LED_tepkiZamani)
    
    RGB_red.value(1)
    utime.sleep(LED_time)
    RGB_red.value(0)
    #utime.sleep(LED_tepkiZamani)
    
    RGB_green.value(1)
    utime.sleep(LED_time)
    RGB_green.value(0)
    #utime.sleep(LED_tepkiZamani)
    
    RGB_blue.value(1)
    utime.sleep(LED_time)
    RGB_blue.value(0)
    #utime.sleep(LED_tepkiZamani)
    utime.sleep(LED_time)
   
    RGB_green.value(1)
    utime.sleep(LED_time)
    RGB_green.value(0)
    #utime.sleep(LED_tepkiZamani)
   
    RGB_red.value(1)
    utime.sleep(LED_time)
    RGB_red.value(0)
    #utime.sleep(LED_tepkiZamani)
   
    led_y.value(1)
    utime.sleep(LED_time)
    led_y.value(0)
    #utime.sleep(LED_tepkiZamani)
   
    led_s.value(1)
    utime.sleep(LED_time)
    led_s.value(0)
    #utime.sleep(LED_tepkiZamani)
    utime.sleep(LED_time)

    

    


                                         
