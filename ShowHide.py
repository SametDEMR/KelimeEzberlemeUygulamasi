import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

from ButonOlustur import *
from ana_menu import *

class ShowHide(QWidget):

    def hepsini_gizleme(self):
        self.buton_geri_giris.hide()
        self.buton_geri_sinav.hide()

        self.buton_giriş.hide()
        self.buton_sifreunuttum.hide()
        self.buton_kayit.hide()
        self.buton_sifre_goster.hide()

        self.buton_kaydol.hide()
        self.buton_sifre_getir.hide()

        self.buton_sinav.hide()
        self.buton_soru_ekleme.hide()
        self.buton_analiz.hide()
        self.buton_ayarlar.hide()
        self.buton_cikis.hide()

        self.buton_sinav_basla.hide()
        self.sinav_soru.hide()
        self.buton_sonraki_soru.hide()
        self.buton_önceki_soru.hide()
        self.buton_sinav_bitir.hide()

        self.buton_kelime_ekle_ekle.hide()

        self.dogru.hide()
        self.yanlis.hide()
        self.bos.hide()
        self.toplam.hide()

        self.dogru_sayi.hide()
        self.yanlis_sayi.hide()
        self.bos_sayi.hide()
        self.toplam_sayi.hide()

        self.A.hide()
        self.B.hide()
        self.C.hide()
        self.D.hide()

        self._5.hide()
        self._10.hide()
        self._15.hide()
        self._20.hide()

        self.ses_soru.hide()
        self.ses_A.hide()
        self.ses_B.hide()
        self.ses_C.hide()
        self.ses_D.hide()


        self.line_edit_kullanici_adi.hide()
        self.line_edit_sifre.hide()

        self.line_edit_isim.hide()
        self.line_edit_soyisim.hide()
        self.line_edit_mail.hide()
        self.line_edit_kaydol_sifre.hide()
        self.line_edit_kaydol_kullanici_adi.hide()

        self.line_edit_sifre_kullanici_adi.hide()
        self.line_edit_sifre_mail.hide()

        self.line_edit_kelime_ingilizce.hide()
        self.line_edit_kelime_turkcesi.hide()
        self.line_edit_cümle1.hide()
        self.line_edit_cümle2.hide()

        self.label_metin.hide()

        self.label_ayarlar.hide()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def giris(self):
        self.buton_giriş.show()
        self.buton_sifreunuttum.show()
        self.buton_kayit.show()
        self.buton_sifre_goster.show()
        self.buton_cikis.show()

        self.line_edit_kullanici_adi.show()
        self.line_edit_sifre.show()

    def kayit(self):
        self.buton_geri_giris.show()

        self.buton_kaydol.show()

        self.line_edit_isim.show()
        self.line_edit_soyisim.show()
        self.line_edit_mail.show()
        self.line_edit_kaydol_sifre.show()
        self.line_edit_kaydol_kullanici_adi.show()

    def sifre_unuttum(self):
        self.buton_geri_giris.show()

        self.buton_sifre_getir.show()

        self.line_edit_sifre_kullanici_adi.show()
        self.line_edit_sifre_mail.show()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def sinav_ana_menu(self):
        self.buton_sinav.show()
        self.buton_soru_ekleme.show()
        self.buton_analiz.show()
        self.buton_cikis.show()
        self.buton_ayarlar.show()

    def sinav_sayfasi_once(self):
        self.buton_geri_sinav.show()

        self.buton_sinav_basla.show()

    def sinav_sayfasi_sonra(self):
        self.buton_sonraki_soru.show()
        self.sinav_soru.show()

        self.label_metin.show()

        self.A.show()
        self.B.show()
        self.C.show()
        self.D.show()

        self.ses_soru.show()
        self.ses_A.show()
        self.ses_B.show()
        self.ses_C.show()
        self.ses_D.show()

    def soru_ekleme(self):
        self.buton_geri_sinav.show()

        self.buton_kelime_ekle_ekle.show()

        self.line_edit_kelime_ingilizce.show()
        self.line_edit_kelime_turkcesi.show()
        self.line_edit_cümle1.show()
        self.line_edit_cümle2.show()

    def analiz(self):
        self.buton_geri_sinav.show()

    def ayarlar(self):
        self.buton_geri_sinav.show()
        self._5.show()
        self._10.show()
        self._15.show()
        self._20.show()

        self.label_ayarlar.show()

    def sinav_sonu_analiz(self):
        self.buton_geri_sinav.show()

        self.dogru.show()
        self.yanlis.show()
        self.bos.show()
        self.toplam.show()

        self.dogru_sayi.show()
        self.yanlis_sayi.show()
        self.bos_sayi.show()
        self.toplam_sayi.show()
