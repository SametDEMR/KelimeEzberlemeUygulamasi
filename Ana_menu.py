from Gizleme import *
from Gosterme import *
from Buton_oluşturma import *

locale.setlocale(locale.LC_ALL, 'turkish')

class Ana_Pencere1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Depo Yönetim Sistemi")
        self.setFixedSize(1200, 600)


        Buton_Olustur_Modul.createButtons(self)

        Gizle_Modul.hepsini_gizle(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def baslaFunction(self):
        print("basla")

    def sonrakisoruFunction(self):
        print("sonraki")

    def oncekisoruFunction(self):
        print("önceki")

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sinavSayfasi(self):
        Gizle_Modul.hepsini_gizle(self)
        Goster_Modul.sinav_sayfasi_goster(self)

    def raporSayfasi(self):
        Gizle_Modul.hepsini_gizle(self)
        Goster_Modul.rapor_sayfasi_goster(self)

    def kelimeEkleme(self):
        Gizle_Modul.hepsini_gizle(self)
        Goster_Modul.kelime_ekleme_goster(self)

    def ayarlar(self):
        Gizle_Modul.hepsini_gizle(self)
        Goster_Modul.ayarlar_goster(self)

    def exit(self):
        sys.exit(app.exec_())

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ana_pencere = Ana_Pencere1()
    ana_pencere.show()
    sys.exit(app.exec_())
