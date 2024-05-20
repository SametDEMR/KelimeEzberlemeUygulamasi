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


class SinavShowHide(QWidget):

    def hepsini_gizleme(self):
        self.buton_geri2.hide()

        self.buton_sinav.hide()
        self.buton_soru_ekleme.hide()
        self.buton_analiz.hide()
        self.buton_çıkış.hide()

        self.buton_sonraki_soru.hide()
        self.buton_önceki_soru.hide()

        self.buton_soru_ekle_ekle.hide()

        self.sik_a.hide()
        self.sik_b.hide()
        self.sik_c.hide()
        self.sik_d.hide()


    def ana_ekran_goster(self):
        self.buton_sinav.show()
        self.buton_soru_ekleme.show()
        self.buton_analiz.show()
        self.buton_çıkış.show()

    def sinav_sayfasi(self):
        self.buton_geri2.show()

        self.buton_sonraki_soru.show()
        self.buton_önceki_soru.show()

        self.sik_a.show()
        self.sik_b.show()
        self.sik_c.show()
        self.sik_d.show()

    def soru_ekleme_sayfasi(self):
        self.buton_geri2.show()
        self.buton_soru_ekle_ekle.show()

    def analiz_sayfasi(self):
        self.buton_geri2.show()