from AnaButonlar import *
from MetinselAraclar import *
from ShowHide import *
from Analizler import *
from TabloOlustur import *

from gtts import gTTS
from playsound import playsound
import os, sys, random, sqlite3, cv2
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from datetime import datetime
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

locale.setlocale(locale.LC_ALL, 'turkish')

class Ana_Pencere123(QWidget):
    def __init__(self):
        super().__init__()

        self.BaslatilmaIslemleri()

        #PROJENİN ÇALIŞACAĞI UYGULAMA PENCERESİ OLUŞTURULUYOR.

        self.setWindowTitle("Kelime Ezberleme Modülü")
        self.setStyleSheet("background-color: #1E468F")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(1200, 600)

        #METİNLERİN GELECEĞİ YERLER OLUŞTURUKUYOR.
        MetinselAraclar.UyariMetinGirisleri(self)
        MetinselAraclar.KelimeEklemeSayfasiMetinGirisleri(self)
        MetinselAraclar.GirisSayfasiMetinGirisleri(self)
        MetinselAraclar.SoruMetinGirisleri(self)
        MetinselAraclar.BilgilendirmeMetinGirisleri(self)

        #UYGULAMADAKİ İŞLEMLERİ SAĞLAYAN BUTONLAR OLUŞTURULUYOR
        ButonOlustur.GirisMenuButonlari(self)
        ButonOlustur.GirisMenuIcIslemButonlari(self)
        ButonOlustur.SinavAnaMenuButonlari(self)
        ButonOlustur.SinavMenuIcIslemButonlari(self)
        ButonOlustur.SinavSikButonlari(self)
        ButonOlustur.AyarlarSoruSayisiSecmeButonlari(self)
        ButonOlustur.MetinleriSeslendirmeButonlari(self)
        ButonOlustur.SoruDilDegistirButonlari(self)

        #ANALİZ KISMINDAKİ KELİMELERİN YAZILACAĞI TABLOLAR OLUŞTURULUYOR.
        TabloOlustur.KelimelerTablosu(self)
        TabloOlustur.Yildiz1TablosuOlustur(self)
        TabloOlustur.Yildiz2TablosuOlustur(self)
        TabloOlustur.Yildiz3TablosuOlustur(self)
        TabloOlustur.Yildiz4TablosuOlustur(self)
        TabloOlustur.Yildiz5TablosuOlustur(self)
        TabloOlustur.Yildiz6TablosuOlustur(self)
        TabloOlustur.EzberlenmisTablosuOlustur(self)

        #ANALİZ KISIMLARININ ARAÇLARI OLUŞTURULUYOR.
        Analizler.AnaAnalizSayfasi(self)
        Analizler.SinavSonuAnalizSayfasi(self)

        #GİRİŞ KISMI EKRANA GELECEĞİ İÇİN ONUNLA UYGULAMA BAŞLATILIYOR
        self.SayfalaraYonlendir("GirisAnaMenu")
        self.GenelIslemleriSifirla()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def SayfalaraYonlendir(self, SayfaAdi):
        #SHOWHİDE KISMINDAKİ FONKSİYONA ULAŞILIYOR
        ShowHide.TumAraclariGizle(self)
        ShowHide.__dict__[f"{SayfaAdi}"](self)

        #SAYFA OLUŞTURMA DIŞINDADA İŞLEMİ OLANLAR İÇİN KOŞULA GÖRE EYLEMLER SAĞLANIYOR.
        self.GenelIslemleriSifirla()
        if SayfaAdi == "SinavaBaslamaSonrasi":
            self.SoruOlustur()
        if SayfaAdi == "SinavSonuAnaliz":
            self.SinavSonuAnaliz()
        if SayfaAdi == "Ayarlar":
            #AYARLAR KISMINDA VARSAYILAN OLARAK SEÇİLECEK TUŞLAR AYARLANIYOR
            self.AyarlarDilDegistir.setExclusive(False)
            self.__dict__[f"{self.dil}"].setChecked(True)
            self.AyarlarDilDegistir.setExclusive(True)
            self.AyarlarSoruSayisi.setExclusive(False)
            self.__dict__[f"_{self.kullan_soru_sayisi}"].setChecked(True)
            self.AyarlarSoruSayisi.setExclusive(True)
            ShowHide.Ayarlar(self)
        if SayfaAdi == "AnalizSayfasi":
            self.AnalizSayfasi()
        if SayfaAdi == "Kelimeler":
            self.KelimelerTablosunaKelimeleriKoy()
    def VeritabaniKontrolEt(self):
        #VERİTABANININ OLUP OLMADIĞI KONTROL EDİLİYOR.
        if os.path.exists("database/KullaniciBilgileri.db"):
            return True
        else:
            conn = sqlite3.connect("database/KullaniciBilgileri.db")
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE kullanicilar (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                isim TEXT NOT NULL,
                                soyisim TEXT NOT NULL,
                                kullaniciadi TEXT UNIQUE NOT NULL,
                                sifre CHAR(50) NOT NULL
                              )''')

            conn.commit()
            conn.close()

    def Cikis(self):
        #UYGULMAYI KAPATIYOR
        QApplication.quit()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    ###GİRİŞ MENÜSÜNÜN İÇERİKLERİ
    def GirisButonunaBasildi(self):
        #GİRİŞ KISMINDA YAZILAN BİLGİLER ALINIYOR
        username = self.GirisKismiKullaniciAdi.text()
        password = self.GirisKismiSifre.text()

        if username and password:
            conn = sqlite3.connect("database/KullaniciBilgileri.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi = ? AND sifre = ?", (username, password))
            user = cursor.fetchone()
            conn.close()

            if user:
                #KULLANICI VARSA VE ŞİFRESİ DOĞRUYSA GEÇİŞ ONAYLANIYOR
                self.kullanici_id = user[0]
                ShowHide.TumAraclariGizle(self)
                ShowHide.SinavUygulamasiAnaMenu(self)
            else:
                #ŞİFRE YANLIŞSA UYARI VERİYOR
                self.GirisKismiUyariMesaji.setText("Kullanıcı Adı Veya Şifre Yanlış. Tekrar Deneyiniz.")
        else:
            #EKSİK BİLGİ GİRİLİRSE HATA VERİYOR
            self.GirisKismiUyariMesaji.setText("Lütfen Bilgileri Eksiksiz Giriniz.")

    def SifreUnuttumButonunaBasildi(self):
        #ŞİFRESİNİ UNUTAN KULLANICININ KULLANICI ADI ALINIYOR
        username = self.SifremiUnuttumKismiKullaniciAdi.text()

        if username:
            conn = sqlite3.connect("database/KullaniciBilgileri.db")
            cursor = conn.cursor()
            cursor.execute("SELECT sifre FROM kullanicilar WHERE kullaniciadi = ?", (username,))
            row = cursor.fetchone()

            if row:
                #KULLANICI VARSA ŞİFREYİ EKRANA YAZIYOR.
                self.GirisKismiUyariMesaji.setText("Şifreniz = \" " + row[0] + " \"")
            else:
                #KULLANICI YOKSA UYARI VERİYOR
                self.GirisKismiUyariMesaji.setText("Kullanıcı Bulunamadı. Tekrar Deneyiniz.")

            conn.close()
        else:
            #BİLGİ EKSİKSE UYARI VERİYOR
            self.GirisKismiUyariMesaji.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    def KayitButonunaBasildi(self):
        #KAYIT OLMAK İSTEYEN KULLANICININ BİLGİLERİ ALINIYORZ
        isim = self.KayitKismiIsim.text()
        soyisim = self.KayitKismiSoyisim.text()
        kullaniciadi = self.KayitKismiKullaniciAdi.text()
        sifre = self.KayitKismiSifre.text()

        if not isim or not soyisim or not kullaniciadi or not sifre:
            #EKSİK BİLGİ GİRİLİNCE UYARI MESAJI VERİYOR
            self.GirisKismiUyariMesaji.setText("Lütfen Bilgileri Eksiksiz Giriniz.")
        elif len(sifre) < 8:
            #ŞİFRENİN 10 KARAKTERDEN UZUN OLMASI İSTENİYOR
            self.GirisKismiUyariMesaji.setText("Şifre en az 10 karakter uzunluğunda olmalıdır.")
        else:
            conn = sqlite3.connect('database/KullaniciBilgileri.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi=?", (kullaniciadi,))
            kullanici = cursor.fetchone()

            if kullanici:
                #VERİTABANINDA KULLANICI ADI KONTROL EDİLİYOR, AYNI VARSA UYARI MESAJI VERİLİYOR
                self.GirisKismiUyariMesaji.setText("Bu Kullanıcı Adı Zaten Kullanımda. Farklı Bir Kullanıcı Adı Giriniz.")
            else:
                #YOKSA YENİ KULLANICI EKLENİYOR
                cursor.execute("INSERT INTO kullanicilar (isim, soyisim, kullaniciadi, sifre) VALUES (?, ?, ?, ?)",
                               (isim, soyisim, kullaniciadi, sifre))
                #YENİ KULLANICI OLDUĞU İÇİN İSTATİSTİKLERİ 0 OLARAK GİRİLİYOR
                cursor.execute("INSERT INTO Kullaniciİstatistik (dogru_cevaplar, yanlis_cevaplar, bos_cevaplar, toplam_sorular) VALUES (0, 0, 0, 0)")

                conn.commit()
                conn.close()

        self.GenelIslemleriSifirla()
        self.GirisKismiUyariMesaji.setText("Kayıt İşlemi Başarılı! Giriş İçin Ana Menüye Dönünüz.")
        #BAŞARILI OLDUĞUNA DAİR UYARI MESAJI VERİLİYOR.

    def SifreGosterGizle(self):
        #ŞİFRENİN * YADA NORMAL GÖSTERİLMESİ AYARLANIYOR
        SifreGosterGizleButonu = self.sender()
        if SifreGosterGizleButonu.isChecked():
            self.GirisKismiSifre.setEchoMode(QLineEdit.Normal)
        else:
            self.GirisKismiSifre.setEchoMode(QLineEdit.Password)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    ### SİNAV MENÜSÜ İÇERİKLERİ
    def Ayarlar(self):
        #AYARLAR KISMINDA TIKLANILAN BUTONA GÖRE SORU SAYISI YADA DİL DEĞİŞİKLİĞİ YAPILIYOR
        TiklananButon = self.sender()
        if len(TiklananButon.text()) < 3:
            self.sinav_soru_sayisi = int(TiklananButon.text())
            self.kullan_soru_sayisi = self.sinav_soru_sayisi
            self.yazi_toplam_sayi.setText(str(self.sinav_soru_sayisi))
        else:
            bilgi = TiklananButon.property("bilgi")
            self.dil = str(bilgi)

    def AnalizSayfasi(self):
        #KULLANICININ BİLDİĞİ KELİMELER VE SAYISAL ANALİZLERİNİ GÖRÜNTÜLEDİĞİ SAYFA
        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Kullaniciİstatistik WHERE kullanici_id = ?;', (self.kullanici_id,))
        KullaniciIstatistikleri = cursor.fetchone()
        conn.commit()
        conn.close()

        #KULLANICININ VERİLERİ ALINIYOR VE EKRANA YAZILIYOR
        self.toplam_dogru_sayi.setText("" + str(KullaniciIstatistikleri[1]))
        self.toplam_yanlis_sayi.setText("" + str(KullaniciIstatistikleri[2]))
        self.toplam_bos_sayi.setText("" + str(KullaniciIstatistikleri[3]))
        self.toplam_soru_sayi.setText("" + str(KullaniciIstatistikleri[4]))

        #STRİNG İFADE İSTEDİĞİ İÇİN KAYIT YOKSA 0 YAZDIRIYORUZ
        if KullaniciIstatistikleri[1] == 0:
            self.ortalama_sayi.setText("ORTALAMA : %00.00")
        else:
            self.ortalama_sayi.setText(
                "%" + str("{:.2f}".format((KullaniciIstatistikleri[1] / KullaniciIstatistikleri[4]) * 100)))

        #KULLANICININ DAHA ÖNCE BİLDİĞİ KELİMELER ALINIYOR
        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('SELECT kelime, bilinen FROM KullaniciBilinen WHERE kullanici_id = ?;',
                       (self.kullanici_id,))
        kullanici_bilinen = cursor.fetchall()

        bilinen_sozluk = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

        #BİR SÖZLÜĞE AKTARILIYOR
        for kelime, bilinen in kullanici_bilinen:
            if bilinen in bilinen_sozluk:
                bilinen_sozluk[bilinen].append(kelime)
        #sÖZLÜKTEN TABLOYA YAZILIYOR
        for bilinen_seviye, kelime_listesi in bilinen_sozluk.items():
            Tablo = getattr(self, f"Yildiz{bilinen_seviye}Tablosu", None)
            Tablo.setRowCount(0)
            current_row_count = 0
            Tablo.setRowCount(current_row_count + len(kelime_listesi))
            for index, kelime in enumerate(kelime_listesi):
                item = QTableWidgetItem(str(kelime))
                item.setTextAlignment(Qt.AlignCenter)
                Tablo.setItem(current_row_count + index, 0, item)

        #KULLANICININ TAMAMEN BİLDİĞİ KELİME VARSA EZBERLENMİŞ KISMINDA GÖZÜKMESİ SAĞLANIYOR
        cursor.execute('SELECT kelime FROM KaliciBilinen WHERE kullanici_id = ?;', (self.kullanici_id,))
        kalici_bilinen = cursor.fetchall()

        #TABLOYA YAZDIRILIYOR
        if kalici_bilinen:
            self.EzberlenmisTablosu.setRowCount(0)
            current_row_count = 0
            self.EzberlenmisTablosu.setRowCount(len(kalici_bilinen))
            for index, kelime in enumerate(kalici_bilinen):
                item = QTableWidgetItem(str(kelime[0]))
                item.setTextAlignment(Qt.AlignCenter)
                self.EzberlenmisTablosu.setItem(current_row_count + index, 0, item)
        else:
            self.EzberlenmisTablosu.setRowCount(0)

        conn.close()

    def SinavSonuAnaliz(self):
        #SINAV SONUNDA SORU SAYISINA GÖRE SORULARIN DOĞRU/YANLIŞ/BOŞ VERİLERİ OLUŞTURULUYOR.
        for sayac in range(self.kullan_soru_sayisi):
            if self.SinavSiklariKaydet[sayac + 1][0] == 0:
                #BOŞ OLDUĞU BELİRLENDİ BOŞ SORU SAYISI ARTTIRILIYOR
                self.test_bos_cevap_sayisi += 1
            else:
                if str(self.SinavSiklariKaydet[sayac + 1][1]) == str(self.Sorular[sayac]["cevabı"]):
                    #DOĞRU OLDUĞU BELİRLENDİ DOĞRU SAYISI ARTTIRILIYOR
                    self.test_dogru_cevap_sayisi += 1

                    conn = sqlite3.connect('database/KullaniciBilgileri.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        'SELECT bilinen, tarih, kelime_id, kelime FROM KullaniciBilinen WHERE kullanici_id = ? AND kelime = ?',
                        (self.kullanici_id, self.Sorular[sayac]["kelime"],))
                    islem = cursor.fetchone()
                    #KELİMENİN ÇIKMA ARALIĞINI BELİRLEMEK İÇİN VERİTABANINDAN KONTROLÜ SAĞLANIYOR
                    if islem:
                        #KELİME DAHA ÖNCE DOĞRU BİLİNMİŞ
                        bilinen = islem[0]
                        bilinen += 1
                        if bilinen == 7:
                            #HERHANGİ BİR KELİMENİN TOPLAM DOĞRU BİLME SEVİYESİNE ULAŞTIĞI ZAMAN KALICI OLARAK BİLİNMİŞ SAYILIYOR
                            cursor.execute("INSERT INTO KaliciBilinen VALUES (?, ?, ?)",
                                           (self.kullanici_id, islem[2], islem[4]))
                            #VE NORMAL BİLİNME YERİNDEN SİLİNİYOR
                            cursor.execute('DELETE FROM KullaniciBilinen WHERE kullanici_id = ? AND kelime_id = ?',
                                           (self.kullanici_id, islem[2], islem[3]))
                        else:
                            #SON BİLİNME SEVİYESİNE ULAŞMAMIŞ KELİMELER BİR SONRAKİ GÖZÜKECEK TARİH VE BİLİNME GÜNCELLEMESİNİ ALIYOR
                            tarih = islem[1]
                            #YENİ TARİH OLUŞTURULUYOR
                            gun_ekle = {1: 1, 2: 3, 3: 7, 4: 0, 5: 0, 6: 0}
                            ay_ekle = {1: 0, 2: 0, 3: 0, 4: 1, 5: 6, 6: 0}
                            yil_ekle = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}
                            gun, ay, yil = map(int, tarih.split('.'))
                            gun += gun_ekle.get(bilinen, 0)
                            ay += ay_ekle.get(bilinen, 0)
                            yil += yil_ekle.get(bilinen, 0)
                            #OLUŞTURULAN TARİH AYIN SON GÜNÜNE YADA YILIN SON GÜNÜNE DENK GELEBİLİR BUNUN AYARLAMASI YAPILIYOR
                            while gun > 30:
                                gun -= 30
                                ay += 1
                            while ay > 12:
                                ay -= 12
                                yil += 1
                            #YENİ TARİH OLUŞTURULUYOR VE VERİTABANINDA GÜNCELLENİYOR
                            yeni_tarih = (f"{gun}.{ay}.{yil}")
                            cursor.execute(
                                'UPDATE KullaniciBilinen SET bilinen = ?, tarih = ? WHERE kullanici_id = ? AND kelime_id = ?',
                                (bilinen, yeni_tarih, self.kullanici_id, islem[2]))
                    else:
                        #KELİME 1. BİLİNME SEVİYESİNDE İSE NORMAL EKLEME İŞLEMİ YAPILIYOR
                        tarih = datetime.now().strftime('%x')
                        gun, ay, yil = map(int, tarih.split('.'))
                        yeni_tarih = f"{gun + 1}.{ay}.{yil}"
                        #TARİH, ÇIKACAĞI GÜN OLDUĞU İÇİN BİR SONRAKİ GÜN OLARAK EKLENİYOR
                        cursor.execute('INSERT INTO KullaniciBilinen VALUES (?, ?, ?, ?, ?)',
                                       (self.kullanici_id, self.Sorular[sayac]["id"], 1, self.Sorular[sayac]["kelime"],
                                        yeni_tarih))
                    conn.commit()
                    conn.close()
                else:
                    #YANLIŞ OLDUĞU BELİRLENDİ YANLIŞ SAYISI ARTTIRILDI
                    self.test_yanlis_cevap_sayisi += 1

        #SINAV SONUNDAKİ ANALİZ KISMINDA GÖRÜNTÜLENMESİ İÇİN EKLENDİ
        self.yazi_dogru_sayi.setText(str(self.test_dogru_cevap_sayisi))
        self.yazi_yanlis_sayi.setText(str(self.test_yanlis_cevap_sayisi))
        self.yazi_bos_sayi.setText(str(self.test_bos_cevap_sayisi))
        self.yazi_toplam_sayi.setText(str(self.sinav_soru_sayaci))

        #VERİTABANINDA GÜNCELLENDİ
        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Kullaniciİstatistik 
                SET dogru_cevaplar = dogru_cevaplar + ?, yanlis_cevaplar = yanlis_cevaplar + ?, bos_cevaplar = bos_cevaplar + ?, toplam_sorular = toplam_sorular + ?
                WHERE kullanici_id = ?''', (
            self.test_dogru_cevap_sayisi, self.test_yanlis_cevap_sayisi, self.test_bos_cevap_sayisi,
            self.sinav_soru_sayaci,
            self.kullanici_id))

        conn.commit()
        conn.close()

        #SORU SAYISI ESKİ HALİNE GETİRİLDİ
        self.kullan_soru_sayisi = self.sinav_soru_sayisi

    def AnalizleriYazdir(self):
        #ANALİZLERİN PDF DOSYASINA YAZDIRILMA İŞLEMİ
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])

        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Kullaniciİstatistik WHERE kullanici_id = ?;', (self.kullanici_id,))
        kullanici_verileri = cursor.fetchone()
        #DOĞRU/YANLIŞ/BOŞ/TOPLAM SORU/ORTALAMA GİBİ DEĞERLER VERİTABNINDAN ALINIP PDF DOSYASINA YAZDIRLIYOR
        c = canvas.Canvas(file_path, pagesize=letter)
        c.setFont("Helvetica", 16)
        c.drawString(250, 750, "- ANALIZ -")
        c.drawString(15, 720,
                     "Toplam Dogru Sayisi : " + str(kullanici_verileri[1]) + "    Toplam Yanlis Sayisi : " + str(
                         kullanici_verileri[2]) + "    Toplam Bos Sayisi : " + str(kullanici_verileri[3]))
        c.drawString(115, 690, "Toplam Soru Sayisi : " + str(kullanici_verileri[4]) + "    Ortalama : %" + str(
            "{:.2f}".format((kullanici_verileri[1] / kullanici_verileri[4]) * 100)))

        #BİLİNEN KELİMELERİN YILDIZLAR İLE GÖSTERİLMESİ AYARLANIYOR
        for i in range(6, 0, -1):
            c.drawString(-50 + i * 95, 550, '*' * i)

        #KOORDİNATLAR BELİRLENİYOR
        tablo_koordinatlari = {
            f"Yildiz{i}Tablosu": (-50 + i * 95, 500) for i in range(6, 0, -1)
        }

        #TABLODAN VERİLER ALINIYOR VE PDF DOSYASINA YAZILIYOR
        for tablo, (x, y) in tablo_koordinatlari.items():
            veriler = []
            for satir in range(getattr(self, tablo).rowCount()):
                satir_verisi = []
                for sutun in range(getattr(self, tablo).columnCount()):
                    hucre_verisi = getattr(self, tablo).item(satir, sutun).text()
                    satir_verisi.append(hucre_verisi)
                veriler.append(satir_verisi)
            y_pos = y
            for satir in veriler:
                x_pos = x
                for hucre_verisi in satir:
                    c.drawString(x_pos, y_pos, hucre_verisi)
                    x_pos += 100
                y_pos -= 20

        c.save()
        conn.commit()
        conn.close()


    ### SİNAV SORULARI İŞLEMLERİ
    def SoruOlustur(self):
        # SINAV SORULARININ EN BAŞTA OLUŞTURULMASI SAĞLANIYOR
        # GEREKLİ DEĞERLER SIFIRLANIYOR
        self.SinavSiklariSeciminiKaldir()
        self.SinavSiklariKaydet = [[0 for j in range(2)] for i in range(25)]
        self.Sorular = []
        self.sinav_soru_sayaci = 1

        # BULUNAN GÜN ALINIYOR
        tarih = datetime.now().strftime('%x')
        gun, ay, yil = map(int, tarih.split('.'))
        tarih = f"{gun}.{ay}.{yil}"
        # VERİTABANINDA KULLANICIYA GÖRE O GÜN ÇIKMASI GEREKEN SORULAR ALINIYOR
        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('SELECT kelime_id FROM KullaniciBilinen WHERE kullanici_id = ? AND tarih = ?',
                       (self.kullanici_id, tarih,))
        bugun_cikacak_kelimeler = cursor.fetchall()

        # KALICI BİLİNEN SORULAR BİR DAHA ÇIKMAYACAĞI İÇİN ONLAR ES GEÇİLİYOR
        cursor.execute('SELECT kelime_id FROM KaliciBilinen WHERE kullanici_id = ?', (self.kullanici_id,))
        artik_cikmayacak_kelimeler = cursor.fetchall()
        conn.commit()
        conn.close()
        # GEREKLİ DEĞERLER ARTTIRILIYOR
        artik_cikmayacak_kelimeler += bugun_cikacak_kelimeler
        bugun_yazilacak = ["asd"] * len(bugun_cikacak_kelimeler)
        self.kullan_soru_sayisi += len(bugun_cikacak_kelimeler)

        conn = sqlite3.connect("database/Kelimeler.db")
        cursor = conn.cursor()
        for sayac in range(len(bugun_cikacak_kelimeler)):
            # BUGUN ÇIKMASI GEREKEN SORULAR ALINIYOR
            cursor.execute("SELECT * FROM kelimeler WHERE kelime_id = ?", (bugun_cikacak_kelimeler[sayac][0],))
            bugunkiler = cursor.fetchall()
            bugun_yazilacak[sayac] = (bugunkiler[0])

        if len(bugun_cikacak_kelimeler) == 0:
            # ARTIK ÇIKMAYACAK KELİMELER ALINIYOR
            cursor.execute("SELECT * FROM kelimeler ORDER BY RANDOM() LIMIT ?", (self.kullan_soru_sayisi,))
        else:
            # KOŞULLARA BAĞLI OLARAK SORULAR OLUŞTURULUYOR
            for sayac in range(len(artik_cikmayacak_kelimeler)):
                çikmaycak = int(artik_cikmayacak_kelimeler[sayac][0])
                cursor.execute("SELECT * FROM kelimeler WHERE NOT kelime_id = ? ORDER BY RANDOM() LIMIT ?",
                               (çikmaycak, self.kullan_soru_sayisi,))

        rows = cursor.fetchall()
        conn.close()
        bugun_yazilacak += rows

        # BU SORULAR GEREKLİ ŞARTLARA GÖRE TAM SORU İÇERİĞİNİ OLUŞTURMAK İÇİN GELİYOR
        for row in bugun_yazilacak:
            data = list(row)
            id, ingilizce_kelime, turkce_kelime, cumle_ing, cumle_tr, image_path = data
            # DİLE GÖRE DOĞRU CEVAP AYARLANIYOR
            if self.dil == 'tr':
                correct_answer = ingilizce_kelime
                other_answers = [r[1] for r in bugun_yazilacak if r[0] != id]
            else:
                correct_answer = turkce_kelime
                other_answers = [r[2] for r in bugun_yazilacak if r[0] != id]
            wrong_answers = random.sample(other_answers, 2)

            # TÜM ŞIKLAR HEP AYNI YERDE GÖZÜKMESİN DİYE KARIŞTIRMA İŞLEMİ YAPILIYOR
            choices = {"A": None, "B": None, "C": None}
            answers = [correct_answer] + wrong_answers[:2]
            random.shuffle(answers)
            choices["A"], choices["B"], choices["C"] = answers

            # SORUNUN TAMAMI OLUŞTURULUYOR
            if self.dil == 'tr':
                self.SoruAciklamasi.setText("YUKARIDAKİ KELİMENİN İNGİLİZCESİ NEDİR?")
                question = {
                    "id": id,
                    "image_path": image_path,
                    "kelime": turkce_kelime,
                    "cumle": cumle_tr,
                    "choices": choices,
                    "cevabı": ingilizce_kelime
                }
            else:
                self.SoruAciklamasi.setText("YUKARIDAKİ KELİMENİN TÜRKÇESİ NEDİR?")
                question = {
                    "id": id,
                    "image_path": image_path,
                    "kelime": ingilizce_kelime,
                    "cumle": cumle_ing,
                    "choices": choices,
                    "cevabı": turkce_kelime
                }
            self.Sorular.append(question)

        # İLK SORUNUN İÇERİĞİ YAILIYOR YOKSA İLK SORU BOŞ GÖZÜKÜR
        self.SinavSayaci.setText(str(self.sinav_soru_sayaci))
        image = self.Sorular[self.sinav_soru_sayaci - 1]['image_path']
        pixmap = QPixmap(image)
        self.SoruResimKismi.setPixmap(pixmap)
        self.SoruResimKismi.setScaledContents(True)
        self.SoruKelimeYeri.setText(self.Sorular[self.sinav_soru_sayaci - 1]['kelime'])
        self.SoruCümleKismi.setText(self.Sorular[self.sinav_soru_sayaci - 1]['cumle'])
        self.A.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['A'])
        self.B.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['B'])
        self.C.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['C'])

    def SoruDegistir(self, degistirme):
        #SORU SAYISINDA İSTENEN YÖNDEKİ DEĞİŞİM ALINIYOR
        self.sinav_soru_sayaci += int(degistirme)

        #O SIRADAKI SORU EKRANA GELİYOR
        self.SinavSayaci.setText(str(self.sinav_soru_sayaci))
        image = self.Sorular[self.sinav_soru_sayaci - 1]['image_path']
        pixmap = QPixmap(image)
        self.SoruResimKismi.setPixmap(pixmap)
        self.SoruResimKismi.setScaledContents(True)
        self.SoruKelimeYeri.setText(self.Sorular[self.sinav_soru_sayaci - 1]['kelime'])
        self.SoruCümleKismi.setText(self.Sorular[self.sinav_soru_sayaci - 1]['cumle'])
        self.A.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['A'])
        self.B.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['B'])
        self.C.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['C'])

        #EĞER BU SORU DAHA ÖNCE İŞARETLENMİŞSE O ŞIK SEÇİLİ OLARAK GELİYOR
        self.SinavSiklariSeciminiKaldir()
        if str(self.SinavSiklariKaydet[self.sinav_soru_sayaci][0]) != '0':
            self.SinavSiklariGrup.setExclusive(False)
            getattr(self, self.SinavSiklariKaydet[self.sinav_soru_sayaci][2]).setChecked(True)
            self.SinavSiklariGrup.setExclusive(True)

        #SINAVIN SONUNA GELİNCE "SINAVI BİTİR" BUTONU GÖZÜKECEK, SONRAKİ SORU KAYBOLACAK
        if self.sinav_soru_sayaci == self.kullan_soru_sayisi:
            self.SonrakiSoruButonu.hide()
            self.SinavBitirButonu.show()
        else:
            self.SonrakiSoruButonu.show()
            self.SinavBitirButonu.hide()
        #SORU SAYISI 1'SE ÖNCEKİ SORU GÖZÜKMEYECEK
        if self.sinav_soru_sayaci != 1:
            self.ÖncekiSoruButonu.show()
        else:
            self.ÖncekiSoruButonu.hide()
    def SinavSiklariSeciminiKaldir(self):
        #SINAV ŞIKLARININ SEÇİMİNİ KALDIRIR
        self.SinavSiklariGrup.setExclusive(False)
        self.A.setChecked(False)
        self.B.setChecked(False)
        self.C.setChecked(False)
        self.SinavSiklariGrup.setExclusive(True)            

    def SinavSiklariniKaydet(self):
        #SINAV ŞIKLARININ METNİNİ ALIR VE ANALİZ KISMINDA KULLANILMAK ÜZERE KAYDEDER
        TiklananSik = self.sender()
        TiklananSikMetni = TiklananSik.property("bilgi")

        self.SinavSiklariKaydet[self.sinav_soru_sayaci] = (str(self.SoruKelimeYeri.text()), str(getattr(self, TiklananSikMetni).text()), str(TiklananSikMetni))

    def SinavMetinleriniSeslendirma(self, pos):
        #SINAV SORULARININ SESLENDİRMESİ SAĞLANIYOR
        ButonPozisyonu = pos - QPoint(160, 0)
        SeslendirilecekMetin = self.childAt(ButonPozisyonu).text()

        #SEÇİLİ OLAN DİL FARKLI OLACAĞINDAN DOLAYI SESLENDİRME KISMI AYARLANIYOR
        if self.dil == 'tr':
            if ButonPozisyonu.y() > 100:
                language = 'en'
            else:
                language = 'tr'
        else:
            if ButonPozisyonu.y() > 100:
                language = 'tr'
            else:
                language = 'en'
        #SES DOSYASININ ÇALMASI İÇİN BİR İSİM OLUŞTURULUYOR VE KAYDEDİLİYOR.
        RandomSayi = random.randint(1,1111111)
        cikti = gTTS(text=SeslendirilecekMetin, lang=language, slow=False)
        cikti.save("dosya/ses" + str(RandomSayi) + ".mp3")
        #KAYDEDİLEN MEDYA ÇALIŞTIRILIYOR
        playsound("dosya/ses" + str(RandomSayi) + ".mp3")


    ### SİNAV MENÜSÜ İÇ İŞLEMLERİ
    def KelimeEklemeButonuBasildi(self):
        #EKELENECEK KELİMENİN BİLGİLERİ ALINIYOR
        ingilizce_kelime = self.SoruEklemeIngilizce.text()
        turkce_kelime = self.SoruEklemeTurkce.text()
        ingilizce_cumle = self.SoruEklemeIngilizceCumle.text()
        turkce_cumle = self.SoruEklemeTurkceCumle.text()

        if ingilizce_kelime and turkce_kelime and ingilizce_cumle and turkce_cumle:
            #EKSİKSİZ GİRİLİNCE DEVAME EDİLİYOR
            #VERİTABANINDA KELİMEMNİN OLUP OLMADIĞI KONTROL EDİLİYOR
            conn = sqlite3.connect('database/Kelimeler.db')
            cursor = conn.cursor()
            ingilizce_lower = ingilizce_kelime.lower()

            cursor.execute("SELECT * FROM Kelimeler WHERE LOWER(ingilizce_kelime) = ?", (ingilizce_lower,))
            existing_word = cursor.fetchone()

            if existing_word:
                #VARSA UYARI MESAJI VERİLİYOR
                self.KelimeEklemeUyariMesaji.setText("Bu Kelime Zaten Mevcut. Başka Bir Kelime Deneyiniz.")
            else:
                #YOKSA DEVAM EDİLİYOR
                if self.ResimSecmeYapilmasi == 0:
                    #RESİMDE İSTENDİĞİ İÇİN KOŞUL MEKANİZMASI ONA GÖRE İŞLİYOR
                    self.KelimeEklemeUyariMesaji.setText("Lütfen Resim Seçiniz.")
                else:
                    #RESİMDE EKLENDİĞİ İÇİN VERİTABANINA KAYIT YAPILIYOR
                    #RESİM ALINIYOR VE GEREKLİ YERE KAYDEDİLİYOR
                    self.ResimDosyaYolu = 'resim/' + f"{ingilizce_kelime}" + '.png'
                    self.KaydedilecekResim = cv2.resize(self.KaydedilecekResim, (400, 400))
                    cv2.imwrite(self.ResimDosyaYolu, self.KaydedilecekResim)

                    cursor.execute(
                        "INSERT INTO Kelimeler (ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2, resim) VALUES (?, ?, ?, ?, ?)",
                        (ingilizce_kelime, turkce_kelime, ingilizce_cumle, turkce_cumle, self.ResimDosyaYolu))

                    conn.commit()
                    #BAŞARILI OLDUĞUNA DAİR UYARI MESAJI GÖSTERİLİYOR
                    self.KelimeEklemeUyariMesaji.setText("Başarıyla Eklenmiştir.")
                    self.ResimSecmeYapilmasi = 0
        else:
            #EKSİKSİZ GİRİLMESİ İSTENİYOR
            self.KelimeEklemeUyariMesaji.setText("Lütfen Bilgileri Eksiksiz Giriniz")
        self.GenelIslemleriSifirla()

    def ResimSecmeButonuBasildi(self):
        #RESİM SEÇMEK İÇİN GEREKLİ OLAN WİNDOWS PENCERESİ AÇILIYOR
        options = QFileDialog.Options()
        self.DosyaAdi, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "","Resim Dosyaları (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        self.KaydedilecekResim = cv2.imread(self.DosyaAdi)
        if self.DosyaAdi:
            #RESİM SEÇİLDİYSE BUNU ALIYOR
            pixmap = QPixmap(self.DosyaAdi)
            self.KelimeEklemeResimKismi.setPixmap(pixmap.scaled(self.KelimeEklemeResimKismi.size(), aspectRatioMode=True))
            self.KelimeEklemeResimKismi.setScaledContents(True)
            self.ResimSecmeYapilmasi = 1

    def KelimelerTablosunaKelimeleriKoy(self):
        #kELİMELER TABLOSUNA GEREKLİ OLAN VERİLER EKLENİYOR
        conn = sqlite3.connect('database/Kelimeler.db')
        cursor = conn.cursor()
        cursor.execute("SELECT ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2, resim FROM Kelimeler")
        veriler = cursor.fetchall()

        if veriler:
            row_count = len(veriler)
            column_count = len(veriler[0])
            #TABLONUN GENEL BOYUTU BELİRLENİYOR
            self.KelimelerTablosu.setRowCount(row_count)
            self.KelimelerTablosu.setColumnCount(column_count)
            
            #EKLEME İŞLEMİNE BAŞLANIYOR
            for row_index, row_data in enumerate(veriler):
                for column_index, data in enumerate(row_data):
                    if column_index == 4:
                        label = QLabel()
                        pixmap = QPixmap(data)
                        if not pixmap.isNull():
                            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
                            label.setPixmap(pixmap)
                        label.setAlignment(Qt.AlignCenter)
                        self.KelimelerTablosu.setCellWidget(row_index, column_index, label)
                    else:
                        item = QTableWidgetItem(str(data))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.KelimelerTablosu.setItem(row_index, column_index, item)
                self.KelimelerTablosu.setRowHeight(row_index, 120)

        conn.close()

    ### GENEL FONKSİYONLAR
    def BaslatilmaIslemleri(self):
        #BAŞLARKEN TANIMLANMASI GEREKNE VERİLERDİR.
        self.ResimSecmeYapilmasi = 0
        self.sinav_soru_sayisi = 5
        self.kullan_soru_sayisi = self.sinav_soru_sayisi
        self.dil = 'ing'
        self.SinavSiklariKaydet = [[0 for j in range(2)] for i in range(25)]
        self.VeritabaniKontrolEt()
    def GenelIslemleriSifirla(self):
        #GEREKLİ OLAN VERİLERİN SIFIRLANMASI İÇİN YAPILDI
        #AKSİ HALDE YAZILI METİN GİTMEZ, SORU SAYISI DÜZGÜN ÇALIŞMAZ
        self.test_dogru_cevap_sayisi = 0
        self.test_yanlis_cevap_sayisi = 0
        self.test_bos_cevap_sayisi = 0

        self.GirisKismiUyariMesaji.setText("")
        self.SinavSayaci.setText("")
        self.yazi_dogru_sayi.setText("")
        self.yazi_yanlis_sayi.setText("")
        self.KelimeEklemeResimKismi.setPixmap(QPixmap())
        self.KelimeEklemeResimKismi.setScaledContents(False)

        self.GirisKismiKullaniciAdi.clear()
        self.GirisKismiSifre.clear()
        self.KayitKismiIsim.clear()
        self.KayitKismiSoyisim.clear()
        self.KayitKismiKullaniciAdi.clear()
        self.KayitKismiSifre.clear()
        self.SifremiUnuttumKismiKullaniciAdi.clear()

        self.SoruEklemeIngilizce.clear()
        self.SoruEklemeTurkce.clear()
        self.SoruEklemeIngilizceCumle.clear()
        self.SoruEklemeTurkceCumle.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = Ana_Pencere123()
    giris_sayfasi.show()
    sys.exit(app.exec_())