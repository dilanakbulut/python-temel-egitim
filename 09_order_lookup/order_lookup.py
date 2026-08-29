import json

with open("orders.json", "r", encoding="utf-8") as dosya:
    siparisler = json.load(dosya)

print(siparisler)
print(type(siparisler))
print(type(siparisler[0]))
# aranan_siparis_no = input("Aradığınız sipariş numarasını giriniz: ")
# bulundu = False
# for siparis in siparisler:
#     if siparis["order_no"] == aranan_siparis_no:
#         print("Sipariş bulundu!")
#         print("Sipariş No:", siparis["order_no"])
#         print("Müşteri Adı:", siparis["customer"])
#         print("Ürün Adı:", siparis["product"])
#         print("Durum:", siparis["status"])
#         bulundu = True
#         break
# if bulundu == False:
#     print("Sipariş bulunamadı.")
def siparis_bul(siparisler, aranan_no):
    for siparis in siparisler:
        if siparis["order_no"] == aranan_no:
            return siparis
    return None
aranan_siparis_no = input("Aradığınız sipariş numarasını giriniz: ")
sonuc = siparis_bul(siparisler, aranan_siparis_no)

if sonuc is not None:
    print("Sipariş bulundu!")
    print("Sipariş No:", sonuc["order_no"])
    print("Müşteri Adı:", sonuc["customer"])
    print("Ürün Adı:", sonuc["product"])
    print("Durum:", sonuc["status"])
else:
    print("Sipariş bulunamadı.")