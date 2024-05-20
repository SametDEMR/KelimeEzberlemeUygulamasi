import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

from GirisButonOlusturma import *
from GirisTextBoxOlusturma import *
from GirisLabelOlusturma import *
from GirisShowHide import *
from SinavButonOlusturma import *
from SinavShowHide import *
from SinavLabelOlusturma import *

locale.setlocale(locale.LC_ALL, 'turkish')


class Ana_Pencere123(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kelime Ezberleme Modülü")
        self.setStyleSheet("background-color: #3c64c8 ")
        self.setFixedSize(1200, 600)

        Giris_Text_box_Olustur.createTextBox(self)
        Label_olusturma.createLabels(self)
        Giris_Buton_Olustur.Giris_Buton(self)

        Sinav_Buton_Olustur.Sinav_Buton(self)
        SinavShowHide.hepsini_gizleme(self)

        ShowHide.hepsini_gizleme(self)
        ShowHide.ana_ekran_goster(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def giris(self):
        username = self.line_edit_kullanici_adi.text()
        password = self.line_edit_sifre.text()

        if username and password:
            ShowHide.gecis_islemleri(self)

            SinavShowHide.ana_ekran_goster(self)

        else:
            self.label_aciklama.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    def sifre_unuttum(self):
        ShowHide.gecis_islemleri(self)

        ShowHide.sifre_unuttum_goster(self)

    def kayit(self):
        ShowHide.gecis_islemleri(self)

        ShowHide.kayit_goster(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def geri2(self):
        SinavShowHide.hepsini_gizleme(self)
        SinavShowHide.ana_ekran_goster(self)

    def sinav(self):
        SinavShowHide.hepsini_gizleme(self)
        SinavShowHide.sinav_sayfasi(self)

        print("sinav sayfası")

    def soru_ekleme(self):
        SinavShowHide.hepsini_gizleme(self)
        SinavShowHide.soru_ekleme_sayfasi(self)
        print("soru ekleme")

    def analiz(self):
        SinavShowHide.hepsini_gizleme(self)
        SinavShowHide.analiz_sayfasi(self)
        print("analiz")

    def cikis(self):
        QApplication.quit()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sifre_goster_gizle(self):
        sender = self.sender()
        if sender.isChecked():
            self.line_edit_sifre.setEchoMode(QLineEdit.Normal)
        else:
            self.line_edit_sifre.setEchoMode(QLineEdit.Password)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def geri(self):
        ShowHide.gecis_islemleri(self)

        ShowHide.ana_ekran_goster(self)

    def kaydol(self):
        isim = self.line_edit_isim.text()
        soyisim = self.line_edit_soyisim.text()
        mail = self.line_edit_mail.text()
        sifre = self.line_edit_sifre.text()
        kullanici_ad = self.line_edit_kaydol_kullanici_adi.text()

        if isim and soyisim and mail and sifre and kullanici_ad:
            self.label_aciklama.setText("Kayıt İşlemi Başarılı! Giriş İçin Ana Menüye Dönünüz.")
        else:
            self.label_aciklama.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    def sifre_getir(self):
        username = self.line_edit_sifre_kullanici_adi.text()
        mail = self.line_edit_sifre_mail.text()

        if len(username) == 0 or len(mail) == 0:
            self.label_aciklama.setText("Lütfen Bilgileri Eksiksiz Giriniz")
        else:
            self.label_aciklama.setText("Şifreniz = ")

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sonraki_soru(self):
        print("sonraki soru")

    def onceki_soru(self):
        print("önceki soru")

    def soruyu_ekle(self):
        print("soru eklendi")

    def buton_yazi_gonder(self, button):
        self.label_sik.setText(button.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = Ana_Pencere123()
    giris_sayfasi.show()
    sys.exit(app.exec_())