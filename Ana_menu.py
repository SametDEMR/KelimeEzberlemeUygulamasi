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

        Text_box_olustur_Modul.createTextBox(self)
        Label_olusturma.createLabels(self)
        Buton_Olustur_Modul.createButtons(self)

        ShowHide.hepsini_gizleme(self)
        ShowHide.ana_ekran_goster(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def giris(self):
        username = self.line_edit_kullanici_adi.text()
        password = self.line_edit_sifre.text()

        if len(username) == 0 or len(password) == 0:
            self.label_aciklama.setText("Lütfen Bilgileri Eksiksiz Giriniz")
        else:
            self.gecis_islemleri()

            print("SINAV İÇERİĞİ BURAYA GELECEK")

    def sifre_unuttum(self):
        self.gecis_islemleri()

        ShowHide.sifre_unuttum_goster(self)

    def kayit(self):
        self.gecis_islemleri()

        ShowHide.kayit_goster(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sifre_goster_gizle(self):
        sender = self.sender()
        if sender.isChecked():
            self.line_edit_sifre.setEchoMode(QLineEdit.Normal)
        else:
            self.line_edit_sifre.setEchoMode(QLineEdit.Password)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def kaydol(self):
        print("kaydol")

    def geri(self):
        self.gecis_islemleri()

        ShowHide.ana_ekran_goster(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def gecis_islemleri(self):
        self.line_edit_kullanici_adi.clear()
        self.line_edit_sifre.clear()
        self.line_edit_isim.clear()
        self.line_edit_soyisim.clear()
        self.line_edit_mail.clear()
        self.line_edit_kaydol_kullanici_adi.clear()
        self.line_edit_sifre_kullanici_adi.clear()
        self.line_edit_sifre_mail.clear()

        ShowHide.hepsini_gizleme(self)

        caller_func = sys._getframe(1).f_code.co_name
        if caller_func != "giris" and caller_func != "geri":
            ShowHide.geri_goster(self)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = Ana_Pencere123()
    giris_sayfasi.show()
    sys.exit(app.exec_())
