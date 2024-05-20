import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

class ShowHide(QWidget):

    def hepsini_gizleme(self):
        self.buton_giriş.hide()
        self.buton_sifreunuttum.hide()
        self.buton_kayit.hide()
        self.buton_sifre_goster.hide()
        self.buton_geri1.hide()
        self.buton_kaydol.hide()
        self.buton_sifre_getir.hide()

        self.label_aciklama.hide()

        self.line_edit_kullanici_adi.hide()
        self.line_edit_sifre.hide()
        self.line_edit_isim.hide()
        self.line_edit_soyisim.hide()
        self.line_edit_mail.hide()
        self.line_edit_kaydol_kullanici_adi.hide()
        self.line_edit_sifre_kullanici_adi.hide()
        self.line_edit_sifre_mail.hide()

    def ana_ekran_goster(self):
        self.buton_giriş.show()
        self.buton_sifreunuttum.show()
        self.buton_kayit.show()
        self.buton_sifre_goster.show()

        self.label_aciklama.show()

        self.line_edit_kullanici_adi.show()
        self.line_edit_sifre.show()

    def sifre_unuttum_goster(self):
        self.buton_sifre_getir.show()

        self.line_edit_sifre_kullanici_adi.show()
        self.line_edit_sifre_mail.show()

        self.label_aciklama.show()

    def kayit_goster(self):
        self.buton_kaydol.show()
        self.buton_sifre_goster.show()

        self.line_edit_sifre.show()
        self.line_edit_isim.show()
        self.line_edit_soyisim.show()
        self.line_edit_mail.show()
        self.line_edit_kaydol_kullanici_adi.show()

        self.label_aciklama.show()

    def gecis_islemleri(self):
        self.label_aciklama.setText("")

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
            self.buton_geri1.show()