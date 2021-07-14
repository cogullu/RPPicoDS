#PIR ve buton kullanımı, kesme#                     #// PIR Sensörününü buton kesmesi kullanarak durduran uygulamadır. //#

from machine import Pin                                                                        
import utime

pressed = False

led_k = Pin(2, Pin.OUT)   # Alarm Işığı
buzzer = Pin(10, Pin.OUT) # Alarm sireni
PIR = Pin(19, Pin.IN, Pin.PULL_DOWN)
buton_1 = Pin(5, Pin.IN, Pin.PULL_DOWN)  # Alarm durdurma butonu

led_k.value(0)
buzzer.value(0)
alarm_durum = True

def buton_1_handler(pin):
    global pressed
    global alarm_durum
    if not pressed:
        pressed= True
        print("Alarm Durduruldu...")
        buzzer.value(0)
        led_k.value(0)
        PIR.value(0)
        alarm_durum = False
   
buton_1.irq(trigger=Pin.IRQ_RISING, handler=buton_1_handler)

while True:           
    if PIR.value():                         # PIR Sensörü True(1) olduğunda
        print("Bir Cisim Algılandı... :D")
        
        
        for j in range(180):
            if alarm_durum == False:        # Alarm çalarken butona basılırsa döngüden çıkar.
                break
                
            buzzer.toggle()
            led_k.toggle()
            utime.sleep_ms(70)
        
    led_k.value(0)
    buzzer.value(0)
    print("Algılanan bir cisim yok...")
    
    utime.sleep(0.5)                     # Her yarım saniyede kontrol eder.
    pressed = False
    alarm_durum = True                 # Daha önceden butona basıldıysa butonu eski haline getirmek için.
    PIR.value(0)
    
        
     

    

    


                                         
