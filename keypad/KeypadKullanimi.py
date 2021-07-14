#Keypad Kullanımı#                    #// Keypad butonlarının kullanımını gösteren uygulamadır. //#
# Uygulamayı çalıştırmadan önce keypad_lib.py dosyasını Pico'nun içine "keypad_lib.py" isminde farklı kaydet seçeneği ile kaydetmelisiniz.

from keypad_lib import keypadOku

while True:

    tus=keypadOku()        # Basılan karakter tus degiskenine aktarılıyor.
    if tus:                # tus 0 değilse, yani birşeye basılmışsa
        print(tus)