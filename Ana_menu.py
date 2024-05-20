from ButonOlustur import *
from TextBoxOlustur import *
from ShowHide import *
from LabelOlustur import *
from Siklar import *
from Siklik import *
from MetinSesButon import *
from SinavSonuAnaliz import *

from gtts import gTTS
from playsound import playsound
import sqlite3
import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap


locale.setlocale(locale.LC_ALL, 'turkish')


class Ana_Pencere123(QWidget):
    def __init__(self):
        super().__init__()

        self.sinav_soru_sayisi = 5
        self.bos_sayisi = 0
        self.sorular = [0] * 21
        self.sikler = [0] * 21
        self.soru_sayaci = 1
        self.sayac = 1

        self.setWindowTitle("Kelime Ezberleme Modülü")
        self.setStyleSheet("background-color: #3c64c8 ")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(1200, 600)

        self.kontrol()

        LabelOlustur.Olustur(self)
        TextBoxOlustur.Olustur(self)
        ButonOlustur.Olustur(self)
        SiklikOlustur.Olustur(self)
        SiklarOlustur.Olustur(self)
        MetinSesButonOlustur.Olustur(self)
        SinavSonuAnaliz.Olustur(self)

        ShowHide.hepsini_gizleme(self)

        pixmap = QPixmap("program/kapalı2.png")
        self.label_resim_soru.setPixmap(pixmap)
        self.label_resim_soru.setScaledContents(True)

        pixmap = QPixmap("program/açık1.png")
        self.label_resim_A.setPixmap(pixmap)
        self.label_resim_A.setScaledContents(True)

        pixmap = QPixmap("program/açık2.png")
        self.label_resim_B.setPixmap(pixmap)
        self.label_resim_B.setScaledContents(True)

        pixmap = QPixmap("program/kapalı1.png")
        self.label_resim_C.setPixmap(pixmap)
        self.label_resim_C.setScaledContents(True)

        ShowHide.giris(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def kontrol(self):
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

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def geri_giris(self):
        self.temizle()
        ShowHide.hepsini_gizleme(self)

        ShowHide.giris(self)

    def giris(self):
        self.temizle()
        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_ana_menu(self)

        """username = self.line_edit_kullanici_adi.text()
        password = self.line_edit_sifre.text()

        if username and password:
            conn = sqlite3.connect("database/KullaniciBilgileri.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi = ? AND sifre = ?", (username, password))
            user = cursor.fetchone()

            if user:
                self.temizle()
                ShowHide.hepsini_gizleme(self)
                ShowHide.sinav_ana_menu(self)
            else:
                self.label_giris.setText("Kullanıcı Adı Veya Şifre Yanlış. Tekrar Deneyiniz.")
            conn.close()
        else:
            self.label_giris.setText("Lütfen Bilgileri Eksiksiz Giriniz")"""

    def sifre_unuttum(self):
        self.temizle()
        ShowHide.hepsini_gizleme(self)
        ShowHide.sifre_unuttum(self)

    def kayit(self):
        self.temizle()
        ShowHide.hepsini_gizleme(self)
        ShowHide.kayit(self)

    """"""""""""""""""""""""

    def sifre_goster_gizle(self):
        sender = self.sender()
        if sender.isChecked():
            self.line_edit_sifre.setEchoMode(QLineEdit.Normal)
        else:
            self.line_edit_sifre.setEchoMode(QLineEdit.Password)

    def kaydol(self):
        isim = self.line_edit_isim.text()
        soyisim = self.line_edit_soyisim.text()
        kullaniciadi = self.line_edit_kaydol_kullanici_adi.text()
        sifre = self.line_edit_kaydol_sifre.text()

        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi=?", (kullaniciadi,))
        kullanici = cursor.fetchone()

        if kullanici:
            self.label_giris.setText("Bu Kullanıcı Adı Zaten Kullanımda. Farklı Bir Kullanıcı Adı Giriniz.")
        else:
            cursor.execute("INSERT INTO kullanicilar (isim, soyisim, kullaniciadi, sifre) VALUES (?, ?, ?, ?)",(isim, soyisim, kullaniciadi, sifre))
            conn.commit()
            conn.close()

            if isim and soyisim and sifre and kullaniciadi:
                self.temizle()
                self.label_giris.setText("Kayıt İşlemi Başarılı! Giriş İçin Ana Menüye Dönünüz.")
            else:
                self.label_giris.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    def sifre_getir(self):
        username = self.line_edit_sifre_kullanici_adi.text()

        if username:
            conn = sqlite3.connect("database/KullaniciBilgileri.db")
            cursor = conn.cursor()
            cursor.execute("SELECT sifre FROM kullanicilar WHERE kullaniciadi = ?", (username,))
            row = cursor.fetchone()

            if row:
                self.label_giris.setText("Şifreniz = \" " + row[0] + " \"")
            else:
                self.label_giris.setText("Kullanıcı Bulunamadı. Tekrar Deneyiniz.")

            conn.close()
        else:
            self.label_giris.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def cikis(self):
        QApplication.quit()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def geri_sinav(self):
        self.temizle()

        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_ana_menu(self)

    def sinav(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_sayfasi_once(self)
        print("sinav sayfası")

    def soru_ekleme(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.soru_ekleme(self)
        print("soru ekleme")

    def analiz(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.analiz(self)
        print("analiz")

    def ayarlar(self):
        self.button_group.setExclusive(False)
        self.__dict__[f"_{self.sinav_soru_sayisi}"].setChecked(True)
        self.button_group.setExclusive(True)
        ShowHide.hepsini_gizleme(self)
        ShowHide.ayarlar(self)
        print("ayarlar")

    """"""""""""""""""""""""

    def soru_basla(self):
        self.soru_sayaci = 1
        self.secim_kaldir()
        self.sorular = [0] * 21
        self.sikler = [0] * 21
        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_sayfasi_sonra(self)
        self.label_sinav_sayac.setText(f"{self.soru_sayaci}")

    def sonraki_soru(self):
        if self.soru_sayaci < self.sinav_soru_sayisi:
            if str(self.sikler[self.soru_sayaci + 1]) == '0':
                self.secim_kaldir()
            else:
                attribute_to_set = getattr(self, str(self.sikler[self.soru_sayaci + 1]))
                attribute_to_set.setChecked(True)

            if self.soru_sayaci + 1 == self.sinav_soru_sayisi:
                self.buton_sonraki_soru.hide()
                self.buton_sinav_bitir.show()

            if self.soru_sayaci > 0:
                self.buton_önceki_soru.show()

            self.soru_sayaci += 1
            self.label_sinav_sayac.setText(f"{self.soru_sayaci}")

    def onceki_soru(self):
        if self.soru_sayaci > 1:
            if str(self.sikler[self.soru_sayaci - 1]) == '0':
                self.secim_kaldir()
            else:
                attribute_to_set = getattr(self, str(self.sikler[self.soru_sayaci - 1]))
                attribute_to_set.setChecked(True)

            if self.soru_sayaci == 2:
                self.buton_önceki_soru.hide()

            if self.soru_sayaci - 1 < self.sinav_soru_sayisi:
                self.buton_sonraki_soru.show()
                self.buton_sinav_bitir.hide()

            self.soru_sayaci -= 1
            self.label_sinav_sayac.setText(f"{self.soru_sayaci}")

    def soru_ekle(self):
        ingilizce = self.line_edit_kelime_ingilizce.text()
        turkce = self.line_edit_kelime_turkcesi.text()
        cumle1 = self.line_edit_cümle1.text()
        cumle2 = self.line_edit_cümle2.text()

        if ingilizce and turkce and cumle1 and cumle2:
            self.label_sinav_sayac.setText("Başarıyla eklenmiştir.")
        else:
            self.label_sinav_sayac.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    def resim_sec(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "","Resim Dosyaları (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.label_ekleme_resim.setPixmap(pixmap.scaled(self.label_ekleme_resim.size(), aspectRatioMode=True))
            self.label_ekleme_resim.setScaledContents(True)

    def sinav_sonu_analiz(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_sonu_analiz(self)
        self.temizle()

        for bos_sayac in range(self.sinav_soru_sayisi):
            if str(self.sikler[bos_sayac + 1]) == '0':
                self.bos_sayisi += 1

        self.yazi_bos_sayi.setText(str(self.bos_sayisi))


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def temizle(self):
        self.label_giris.setText("")
        self.label_sinav_sayac.setText("")
        self.label_ekleme_resim.setPixmap(QPixmap())
        self.label_ekleme_resim.setScaledContents(False)

        self.line_edit_kullanici_adi.clear()
        self.line_edit_sifre.clear()
        self.line_edit_isim.clear()
        self.line_edit_soyisim.clear()
        self.line_edit_kaydol_kullanici_adi.clear()
        self.line_edit_kaydol_sifre.clear()
        self.line_edit_sifre_kullanici_adi.clear()

    def secim_kaldir(self):
        self.button_group1.setExclusive(False)
        self.A.setChecked(False)
        self.B.setChecked(False)
        self.C.setChecked(False)
        self.button_group1.setExclusive(True)

    def siklari_kaydet(self):
        sender_button = self.sender()
        bilgi = sender_button.property("bilgi")

        self.sikler[self.soru_sayaci] = bilgi
        self.sorular[self.soru_sayaci] = self.sinav_soru.text()

    def soru_sayi_degistir(self):
        sender = self.sender()
        self.sinav_soru_sayisi = int(sender.text())
        self.yazi_toplam_sayi.setText(str(self.sinav_soru_sayisi))

    def seslendirme(self, pos):
        corrected_pos = pos - QPoint(160, 0)
        buton_metni = self.childAt(corrected_pos).text()

        if corrected_pos.y() > 100:
            language = 'tr'
        else:
            language = 'en'

        cikti = gTTS(text=buton_metni, lang=language, slow=False)
        cikti.save("dosya/ses" + str(self.sayac) + ".mp3")
        playsound("dosya/ses" + str(self.sayac) + ".mp3")
        self.sayac += 1




if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = Ana_Pencere123()
    giris_sayfasi.show()
    sys.exit(app.exec_())