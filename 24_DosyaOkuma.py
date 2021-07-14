with open("sicaklik.txt", "a+") as dosya:   # sicaklik.txt isminde dosya oluşturuluyor ve dosya objesine aktarılıyor.
        print(dosya.read())
# Dosya bir kez tamamen okunduktan sonra imleç otomatik olarak başa dönmüyor.
# Dosyayı tekrar okumak istiyorsak, bunu başa sarmamız lazım. İşte bunun için seek() metodunu kullanacağız.
# Bu metodu kullanmazsanız, dosyanın sonuna geldiğinizde tekrar okuma yaparsanız boşlukla karşılaşırsınız.


#         dosya.seek(0)                   # imleci tekrar başa aldık.             
#         veriListe = dosya.readlines()   # dosyadaki satırları listeye kaydettik.
#         dosya.seek(0)                   # her kullanımdan sonra tekrar okumak istiyorsak başa almalıyız.
#         for i in range(len(veriListe)): # dosyadaki satır sayısı kadar döngü oluşturduk.
#             print(dosya.readline())     # her bir satırı ayrı ayrı yazdırdık.
  
  
#         dosya.seek(0)                  
#         print(dosya.readlines())
    
# dosya.read())       # read() metodu dosyanın tamamını okuyor.
# dosya.readline()    # readline() metodu dosyayı satır satır okuyor.
# dosya.readlines()   # readlines() metodu dosyayı liste olarak geri döndürür.