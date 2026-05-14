# hesap_modulu.py

class BankaHesabi:
    """Bakiye ve finansal işlemleri yöneten sınıf."""
    def __init__(self, hesap_no, ilk_bakiye=0.0):
        self.hesap_no = hesap_no
        self._bakiye = ilk_bakiye # Gizli nitelik (Encapsulation)

    @property
    def bakiye(self):
        """Bakiyeyi dışarıya güvenli bir şekilde sunar."""
        return self._bakiye

    @bakiye.setter
    def bakiye(self, yeni_deger):
        """Bakiyenin negatif olmasını engeller."""
        if yeni_deger < 0:
            raise ValueError("Bakiye yetersiz!")
        self._bakiye = yeni_deger

    def transfer(self, miktar):
        """Negatif değerler harcama/çekme, pozitifler yatırma."""
        try:
            self.bakiye += miktar # Setter kontrolü burada çalışır
            return True
        except ValueError:
            return False