from AnaButonlar import *
from AAnaMenu import *
class ShowHide():
    def TumAraclariGizle(self):
        self.GirisSayfasiGeriGitme.hide()
        self.SinavAnaMenuGeriGitme.hide()

        self.GirisButonu.hide()
        self.SifremiUnuttumButonu.hide()
        self.KayitOlmaButonu.hide()
        self.SifreGosterGizleButonu.hide()

        self.KaydolButonu.hide()
        self.SifremiGetirButonu.hide()

        self.SinavSayfasiButonu.hide()
        self.SoruEklemeSayfasiButonu.hide()
        self.KelimelerSayfasiButonu.hide()
        self.AnalizSayfasiButonu.hide()
        self.AyarlarSayfasiButonu.hide()
        self.CikisButonu.hide()

        self.SinavaBaslaButonu.hide()
        self.SoruKelimeYeri.hide()
        self.SonrakiSoruButonu.hide()
        self.ÖncekiSoruButonu.hide()
        self.SinavBitirButonu.hide()

        self.KelimeyiEkleButonu.hide()
        self.ResimSecmeButonu.hide()

        self.KelimelerTablosu.hide()

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

        self.SoruKelimeMetniSeslendirme.hide()
        self.SoruCumleMetniSeslendirme.hide()
        self.ses_A.hide()
        self.ses_B.hide()
        self.ses_C.hide()

        self.SoruCümleKismi.hide()

        self.GirisKismiKullaniciAdi.hide()
        self.GirisKismiSifre.hide()

        self.KayitKismiIsim.hide()
        self.KayitKismiSoyisim.hide()
        self.KayitKismiSifre.hide()
        self.KayitKismiKullaniciAdi.hide()

        self.SifremiUnuttumKismiKullaniciAdi.hide()

        self.SoruEklemeIngilizce.hide()
        self.SoruEklemeTurkce.hide()
        self.SoruEklemeIngilizceCumle.hide()
        self.SoruEklemeTurkceCumle.hide()

        self.GirisKismiUyariMesaji.hide()
        self.SinavSayaci.hide()
        self.SoruAciklamasi.hide()
        self.AyarlarSoruSayisiKismi.hide()
        self.AyarlarDilKismi.hide()

        self.KelimeEklemeResimKismi.hide()
        self.KelimeEklemeUyariMesaji.hide()
        self.SoruResimKismi.hide()

        self.AnalizleriYazdir.hide()

        self.Yildiz1Tablosu.hide()
        self.Yildiz2Tablosu.hide()
        self.Yildiz3Tablosu.hide()
        self.Yildiz4Tablosu.hide()
        self.Yildiz5Tablosu.hide()
        self.Yildiz6Tablosu.hide()
        self.EzberlenmisTablosu.hide()

        self.toplam_dogru_yazi.hide()
        self.toplam_yanlis_yazi.hide()
        self.toplam_bos_yazi.hide()
        self.toplam_soru_yazi.hide()
        self.ortalama_yazi.hide()
        self.toplam_dogru_sayi.hide()
        self.toplam_yanlis_sayi.hide()
        self.toplam_bos_sayi.hide()
        self.toplam_soru_sayi.hide()
        self.ortalama_sayi.hide()


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def GirisAnaMenu(self):
        self.GirisButonu.show()
        self.SifremiUnuttumButonu.show()
        self.KayitOlmaButonu.show()
        self.SifreGosterGizleButonu.show()
        self.CikisButonu.show()

        self.GirisKismiKullaniciAdi.show()
        self.GirisKismiSifre.show()

        self.GirisKismiUyariMesaji.show()

    def KayitMenusu(self):
        self.GirisSayfasiGeriGitme.show()

        self.KaydolButonu.show()

        self.KayitKismiIsim.show()
        self.KayitKismiSoyisim.show()
        self.KayitKismiSifre.show()
        self.KayitKismiKullaniciAdi.show()

        self.GirisKismiUyariMesaji.show()

    def SifreUnuttumMenusu(self):
        self.GirisSayfasiGeriGitme.show()

        self.SifremiGetirButonu.show()

        self.SifremiUnuttumKismiKullaniciAdi.show()

        self.GirisKismiUyariMesaji.show()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def SinavUygulamasiAnaMenu(self):
        self.SinavSayfasiButonu.show()
        self.SoruEklemeSayfasiButonu.show()
        self.KelimelerSayfasiButonu.show()
        self.AnalizSayfasiButonu.show()
        self.CikisButonu.show()
        self.AyarlarSayfasiButonu.show()

    def SinavaBaslamaOncesi(self):
        self.SinavAnaMenuGeriGitme.show()

        self.SinavaBaslaButonu.show()

    def SinavaBaslamaSonrasi(self):
        self.SonrakiSoruButonu.show()
        self.SoruKelimeYeri.show()

        self.SoruAciklamasi.show()

        self.SoruKelimeMetniSeslendirme.show()

        self.A.show()
        self.B.show()
        self.C.show()
        self.SoruKelimeMetniSeslendirme.show()
        self.SoruCumleMetniSeslendirme.show()
        self.ses_A.show()
        self.ses_B.show()
        self.ses_C.show()

        self.SoruCümleKismi.show()

        self.SoruAciklamasi.show()
        self.SinavSayaci.show()
        self.SoruResimKismi.show()

    def SoruEklemeKismi(self):
        self.SinavAnaMenuGeriGitme.show()

        self.KelimeyiEkleButonu.show()

        self.SoruEklemeIngilizce.show()
        self.SoruEklemeTurkce.show()
        self.SoruEklemeIngilizceCumle.show()
        self.SoruEklemeTurkceCumle.show()

        self.ResimSecmeButonu.show()

        self.KelimeEklemeResimKismi.show()
        self.KelimeEklemeUyariMesaji.show()

    def AnalizSayfasi(self):
        self.SinavAnaMenuGeriGitme.show()

        self.AnalizleriYazdir.show()

        self.toplam_dogru_yazi.show()
        self.toplam_yanlis_yazi.show()
        self.toplam_bos_yazi.show()
        self.toplam_soru_yazi.show()
        self.ortalama_yazi.show()

        self.toplam_dogru_sayi.show()
        self.toplam_yanlis_sayi.show()
        self.toplam_bos_sayi.show()
        self.toplam_soru_sayi.show()
        self.ortalama_sayi.show()

        self.Yildiz1Tablosu.show()
        self.Yildiz2Tablosu.show()
        self.Yildiz3Tablosu.show()
        self.Yildiz4Tablosu.show()
        self.Yildiz5Tablosu.show()
        self.Yildiz6Tablosu.show()
        self.EzberlenmisTablosu.show()

    def Ayarlar(self):
        self.SinavAnaMenuGeriGitme.show()

        self.ing.show()
        self.tr.show()

        self._5.show()
        self._10.show()
        self._15.show()
        self._20.show()

        self.AyarlarSoruSayisiKismi.show()
        self.AyarlarDilKismi.show()

    def SinavSonuAnaliz(self):
        self.SinavAnaMenuGeriGitme.show()

        self.yazi_dogru.show()
        self.yazi_yanlis.show()
        self.yazi_bos.show()
        self.yazi_toplam.show()
        self.yazi_dogru_sayi.show()
        self.yazi_yanlis_sayi.show()
        self.yazi_bos_sayi.show()
        self.yazi_toplam_sayi.show()

    def Kelimeler(self):
        self.SinavAnaMenuGeriGitme.show()
        self.KelimelerTablosu.show()