# Order Lookup CLI

Bu proje, 24 Günlük Applied AI / AI Automation çalışma programının 1. gününde geliştirilen küçük bir Python uygulamasıdır.

Amaç; Python temellerini, JSON veri okuma mantığını, list/dict kullanımını, döngüleri, koşulları ve fonksiyonları tek bir çalışan uygulamada birleştirmektir.

## Proje Ne Yapıyor?

Uygulama `orders.json` dosyasındaki siparişleri okur.

Kullanıcı terminalden bir sipariş numarası girer.

Program:

1. JSON dosyasını okur.
2. Sipariş listesini Python list/dict yapısına çevirir.
3. Girilen sipariş numarasını arar.
4. Sipariş bulunursa bilgileri gösterir.
5. Sipariş bulunamazsa kullanıcıya bilgi verir.

## Dosya Yapısı

```text
09_order_lookup/
├── orders.json
├── order_lookup.py
└── README.md
```

### `orders.json`

Sipariş verilerini tutar.

Örnek:

```json
[
  {
    "order_no": "1001",
    "customer": "Dilan",
    "product": "Kulaklik",
    "status": "Kargoda"
  }
]
```

### `order_lookup.py`

JSON dosyasını okuyup sipariş aramasını yapan Python programıdır.

### `README.md`

Projenin nasıl çalıştığını ve çalışma sırasında öğrenilenleri açıklar.

## Nasıl Çalıştırılır?

Terminalde proje klasörüne gir:

```bash
cd 09_order_lookup
```

Ardından:

```bash
python order_lookup.py
```

Program bir sipariş numarası ister:

```text
Aradığınız sipariş numarasını giriniz: 1001
```

Örnek başarılı çıktı:

```text
Sipariş bulundu!
Sipariş No: 1001
Müşteri Adı: Dilan
Ürün Adı: Kulaklik
Durum: Kargoda
```

Olmayan bir sipariş numarası girilirse:

```text
Sipariş bulunamadı.
```

## Bugün Öğrendiğim Python Konuları

- `print()`
- değişkenler
- `str`
- `int`
- `float`
- `bool`
- `type()`
- matematik operatörleri
- `input()`
- tip dönüşümleri
- f-string
- string index ve slicing
- string metotları
- `if / elif / else`
- karşılaştırma operatörleri
- `and / or / not`
- listeler
- dictionary
- `for`
- `while`
- `break`
- fonksiyonlar
- parametreler
- `return`
- JSON dosyası okuma

## Karşılaştığım Hatalar ve Çıkardığım Dersler

### 1. Boolean yazımı

Python'da boolean değerler:

```python
True
False
```

şeklinde yazılır.

### 2. ValueError

`int()` ile sayıya çevrilemeyen bir metin dönüştürülmeye çalışıldığında oluşabilir.

```python
int("yirmi")
```

çalışmaz.

### 3. KeyboardInterrupt

Program `input()` beklerken elle durdurulduğunda görülebilir.

### 4. Reserved keyword

Python'ın özel kelimeleri değişken adı olarak kullanılamaz.

Örneğin `not` bir Python anahtar kelimesidir.

### 5. Indentation

Python'da girinti programın davranışını doğrudan etkiler.

Bir satırın döngü içinde veya dışında olması sonucu değiştirebilir.

### 6. FileNotFoundError

Python dosyayı çalışma dizininde arar.

Terminal yanlış klasördeyse `orders.json` bulunamayabilir.

### 7. KeyError

Dictionary veya JSON içinde olmayan bir key'e erişmeye çalışınca oluşur.

JSON'daki key isimleri Python'da birebir aynı kullanılmalıdır.

### 8. NameError

Bir değişken oluşturulmadan kullanılmaya çalışılırsa oluşabilir.

### 9. TypeError

Fonksiyonun beklediği parametre sayısı ile çağrıda verilen argüman sayısı uyuşmazsa oluşabilir.

## Gün 1 Sonucu

Bugün yalnızca Python syntax çalışmak yerine öğrendiğim kavramları küçük bir gerçek uygulamada birleştirdim.

Temel akış:

```text
veri kaynağı
→ veriyi oku
→ kullanıcı girdisi al
→ veriyi işle
→ doğru kaydı bul
→ sonucu döndür
```

Sonraki adımda bu yapı fonksiyonlara ve modüllere ayrılarak hata yönetimi eklenecek.
