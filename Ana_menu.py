import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json


from Buton_oluşturma import *
from Text_box_oluşturma import *
from Label_olusturma import *
from ShowHide import *

locale.setlocale(locale.LC_ALL, 'turkish')

class Ana_Pencere123(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kelime Ezberleme Modülü")
        self.setFixedSize(1200, 600)

        """self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)"""

        """self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1200, 600)  # Pencere boyutlarına uygun boyutta ayarla
        self.background_label.setPixmap(QPixmap('resim.png'))
        self.background_label.setScaledContents(True)"""

        Text_box_olustur_Modul.createTextBox(self)
        Label_olusturma.createLabels(self)
        Buton_Olustur_Modul.createButtons(self)
        ShowHide.hepsini_gizleme(self)
        ShowHide.ana_ekran_goster(self)

    def login(self):
        self.line_edit_içi_sil()
        username = self.line_edit_kullanici_adi.text()
        password = self.line_edit_sifre.text()

        if len(username) == 0 or len(password) == 0:
            self.label_aciklama.setText("Lütfen Bilgileri Eksiksiz Giriniz")
        else:
            ShowHide.hepsini_gizleme(self)
            print("SINAV İÇERİĞİ BURAYA GELECEK")


    def sifre_unuttum(self):
        self.line_edit_içi_sil()
        ShowHide.hepsini_gizleme(self)
        ShowHide.geri_goster(self)

    def kayit(self):
        self.line_edit_içi_sil()
        ShowHide.hepsini_gizleme(self)
        ShowHide.geri_goster(self)
        ShowHide.kayit_goster(self)

    def sifre_goster_gizle(self):
        sender = self.sender()
        if sender.isChecked():
            self.line_edit_sifre.setEchoMode(QLineEdit.Normal)
        else:
            self.line_edit_sifre.setEchoMode(QLineEdit.Password)

    def geri(self):
        self.line_edit_içi_sil()
        ShowHide.hepsini_gizleme(self)
        ShowHide.geri_gizle(self)
        ShowHide.ana_ekran_goster(self)

    def line_edit_içi_sil(self):
        self.line_edit_kullanici_adi.clear()
        self.line_edit_sifre.clear()
        self.line_edit_isim.clear()
        self.line_edit_soyisim.clear()
        self.line_edit_mail.clear()

    def kaydol(self):

        print("kaydol")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = Ana_Pencere123()
    giris_sayfasi.show()
    sys.exit(app.exec_())
