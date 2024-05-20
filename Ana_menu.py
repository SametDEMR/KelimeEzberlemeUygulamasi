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
        Gizle_Modul.buton1_gizle(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def baslaFunction(self):
        print("basla")

    def sonrakisoruFunction(self):
        print("sonraki")

    def oncekisoruFunction(self):
        print("önceki")

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def menu1Function(self):
        Gizle_Modul.buton1_gizle(self)
        Goster_Modul.buton1_goster(self)

    def menu2Function(self):
        Goster_Modul.buton2_goster(self)

    def menu3Function(self):
        Goster_Modul.buton3_goster(self)

    def exitFunction(self):
        sys.exit(app.exec_())

    def ayarlarFunction(self):
        print("ayarlar")

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ana_pencere = Ana_Pencere1()
    ana_pencere.show()
    sys.exit(app.exec_())
