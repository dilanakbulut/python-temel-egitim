# def selam_ver():
#     print("Merhaba! Nasılsınız?")
# selam_ver()
# selam_ver()
# def selam_ver(isim):
#     print(f"Merhaba {isim}! Nasılsınız?")

# selam_ver("Dilan")
# selam_ver("Ahmet")
# def topla(sayi1, sayi2):
#     return sayi1 + sayi2
# toplam_sonucu = topla(5, 10)
# print("Toplam sonucu: ", toplam_sonucu)
# def kisi_bilgisi(isim, soyisim, yas):
#     print(f"İsim: {isim}")
#     print(f"Soyisim: {soyisim}")
#     print(f"Yaş: {yas}")
# kisi_bilgisi("Dilan", "Dursun", 25)
# kisi_bilgisi("Ahmet", "Yılmaz", 30)
def hesapla_fiyat(urun_fiyati, urun_adedi):
    toplam_tutar = urun_fiyati * urun_adedi
    return toplam_tutar

# Örnek kullanım
fiyat = hesapla_fiyat(250, 4)
print("Toplam fiyat: ", fiyat)