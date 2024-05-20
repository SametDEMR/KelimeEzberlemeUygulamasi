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
import os, sys, random
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
import cv2


locale.setlocale(locale.LC_ALL, 'turkish')


class Ana_Pencere123(QWidget):
    def __init__(self):
        super().__init__()

        self.sinav_soru_sayisi = 5

        self.dogru_sayisi = 0
        self.yanlis_sayisi = 0
        self.bos_sayisi = 0

        self.soru_sayaci = 0
        self.soru_kalip = [[0 for j in range(5)] for i in range(21)]
        self.soru_sik2 = [[0 for j in range(6)] for i in range(21)]
        self.sikler = [[0 for j in range(2)] for i in range(21)]

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

    def soru_ekleme(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.soru_ekleme(self)

    def analiz(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.analiz(self)

    def ayarlar(self):
        self.button_group.setExclusive(False)
        self.__dict__[f"_{self.sinav_soru_sayisi}"].setChecked(True)
        self.button_group.setExclusive(True)
        ShowHide.hepsini_gizleme(self)
        ShowHide.ayarlar(self)

    """"""""""""""""""""""""

    def sonraki_soru(self):
        if self.soru_sayaci == 0:
            ShowHide.hepsini_gizleme(self)
            ShowHide.sinav_sayfasi_sonra(self)

            conn = sqlite3.connect('database/Kelimeler.db')
            cursor = conn.cursor()

            cursor.execute('SELECT resim, ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2 FROM Kelimeler')
            soru_kalip = cursor.fetchall()
            random_kalip = random.sample(soru_kalip, 20)

            self.sayac = 1
            for random_resim, random_ingilizce, random_turkce, random_cümle1, random_cümle2 in random_kalip:
                self.soru_kalip[self.sayac][0] = random_resim
                self.soru_kalip[self.sayac][1] = random_ingilizce
                self.soru_kalip[self.sayac][2] = random_turkce
                self.soru_kalip[self.sayac][3] = random_cümle1
                self.soru_kalip[self.sayac][4] = random_cümle2
                self.sayac += 1

            conn.close()

        self.soru_sayaci += 1
        self.label_sinav_sayac.setText(f"{self.soru_sayaci}")

        self.cümle_soru.setText(f"{self.soru_kalip[self.soru_sayaci][3]}")

        random_sayi1 = random.randint(1, 20)
        random_sayi2 = random.randint(1, 20)

        options_indices = [self.soru_sayaci, random_sayi1, random_sayi2]
        text_indices = [self.soru_sayaci, random_sayi1, random_sayi2]
        random_index = random.randint(0, 2)

        if str(self.soru_sik2[self.soru_sayaci][0]) == '0':
            random_indices = [0, 1, 2]
            random_indices.remove(random_index)
            random_indices.insert(0, random_index)

            options_texts = [self.soru_kalip[options_indices[i]][2] for i in random_indices]
            while len(set(options_texts)) != 3:
                random_index = random.randint(0, 2)
                options_texts[random_index] = self.soru_kalip[random_sayi1 + random_index][2]

            self.A.setText(options_texts[0])
            self.B.setText(options_texts[1])
            self.C.setText(options_texts[2])
            self.cümle_1.setText(self.soru_kalip[text_indices[random_indices[0]]][4])
            self.cümle_2.setText(self.soru_kalip[text_indices[random_indices[1]]][4])
            self.cümle_3.setText(self.soru_kalip[text_indices[random_indices[2]]][4])

        else:
            self.A.setText(self.soru_sik2[self.soru_sayaci][0])
            self.B.setText(self.soru_sik2[self.soru_sayaci][1])
            self.C.setText(self.soru_sik2[self.soru_sayaci][2])
            self.cümle_1.setText(self.soru_sik2[self.soru_sayaci][3])
            self.cümle_2.setText(self.soru_sik2[self.soru_sayaci][4])
            self.cümle_3.setText(self.soru_sik2[self.soru_sayaci][5])

        options = self.soru_sik2[self.soru_sayaci]
        options[0] = self.A.text()
        options[1] = self.B.text()
        options[2] = self.C.text()
        options[3] = self.cümle_1.text()
        options[4] = self.cümle_2.text()
        options[5] = self.cümle_3.text()

        self.sinav_soru.setText(self.soru_kalip[self.soru_sayaci][1])
        image = self.soru_kalip[self.soru_sayaci][0]
        pixmap = QPixmap(image)
        self.label_resim_soru.setPixmap(pixmap)
        self.label_resim_soru.setScaledContents(True)

        """sonraki önceki buton gösterme gizleme metni yazma"""
        if str(self.sikler[self.soru_sayaci][0]) == '0':
            self.secim_kaldir()
        else:
            attribute_to_set = getattr(self, str(self.sikler[self.soru_sayaci][0]))
            attribute_to_set.setChecked(True)
        if self.soru_sayaci == self.sinav_soru_sayisi:
            self.buton_sonraki_soru.hide()
            self.buton_sinav_bitir.show()
        if self.soru_sayaci > 1:
            self.buton_önceki_soru.show()
        """sonraki önceki buton gösterme gizleme metni yazma"""

    def onceki_soru(self):
        self.soru_sayaci -= 1
        self.label_sinav_sayac.setText(f"{self.soru_sayaci}")

        self.soru_sik2[self.soru_sayaci + 1][0] = self.A.text()
        self.soru_sik2[self.soru_sayaci + 1][1] = self.B.text()
        self.soru_sik2[self.soru_sayaci + 1][2] = self.C.text()

        self.cümle_soru.setText(f"{self.soru_kalip[self.soru_sayaci][3]}")

        self.A.setText(str(self.soru_sik2[self.soru_sayaci][0]))
        self.B.setText(str(self.soru_sik2[self.soru_sayaci][1]))
        self.C.setText(str(self.soru_sik2[self.soru_sayaci][2]))
        self.cümle_1.setText(str(self.soru_sik2[self.soru_sayaci][3]))
        self.cümle_2.setText(str(self.soru_sik2[self.soru_sayaci][4]))
        self.cümle_3.setText(str(self.soru_sik2[self.soru_sayaci][5]))

        self.label_resim_soru.setPixmap(QPixmap())
        self.label_resim_soru.setScaledContents(False)
        image = self.soru_kalip[self.soru_sayaci][0]
        pixmap = QPixmap(image)
        self.label_resim_soru.setPixmap(pixmap)
        self.label_resim_soru.setScaledContents(True)

        self.sinav_soru.setText(self.soru_kalip[self.soru_sayaci][1])


        """sonraki önceki buton gösterme gizleme metni yazma"""
        if str(self.sikler[self.soru_sayaci][0]) == '0':
            self.secim_kaldir()
        else:
            attribute_to_set = getattr(self, str(self.sikler[self.soru_sayaci][0]))
            attribute_to_set.setChecked(True)
        if self.soru_sayaci == 1:
            self.buton_önceki_soru.hide()
        if self.soru_sayaci < self.sinav_soru_sayisi:
            self.buton_sonraki_soru.show()
            self.buton_sinav_bitir.hide()
        """sonraki önceki buton gösterme gizleme metni yazma"""

    def kelime_ekle(self):
        ingilizce = self.line_edit_kelime_ingilizce.text()
        turkce = self.line_edit_kelime_turkce.text()
        cumle1 = self.line_edit_ingilizce_cümle.text()
        cumle2 = self.line_edit_türkçe_cümle.text()

        if ingilizce and turkce and cumle1 and cumle2:
            try:
                conn = sqlite3.connect('database/Kelimeler.db')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Kelimeler WHERE ingilizce_kelime = ?", (ingilizce,))
                existing_word = cursor.fetchone()

                if existing_word:
                    self.label_kelime_ekle.setText("Bu Kelime Zaten Mevcut. Başka Bir Kelime Deneyiniz.")
                else:
                    self.resim_dosya_yolu = 'resim/' + f"{ingilizce}" + '.png'
                    self.resim = cv2.resize(self.resim, (100, 100))
                    cv2.imwrite(self.resim_dosya_yolu, self.resim)

                    cursor.execute(
                        "INSERT INTO Kelimeler (ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2, resim) VALUES (?, ?, ?, ?, ?)",
                        (ingilizce, turkce, cumle1, cumle2, self.resim_dosya_yolu))

                    conn.commit()

                    self.label_kelime_ekle.setText("Başarıyla Eklenmiştir.")
                    self.temizle()

                conn.close()
            except Exception as e:
                print("Hata:", e)
                self.label_kelime_ekle.setText("Bir hata oluştu, lütfen tekrar deneyin.")
        else:
            self.label_kelime_ekle.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    def resim_sec(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "","Resim Dosyaları (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        self.resim = cv2.imread(file_name)
        if file_name:
            pixmap = QPixmap(file_name)
            self.label_ekleme_resim.setPixmap(pixmap.scaled(self.label_ekleme_resim.size(), aspectRatioMode=True))
            self.label_ekleme_resim.setScaledContents(True)

    def sinav_sonu_analiz(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_sonu_analiz(self)
        self.temizle()

        for sayac in range(self.sinav_soru_sayisi):
            if str(self.sikler[sayac + 1][0]) == '0':
                self.bos_sayisi += 1
            else:
                if str(self.sikler[sayac + 1][0]) == str(self.soru_kalip[sayac + 1][2]):
                    self.dogru_sayisi += 1
                else:
                    self.yanlis_sayisi += 1

            sayac += 1

        self.yazi_dogru_sayi.setText(str(self.dogru_sayisi))
        self.yazi_yanlis_sayi.setText(str(self.yanlis_sayisi))
        self.yazi_bos_sayi.setText(str(self.bos_sayisi))

        self.dogru_sayisi = 0
        self.yanlis_sayisi = 0
        self.bos_sayisi = 0

        self.soru_sayaci = 0
        self.soru_kalip = [[0 for j in range(5)] for i in range(21)]
        self.soru_sik2 = [[0 for j in range(6)] for i in range(21)]
        self.sikler = [[0 for j in range(2)] for i in range(21)]

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def temizle(self):
        self.label_giris.setText("")
        self.label_sinav_sayac.setText("")
        self.yazi_dogru_sayi.setText("")
        self.yazi_yanlis_sayi.setText("")
        self.label_ekleme_resim.setPixmap(QPixmap())
        self.label_ekleme_resim.setScaledContents(False)

        self.line_edit_kullanici_adi.clear()
        self.line_edit_sifre.clear()
        self.line_edit_isim.clear()
        self.line_edit_soyisim.clear()
        self.line_edit_kaydol_kullanici_adi.clear()
        self.line_edit_kaydol_sifre.clear()
        self.line_edit_sifre_kullanici_adi.clear()

        self.line_edit_kelime_ingilizce.clear()
        self.line_edit_kelime_turkce.clear()
        self.line_edit_ingilizce_cümle.clear()
        self.line_edit_türkçe_cümle.clear()

    def secim_kaldir(self):
        self.button_group1.setExclusive(False)
        self.A.setChecked(False)
        self.B.setChecked(False)
        self.C.setChecked(False)
        self.button_group1.setExclusive(True)

    def siklari_kaydet(self):
        sender_button = self.sender()
        bilgi = sender_button.property("bilgi")

        self.sikler[self.soru_sayaci][0] = bilgi

        if self.sikler[self.soru_sayaci][0] == "A":
            self.sikler[self.soru_sayaci][0] = str(self.A.text())

        if self.sikler[self.soru_sayaci][0] == "B":
            self.sikler[self.soru_sayaci][0] = str(self.B.text())

        if self.sikler[self.soru_sayaci][0] == "C":
            self.sikler[self.soru_sayaci][0] = str(self.C.text())

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