#Step motor kütüphenesi kullanma#                     #// Step motorun kütüphanesinin kullanımını anlatan uygulamadır. //#

# Step motoru çalıştırmak için Step motor jumperın takılı olduğundan emin olun.
# "step_lib.py" dosyasını aynı isimde Pico'nun içine kaydedin. İsmini değiştirmeyin!

from machine import Pin                                                                        
import utime
from step_lib import tamTurIleri, tamTurGeri, yarimTurIleri, yarimTurGeri, ceyrekTurIleri, ceyrekTurGeri, adimSayIleri, adimSayGeri
# Parametreler pozitif tam sayı olarak girilmelidir.
# İlk parametre tur sayısı(varsayılan=1) , 2. parametre tur hızı (1-100 aralığında, varsayılan=100)

while True:
    print("Tam Tur İleri")        
    tamTurIleri(1,100)            # 100 hızında 1 tam ileri tur (Saat Yönü Tersi)         
    
    print("Tam Tur Geri")
    tamTurGeri(2,100)             # 100 hızında 2 tam geri tur  (Saat Yönü) 
    
    print("Yarım Tur İleri")
    yarimTurIleri(1,98)           # 98 hızında 1 yarım ileri tur  
    
    print("Yarım Tur Geri")
    yarimTurGeri(2,97)            # 97 hızında 2 yarım geri tur  
    
    print("Çeyrek Tur İleri")
    ceyrekTurIleri(3,95)          # 95 hızında 3 çeyrek ileri tur  
    
    print("Çeyrek Tur Geri")
    ceyrekTurGeri(2, 90)          # 90 hızında 2 çeyrek geri tur
    
    print("Adım Sayısı İleri")
    adimSayIleri(64, 100)          # 100 hızında 64 adım ileri, hassas döndürme
    
    print("Adım Sayısı Geri")
    adimSayGeri(64, 100)          # 100 hızında 64 adım geri, hassas döndürme
    
    print("TURLAR BİTTİ")
    print("--------------------------------------------------")
    
