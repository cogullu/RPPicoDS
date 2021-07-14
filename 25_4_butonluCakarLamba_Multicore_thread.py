#Araç ButonBuzzer Çakar Lamba, thread#                     #// Araçlar için Butonla Ses Çıkaran Çakar Lamba //#


from machine import Pin                                                                        
import utime
import _thread            # _thread kütüphanesi

buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)

RGB_red = Pin(17, Pin.OUT)     # RGB Kırmızı Işık
RGB_blue = Pin(16, Pin.OUT)    # RGB Mavi Işık
buzzer = Pin(10, Pin.OUT)      # Buzzer Pin
                 
RGB_red.value(0)              
RGB_blue.value(0)

LED_time = 0.09               # LED animasyon hızı
LED_count = 5                 # LED yanıp, sönme sayısı


def second_thread():                         # 2. _threadda yapılacak işlemler
    while True:
        if buton_1.value() == 1:
            buzzer.toggle()
            utime.sleep(0.05)
        
_thread.start_new_thread(second_thread, ())

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
    
    

    
    
    

    


                                         
