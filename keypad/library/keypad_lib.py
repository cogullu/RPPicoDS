#Keypad Kütüphanesi#                    #// Keypad butonlarının kullanımı için kütüphane dosyasıdır. //#
# Tuşların altındaki dirençlerin değerlerini okuyarak tuşu basıldığını algılar.

# # # # Bu kütüphane Ankara Kanuni MTAL - Atölye Ankara Ekibi Öğretmenleri tarafından yazılmıştır. # # # #
# # # # https://atolyeankara.com/ # # # #

from machine import Pin, ADC
import utime

keypad = ADC(28)             #KeyPad'in bağlı olduğu analog pindir.
# 1 analog pin kullanılarak, bu analog pine bağlı keypadin üzerindeki butonları dirençler ile okutuyoruz.

def keypadOku():            # Basılan karakteri döndüren fonksiyon.
    basilan=0
    deger=keypad.read_u16()  # Basılan karakterin direnci

    if(deger >200 and deger<500): # Tuşlara basılmazken direnç değeri aralığıdır. Bu durumda 0 döndürür.
        return 0    
    
    else:
        if(deger >65000):        
            basilan ='1'
        elif(deger >29000 and deger<36000):
            basilan = '2'
        elif(deger >19000 and deger<25000):
            basilan = '3'
        elif(deger >11500 and deger<12000):
            basilan = '4'
        elif(deger >9850 and deger<10250):
            basilan = '5'
        elif(deger >8500 and deger<9000):
            basilan = '6'
        elif(deger >6450 and deger<7000):
            basilan = '7'
        elif(deger >5900 and deger<6300):
            basilan = '8'
        elif(deger >5500 and deger<5850):
            basilan = '9'
        elif(deger >4600 and deger<5000):
            basilan = '*'
        elif(deger >4350 and deger<4600):
            basilan = '0'
        elif(deger >4000 and deger<4350):        
            basilan = '#'          
        
        utime.sleep(0.2)     # Tuş hassasiyeti süresi   
        return basilan
    
    

   
   

