from AnaButonlar import *
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
        self.buton_resim_sec.hide()

        self.yazi_dogru.hide()
        self.yazi_yanlis.hide()
        self.yazi_bos.hide()
        self.yazi_toplam.hide()
        self.yazi_dogru_sayi.hide()
        self.yazi_yanlis_sayi.hide()
        self.yazi_bos_sayi.hide()
        self.yazi_toplam_sayi.hide()

        self.ing.hide()
        self.tr.hide()

        self.A.hide()
        self.B.hide()
        self.C.hide()

        self._5.hide()
        self._10.hide()
        self._15.hide()
        self._20.hide()

        self.ses_soru.hide()
        self.ses_soru_cümle.hide()
        self.ses_A.hide()
        self.ses_B.hide()
        self.ses_C.hide()

        self.cümle_soru.hide()

        self.line_edit_kullanici_adi.hide()
        self.line_edit_sifre.hide()

        self.line_edit_isim.hide()
        self.line_edit_soyisim.hide()
        self.line_edit_kaydol_sifre.hide()
        self.line_edit_kaydol_kullanici_adi.hide()

        self.line_edit_sifre_kullanici_adi.hide()

        self.line_edit_kelime_ingilizce.hide()
        self.line_edit_kelime_turkce.hide()
        self.line_edit_ingilizce_cümle.hide()
        self.line_edit_türkçe_cümle.hide()

        self.label_giris.hide()
        self.label_sinav_sayac.hide()
        self.label_metin.hide()
        self.label_ayarlar_sayi.hide()
        self.label_ayarlar_dil.hide()

        self.label_ekleme_resim.hide()
        self.label_kelime_ekle.hide()
        self.label_resim_soru.hide()

        self.yazdir.hide()
        self.toplam_dogru_sayi.hide()
        self.toplam_yanlis_sayi.hide()
        self.toplam_bos_sayi.hide()
        self.toplam_soru_sayi.hide()
        self.ortalama_sayi.hide()

        self._6lik.hide()
        self._5lik.hide()
        self._4lik.hide()
        self._3lik.hide()
        self._2lik.hide()
        self._1lik.hide()
        self._6lik_yazi.hide()
        self._5lik_yazi.hide()
        self._4lik_yazi.hide()
        self._3lik_yazi.hide()
        self._2lik_yazi.hide()
        self._1lik_yazi.hide()


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def giris(self):
        self.buton_giriş.show()
        self.buton_sifreunuttum.show()
        self.buton_kayit.show()
        self.buton_sifre_goster.show()
        self.buton_cikis.show()

        self.line_edit_kullanici_adi.show()
        self.line_edit_sifre.show()

        self.label_giris.show()

    def kayit(self):
        self.buton_geri_giris.show()

        self.buton_kaydol.show()

        self.line_edit_isim.show()
        self.line_edit_soyisim.show()
        self.line_edit_kaydol_sifre.show()
        self.line_edit_kaydol_kullanici_adi.show()

        self.label_giris.show()

    def sifre_unuttum(self):
        self.buton_geri_giris.show()

        self.buton_sifre_getir.show()

        self.line_edit_sifre_kullanici_adi.show()

        self.label_giris.show()

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

        self.ses_soru.show()

        self.A.show()
        self.B.show()
        self.C.show()
        self.ses_soru.show()
        self.ses_soru_cümle.show()
        self.ses_A.show()
        self.ses_B.show()
        self.ses_C.show()

        self.cümle_soru.show()

        self.label_metin.show()
        self.label_sinav_sayac.show()
        self.label_resim_soru.show()

    def soru_ekleme(self):
        self.buton_geri_sinav.show()

        self.buton_kelime_ekle_ekle.show()

        self.line_edit_kelime_ingilizce.show()
        self.line_edit_kelime_turkce.show()
        self.line_edit_ingilizce_cümle.show()
        self.line_edit_türkçe_cümle.show()

        self.buton_resim_sec.show()

        self.label_ekleme_resim.show()
        self.label_kelime_ekle.show()

    def analiz(self):
        self.buton_geri_sinav.show()

        self.yazdir.show()
        self.toplam_dogru_sayi.show()
        self.toplam_yanlis_sayi.show()
        self.toplam_bos_sayi.show()
        self.toplam_soru_sayi.show()
        self.ortalama_sayi.show()

        self._6lik.show()
        self._5lik.show()
        self._4lik.show()
        self._3lik.show()
        self._2lik.show()
        self._1lik.show()
        self._6lik_yazi.show()
        self._5lik_yazi.show()
        self._4lik_yazi.show()
        self._3lik_yazi.show()
        self._2lik_yazi.show()
        self._1lik_yazi.show()

    def ayarlar(self):
        self.buton_geri_sinav.show()

        self.ing.show()
        self.tr.show()

        self._5.show()
        self._10.show()
        self._15.show()
        self._20.show()

        self.label_ayarlar_sayi.show()
        self.label_ayarlar_dil.show()

    def sinav_sonu_analiz(self):
        self.buton_geri_sinav.show()

        self.yazi_dogru.show()
        self.yazi_yanlis.show()
        self.yazi_bos.show()
        self.yazi_toplam.show()
        self.yazi_dogru_sayi.show()
        self.yazi_yanlis_sayi.show()
        self.yazi_bos_sayi.show()
        self.yazi_toplam_sayi.show()
