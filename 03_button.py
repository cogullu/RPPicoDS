#buton kullanımı#                         #// buton kullanımını gösteren uygulamadır. //#

from machine import Pin                                                                        
import utime

buton = Pin(5, Pin.IN, Pin.PULL_DOWN)     # 5 numaralı pini giriş olarak ayarladık. Böylece butondan gelen verileri okuyabileceğiz.
#// "PULL_DOWN" ifadesi, Piconun içindeki dahili direnç sayesinde butona basıldığında 1 değeri verir.
while True: 
     if buton.value() == 1:              # boton değeri 1 olduğunda, yani butona basıldığını kontrol eden if yapısıdır.
          # Girintilere dikkat edin!
          print("Butona Basıldı")        # "print" fonksiyonu ile REPL(kabuk-shell) ekranına yazı yazdırıyoruz.
          utime.sleep(2)                 # Kodlar çok hızlı çalıştığından bir buton basışında birden fazla basmış olmamak için
                                         # //2 sn bekleme koyarak kodun kararlı çalışmasını sağlıyoruz.
                                         # //Bu sayede butona basıldıktan sonraki 2 sn boyunca buton basışını algılamayacak.
