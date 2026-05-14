# kullanici_modulu.py

class Kullanici:
    """Temel kimlik bilgilerini tutan üst sınıf."""
    def __init__(self, ad_soyad, tc_no):
        self.ad_soyad = ad_soyad
        self.tc_no = tc_no

class Musteri(Kullanici):
    """Kullanici sınıfından miras alan alt sınıf."""
    def __init__(self, ad_soyad, tc_no, musteri_id, tema_rengi):
        super().__init__(ad_soyad, tc_no)
        self.id = musteri_id
        self.tema = tema_rengi
        self.islem_kayitlari = []

    def log_ekle(self, mesaj):
        self.islem_kayitlari.append(mesaj)