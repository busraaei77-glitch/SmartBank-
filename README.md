# SmartBank-
SmartBank;
# 🏦 SmartStore Bank Automation

PyQt5 kullanılarak geliştirilmiş, Nesne Yönelimli Programlama (OOP) prensiplerini (Kalıtım, Kapsülleme, Polimorfizm) temel alan modüler bir bankacılık ve mağaza yönetim simülasyonu.


## takım üyeleri
*büşra arı
*haticenur yıldırım
*rümeysa aras


## ✨ Özellikler

*   *Dinamik Kullanıcı Paneli:* Müşteriler arası (Haticenur, Büşra, Rümeysa) anlık geçiş ve her müşteriye özel renk teması.
*   *Finansal İşlemler:* Para yatırma, para çekme, ücretsiz EFT gönderimi ve fatura ödeme simülasyonları.
*   *Akıllı Stok ve Fiyat Yönetimi:* @property ve setter metodları ile negatif fiyat/stok girişini engelleyen kapsülleme mekanizması.
*   *İşlem Geçmişi:* Yapılan tüm işlemlerin gerçek zamanlı loglanması ve kullanıcı arayüzünde listelenmesi.
*   *Modern Arayüz:* Karanlık mod (Dark Mode) temasıyla optimize edilmiş kullanıcı deneyimi.

## 📂 Proje Yapısı

Proje, sürdürülebilirlik için üç ana modüle ayrılmıştır:

1.  *main.py:* Uygulamanın giriş noktası. PyQt5 arayüz mantığını ve buton tetikleyicilerini içerir.
2.  *kullanici_modulu.py:* Kullanici temel sınıfı ve ondan miras alan Musteri sınıfını barındırır.
3.  *hesap_modulu.py:* BankaHesabi, Urun ve Magaza sınıflarını içeren mantıksal katman.

## 🛠️ Kurulum ve Kullanım

1.  *Gereksinimleri Yükleyin:*
    ```bash
    pip install PyQt5

    ## 💻 Teknik Detaylar

*   *Dil:* Python 3.x
*   *Kütüphane:* PyQt5
*   *Mimari:* Modüler OOP
*   *Arayüz:* QVBoxLayout, QHBoxLayout, QFrame ve Özel QSS (Qt Style Sheets)
