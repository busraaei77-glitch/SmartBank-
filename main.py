# main.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from kullanici_modulu import Musteri
from hesap_modulu import BankaHesabi

class ModernBanka(QWidget):
    def __init__(self):
        super().__init__()
        # Veri Yapısı (Haticenur, Büşra, Rümeysa)
        self.veritabani = {
            "Haticenur": {"m": Musteri("Haticenur", "101", "ID-1", "#FFD1DC"), "h": BankaHesabi("TR01", 1000)},
            "Büşra": {"m": Musteri("Büşra", "102", "ID-2", "#FFCC99"), "h": BankaHesabi("TR02", 2000)},
            "Rümeysa": {"m": Musteri("Rümeysa", "103", "ID-3", "#B2FFFF"), "h": BankaHesabi("TR03", 1500)}
        }
        self.aktif_ad = "Haticenur"
        self.arayuz_yukle()

    def arayuz_yukle(self):
        self.setWindowTitle("SmartStore Bank Automation")
        self.resize(800, 500)
        self.setStyleSheet("background-color: #121212; color: white; font-family: Arial;")

        ana_duzen = QHBoxLayout(self)

        # SOL MENÜ (Profil Seçimi)
        sol_menu = QFrame()
        sol_menu.setStyleSheet("background-color: #1E1E1E; border-right: 2px solid #333;")
        sol_layout = QVBoxLayout(sol_menu)
        
        for isim in self.veritabani.keys():
            btn = QPushButton(isim)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("padding: 15px; border: none; font-weight: bold;")
            btn.clicked.connect(lambda ch, n=isim: self.profil_degistir(n))
            sol_layout.addWidget(btn)
        sol_layout.addStretch()
        ana_duzen.addWidget(sol_menu, 1)

        # SAĞ PANEL (İşlemler)
        sag_panel = QVBoxLayout()
        
        self.lbl_baslik = QLabel("Müşteri Paneli")
        self.lbl_baslik.setStyleSheet("font-size: 24px; font-weight: bold; color: #BB86FC;")
        sag_panel.addWidget(self.lbl_baslik)

        self.lbl_bakiye = QLabel("Bakiye: 0.00 TL")
        self.lbl_bakiye.setStyleSheet("font-size: 30px; color: #03DAC6; padding: 10px 0;")
        sag_panel.addWidget(self.lbl_bakiye)

        # İşlem Girdi Alanı
        islem_kutu = QHBoxLayout()
        self.txt_miktar = QLineEdit()
        self.txt_miktar.setPlaceholderText("Miktar girin...")
        self.txt_miktar.setStyleSheet("padding: 10px; background: #2C2C2C; border: 1px solid #444;")
        islem_kutu.addWidget(self.txt_miktar)

        btn_yatir = QPushButton("Para Yatır")
        btn_yatir.clicked.connect(lambda: self.islem_tetikle(1))
        btn_yatir.setStyleSheet("background: #03DAC6; color: black; padding: 10px;")
        islem_kutu.addWidget(btn_yatir)

        btn_cek = QPushButton("Para Çek")
        btn_cek.clicked.connect(lambda: self.islem_tetikle(-1))
        btn_cek.setStyleSheet("background: #CF6679; color: black; padding: 10px;")
        islem_kutu.addWidget(btn_cek)
        sag_panel.addLayout(islem_kutu)

        # Ekstra İşlemler (EFT ve Fatura)
        ek_islem_layout = QHBoxLayout()
        btn_eft = QPushButton("EFT Gönder (Ücretsiz)")
        btn_eft.clicked.connect(lambda: self.islem_tetikle(-1, "EFT"))
        ek_islem_layout.addWidget(btn_eft)
        
        btn_fatura = QPushButton("Fatura Öde (Elektrik)")
        btn_fatura.clicked.connect(lambda: self.islem_tetikle(-250, "Fatura"))
        ek_islem_layout.addWidget(btn_fatura)
        sag_panel.addLayout(ek_islem_layout)

        # İşlem Geçmişi
        self.liste_kayit = QListWidget()
        self.liste_kayit.setStyleSheet("background: #1E1E1E; border: none; padding: 5px;")
        sag_panel.addWidget(QLabel("Son İşlemler:"))
        sag_panel.addWidget(self.liste_kayit)

        ana_duzen.addLayout(sag_panel, 3)
        self.profil_degistir(self.aktif_ad)

    def profil_degistir(self, ad):
        self.aktif_ad = ad
        data = self.veritabani[ad]
        self.lbl_baslik.setText(f"Müşteri: {data['m'].ad_soyad} ({data['m'].id})")
        self.lbl_baslik.setStyleSheet(f"font-size: 24px; color: {data['m'].tema};")
        self.ekran_guncelle()

    def ekran_guncelle(self):
        data = self.veritabani[self.aktif_ad]
        self.lbl_bakiye.setText(f"Bakiye: {data['h'].bakiye:.2f} TL")
        self.liste_kayit.clear()
        self.liste_kayit.addItems(reversed(data['m'].islem_kayitlari))
        self.txt_miktar.clear()

    def islem_tetikle(self, carpan, tip="Genel"):
        try:
            val = float(self.txt_miktar.text()) if tip == "Genel" else abs(carpan)
            final_val = val if (carpan > 0 and tip == "Genel") else -val
            
            hesap = self.veritabani[self.aktif_ad]["h"]
            musteri = self.veritabani[self.aktif_ad]["m"]
            
            if hesap.transfer(final_val):
                islem_adi = "Yatırma" if final_val > 0 else f"{tip} İşlemi"
                musteri.log_ekle(f"{islem_adi}: {abs(final_val)} TL")
                self.ekran_guncelle()
            else:
                QMessageBox.critical(self, "Hata", "Bakiye yetersiz veya geçersiz tutar!")
        except:
            QMessageBox.warning(self, "Uyarı", "Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernBanka()
    window.show()
    sys.exit(app.exec_())