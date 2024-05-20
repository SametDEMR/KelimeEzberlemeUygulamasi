from AnaButonlar import *
from TextBoxOlustur import *
from ShowHide import *
from LabelOlustur import *
from Siklar import *
from Siklik import *
from MetinSesButon import *
from AnalizKısımları import *
from DilDeğiştir import *

from gtts import gTTS
from playsound import playsound
import sqlite3
import os, sys, random
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
import cv2
from datetime import datetime
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


locale.setlocale(locale.LC_ALL, 'turkish')


class Ana_Pencere123(QWidget):
    def __init__(self):
        super().__init__()

        self.tiklama = 0
        self.onay = 0
        self.sinav_soru_sayisi = 5
        self.toplam_goster_soru = 0
        self.onceki_soru_sayisi = 0
        self.dil = 'ing'

        self.bilinen_kelimeler = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: []
        }

        self.sifirla()
        self.kontrol()

        self.setWindowTitle("Kelime Ezberleme Modülü")
        self.setStyleSheet("background-color: #1E468F")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(1200, 600)

        LabelOlustur.Olustur(self)
        TextBoxOlustur.Olustur(self)
        ButonOlustur.Olustur(self)
        SiklikOlustur.Olustur(self)
        SiklarOlustur.Olustur(self)
        SinavSonuAnaliz.Olustur(self)
        MetinSesButonOlustur.Olustur(self)
        DilButonOlustur.Olustur(self)

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

    def sifirla(self):
        self.toplam_dogru_sayisi = 0
        self.toplam_yanlis_sayisi = 0
        self.toplam_bos_sayisi = 0
        self.toplam_soru_sayisi = 0

        self.dogru_sayisi = 0
        self.yanlis_sayisi = 0
        self.bos_sayisi = 0
        self.soru_sayaci = 0

        self.soru_kalip = [[0 for j in range(5)] for i in range(50)]
        self.soru_siklari = [[0 for j in range(6)] for i in range(50)]
        self.sikler_kayit = [[0 for j in range(4)] for i in range(50)]

    def cikis(self):
        QApplication.quit()

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

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def geri_giris(self):
        self.tiklama = 0
        self.temizle()
        ShowHide.hepsini_gizleme(self)

        ShowHide.giris(self)

    def giris(self):
        username = self.line_edit_kullanici_adi.text()
        password = self.line_edit_sifre.text()

        if username and password:
            conn = sqlite3.connect("database/KullaniciBilgileri.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi = ? AND sifre = ?", (username, password))
            user = cursor.fetchone()
            conn.close()

            if user:
                self.kullanici_id = user[0]
                self.temizle()
                ShowHide.hepsini_gizleme(self)
                ShowHide.sinav_ana_menu(self)
            else:
                self.label_giris.setText("Kullanıcı Adı Veya Şifre Yanlış. Tekrar Deneyiniz.")
        else:
            self.label_giris.setText("Lütfen Bilgileri Eksiksiz Giriniz. ★")

    def sifre_unuttum(self):
        if self.tiklama == 0:
            self.temizle()
            ShowHide.hepsini_gizleme(self)
            ShowHide.sifre_unuttum(self)
            self.tiklama += 1
        else:
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

    def kayit(self):
        if self.tiklama == 0:
            self.temizle()
            ShowHide.hepsini_gizleme(self)
            ShowHide.kayit(self)
            self.tiklama += 1
        else:
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
                cursor.execute("INSERT INTO kullanicilar (isim, soyisim, kullaniciadi, sifre) VALUES (?, ?, ?, ?)",
                               (isim, soyisim, kullaniciadi, sifre))
                cursor.execute(
                    "INSERT INTO Kullaniciİstatistik (dogru_cevaplar, yanlis_cevaplar, bos_cevaplar, toplam_sorular) VALUES (0, 0, 0, 0)")

                conn.commit()
                conn.close()

                if isim and soyisim and sifre and kullaniciadi:
                    self.temizle()
                    self.label_giris.setText("Kayıt İşlemi Başarılı! Giriş İçin Ana Menüye Dönünüz.")
                else:
                    self.label_giris.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    def sifre_goster_gizle(self):
        sender = self.sender()
        if sender.isChecked():
            self.line_edit_sifre.setEchoMode(QLineEdit.Normal)
        else:
            self.line_edit_sifre.setEchoMode(QLineEdit.Password)


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def geri_sinav(self):
        self.tiklama = 0
        self.temizle()

        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_ana_menu(self)

    def analiz_geri(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.analiz(self)

    def analiz_sayisal(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.sayisal(self)

    def analiz_sozel(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.sozel(self)

    def sinav(self):
        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_sayfasi_once(self)

    def kelime_ekleme(self):
        if self.tiklama == 0:
            ShowHide.hepsini_gizleme(self)
            ShowHide.soru_ekleme(self)
            self.tiklama += 1
        else:
            ingilizce = self.line_edit_kelime_ingilizce.text()
            turkce = self.line_edit_kelime_turkce.text()
            cumle1 = self.line_edit_ingilizce_cümle.text()
            cumle2 = self.line_edit_türkçe_cümle.text()

            if ingilizce and turkce and cumle1 and cumle2:
                conn = sqlite3.connect('database/Kelimeler.db')
                cursor = conn.cursor()
                ingilizce_lower = ingilizce.lower()

                cursor.execute("SELECT * FROM Kelimeler WHERE LOWER(ingilizce_kelime) = ?", (ingilizce_lower,))
                existing_word = cursor.fetchone()

                if existing_word:
                    self.label_kelime_ekle.setText("Bu Kelime Zaten Mevcut. Başka Bir Kelime Deneyiniz.")
                else:
                    if self.onay == 0:
                        self.label_kelime_ekle.setText("Lütfen Resim Seçiniz.")
                    else:
                        self.resim_dosya_yolu = 'resim/' + f"{ingilizce}" + '.png'
                        self.resim = cv2.resize(self.resim, (100, 100))
                        cv2.imwrite(self.resim_dosya_yolu, self.resim)

                        tarih = datetime.datetime.now().strftime('%x')

                        cursor.execute(
                            "INSERT INTO Kelimeler (tarih, ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2, resim) VALUES (?, ?, ?, ?, ?, ?)",
                            (tarih, ingilizce, turkce, cumle1, cumle2, self.resim_dosya_yolu))

                        conn.commit()

                        self.label_kelime_ekle.setText("Başarıyla Eklenmiştir.")
                        self.temizle()
                        self.onay = 0
            else:
                self.label_kelime_ekle.setText("Lütfen Bilgileri Eksiksiz Giriniz")

    def analiz(self):
        if self.tiklama == 0:
            ShowHide.hepsini_gizleme(self)
            ShowHide.analiz(self)

            conn = sqlite3.connect('database/KullaniciBilgileri.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Kullaniciİstatistik WHERE kullanici_id = ?;', (self.kullanici_id,))
            kullanici_verileri = cursor.fetchone()
            conn.commit()
            conn.close()

            self.toplam_dogru_sayi.setText("" + str(kullanici_verileri[1]))
            self.toplam_yanlis_sayi.setText("" + str(kullanici_verileri[2]))
            self.toplam_bos_sayi.setText("" + str(kullanici_verileri[3]))
            self.toplam_soru_sayi.setText("" + str(kullanici_verileri[4]))

            if kullanici_verileri[1] == 0:
                self.ortalama_sayi.setText("ORTALAMA : %00.00")
            else:
                self.ortalama_sayi.setText("%" + str("{:.2f}".format((kullanici_verileri[1] / kullanici_verileri[4])*100)))




            conn = sqlite3.connect('database/KullaniciBilgileri.db')
            cursor = conn.cursor()
            cursor.execute('SELECT kelime, bilinen FROM KullaniciBilinen WHERE kullanici_id = ?;',
                           (self.kullanici_id,))
            kullanici_bilinen = cursor.fetchall()



            bilinen_sozluk = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

            for kelime, bilinen in kullanici_bilinen:
                if bilinen in bilinen_sozluk:
                    bilinen_sozluk[bilinen].append(kelime)

            for bilinen_seviye, kelime_listesi in bilinen_sozluk.items():
                label = getattr(self, f"_{bilinen_seviye}lik_yazi", None)
                label.setText("\n".join(kelime_listesi))


            cursor.execute('SELECT kelime FROM KaliciBilinen WHERE kullanici_id = ?;',(self.kullanici_id,))
            kalici_bilinen = cursor.fetchall()

            if kalici_bilinen:
                metin = "      ".join(k[0] for k in kalici_bilinen)
                self._ezber_yazi.setText(metin)

            conn.close()

        else:
            ShowHide.hepsini_gizleme(self)
            ShowHide.sinav_sonu_analiz(self)
            self.temizle()

            for sayac in range(self.sinav_soru_sayisi):
                if str(self.sikler_kayit[sayac + 1][0]) == '0':
                    self.bos_sayisi += 1
                else:
                    try:
                        if str(self.sikler_kayit[sayac + 1][1]) == str(self.soru_kalip[sayac + 1][2]):
                            self.dogru_sayisi += 1

                            kelime_id = str(self.sikler_kayit[sayac + 1][2])
                            kelime = str(self.sikler_kayit[sayac + 1][3])

                            conn = sqlite3.connect('database/KullaniciBilgileri.db')
                            cursor = conn.cursor()
                            cursor.execute(
                                'SELECT bilinen, tarih FROM KullaniciBilinen WHERE kelime_id = ? AND kullanici_id = ?',
                                (kelime_id, self.kullanici_id))
                            islem = cursor.fetchone()

                            if islem:
                                bilinen = islem[0]
                                bilinen += 1
                                if bilinen == 7:
                                    cursor.execute("INSERT INTO KaliciBilinen VALUES (?, ?, ?)",(self.kullanici_id, kelime_id, kelime))

                                    cursor.execute('DELETE FROM KullaniciBilinen WHERE kullanici_id = ? AND kelime_id = ?',
                                            (self.kullanici_id, kelime_id))
                                else:
                                    tarih = islem[1]
                                    gun, ay, yil = map(int, tarih.split('.'))

                                    gun_ekle = {1: 1, 2: 3, 3: 7, 4: 0, 5: 0, 6: 0}
                                    ay_ekle = {1: 0, 2: 0, 3: 0, 4: 1, 5: 6, 6: 0}
                                    yil_ekle = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}
                                    gun += gun_ekle.get(bilinen, 0)
                                    ay += ay_ekle.get(bilinen, 0)
                                    yil += yil_ekle.get(bilinen, 0)

                                    yeni_tarih = f"{gun}.{ay}.{yil}"
                                    cursor.execute('UPDATE KullaniciBilinen SET bilinen = ?, tarih = ? WHERE kullanici_id = ? AND kelime_id = ?',
                                            (bilinen, yeni_tarih, self.kullanici_id, kelime_id))

                            else:
                                tarih = datetime.now().strftime('%x')
                                gun, ay, yil = map(int, tarih.split('.'))
                                yeni_tarih = f"{gun}.{ay}.{yil}"
                                cursor.execute('INSERT INTO KullaniciBilinen VALUES (?, ?, ?, ?, ?)',
                                               (self.kullanici_id, kelime_id, 1, kelime, yeni_tarih))

                            conn.commit()
                            conn.close()
                    except Exception as e:
                        print(e)
                    else:
                        self.yanlis_sayisi += 1

                sayac += 1

            self.yazi_dogru_sayi.setText(str(self.dogru_sayisi))
            self.yazi_yanlis_sayi.setText(str(self.yanlis_sayisi))
            self.yazi_bos_sayi.setText(str(self.bos_sayisi))

            conn = sqlite3.connect('database/KullaniciBilgileri.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Kullaniciİstatistik WHERE kullanici_id = ?;', (self.kullanici_id,))
            kullanici_verileri = cursor.fetchone()
            conn.commit()
            conn.close()

            self.toplam_dogru_sayisi += int(self.dogru_sayisi) + kullanici_verileri[1]
            self.toplam_yanlis_sayisi += int(self.yanlis_sayisi) + kullanici_verileri[2]
            self.toplam_bos_sayisi += int(self.bos_sayisi) + kullanici_verileri[3]
            self.toplam_soru_sayisi += int(self.toplam_goster_soru) + kullanici_verileri[4]

            conn = sqlite3.connect('database/KullaniciBilgileri.db')
            cursor = conn.cursor()
            cursor.execute('''UPDATE Kullaniciİstatistik 
                                          SET dogru_cevaplar = ?, yanlis_cevaplar = ?, bos_cevaplar = ?, toplam_sorular = ?
                                          WHERE kullanici_id = ?''',
                           (self.toplam_dogru_sayisi, self.toplam_yanlis_sayisi,
                            self.toplam_bos_sayisi, self.toplam_soru_sayisi, self.kullanici_id))

            conn.commit()
            conn.close()

            self.sifirla()

    def ayarlar(self):
        if self.tiklama == 0:
            self.button_group3.setExclusive(False)
            self.__dict__[f"{self.dil}"].setChecked(True)
            self.button_group3.setExclusive(True)
            self.button_group.setExclusive(False)
            self.__dict__[f"_{self.sinav_soru_sayisi}"].setChecked(True)
            self.button_group.setExclusive(True)
            ShowHide.hepsini_gizleme(self)
            ShowHide.ayarlar(self)
            self.tiklama +=1
        else:
            sender = self.sender()

            if len(sender.text()) < 3:
                self.sinav_soru_sayisi = int(sender.text())
                self.yazi_toplam_sayi.setText(str(self.sinav_soru_sayisi))
            else:
                bilgi = sender.property("bilgi")
                self.dil = str(bilgi)

    """"""""""""""""""""""""

    def sonraki_soru(self):
        self.tiklama = 1
        if self.soru_sayaci == 0:
            ShowHide.hepsini_gizleme(self)
            ShowHide.sinav_sayfasi_sonra(self)

            self.toplam_goster_soru = self.sinav_soru_sayisi

            tarih = datetime.now().strftime('%x')
            gun, ay, yil = map(int, tarih.split('.'))
            tarih = f"{gun}.{ay}.{yil}"

            conn = sqlite3.connect('database/KullaniciBilgileri.db')
            cursor = conn.cursor()
            cursor.execute('SELECT kelime_id FROM KullaniciBilinen WHERE kullanici_id = ? AND tarih = ?', (self.kullanici_id, tarih,))
            bilinen_kelimeler = cursor.fetchall()
            cursor.execute('SELECT kelime_id FROM KaliciBilinen')
            kalici_bilinen = cursor.fetchall()
            conn.commit()
            conn.close()

            conn = sqlite3.connect('database/Kelimeler.db')
            cursor = conn.cursor()
            kelime_bilgileri = []
            for kelime_id in bilinen_kelimeler:
                cursor.execute('SELECT resim, ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2 FROM Kelimeler WHERE kelime_id = ?',
                        (kelime_id[0],))
                kelime_bilgisi = cursor.fetchone()
                kelime_bilgileri.append(kelime_bilgisi)
            if len(kalici_bilinen) == 0:
                cursor.execute('SELECT resim, ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2 FROM Kelimeler')
            else:
                for sayac in range(len(kalici_bilinen)):
                    cursor.execute('SELECT resim, ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2 FROM Kelimeler WHERE NOT kelime_id = ?', (kalici_bilinen[sayac][0],))
            soru_kalip = cursor.fetchall()
            random_kalip = random.sample(soru_kalip, 25)
            conn.commit()
            conn.close()

            self.toplam_goster_soru += int(len(bilinen_kelimeler))
            kelime_bilgileri += random_kalip

            self.sayac = 1
            if self.dil == 'tr':
                self.label_metin.setText("Yukarıda Verilen Kelimenin İNGİLİZCESİ Nedir?")
                for random_resim, random_ingilizce, random_turkce, random_cümle1, random_cümle2 in kelime_bilgileri:
                    self.soru_kalip[self.sayac][0] = random_resim
                    self.soru_kalip[self.sayac][1] = random_turkce
                    self.soru_kalip[self.sayac][2] = random_ingilizce
                    self.soru_kalip[self.sayac][3] = random_cümle2
                    self.soru_kalip[self.sayac][4] = random_cümle1
                    self.sayac += 1
            else:
                self.label_metin.setText("Yukarıda Verilen Kelimenin TÜRKÇESİ Nedir?")
                for random_resim, random_ingilizce, random_turkce, random_cümle1, random_cümle2 in kelime_bilgileri:
                    self.soru_kalip[self.sayac][0] = random_resim
                    self.soru_kalip[self.sayac][1] = random_ingilizce
                    self.soru_kalip[self.sayac][2] = random_turkce
                    self.soru_kalip[self.sayac][3] = random_cümle1
                    self.soru_kalip[self.sayac][4] = random_cümle2
                    self.sayac += 1


        self.soru_sayaci += 1
        self.label_sinav_sayac.setText(f"{self.soru_sayaci}")

        self.cümle_soru.setText(f"{self.soru_kalip[self.soru_sayaci][3]}")

        seçilecek = ['A','B','C']
        rastgele_seç = random.choice(seçilecek)

        if str(self.soru_siklari[self.soru_sayaci][0]) == '0':
            self.A.setText(self.soru_kalip[self.soru_sayaci + 1][2])
            self.B.setText(self.soru_kalip[self.soru_sayaci + 2][2])
            self.C.setText(self.soru_kalip[self.soru_sayaci + 3][2])
            getattr(self, rastgele_seç).setText(self.soru_kalip[self.soru_sayaci][2])
        else:
            self.A.setText(self.soru_siklari[self.soru_sayaci][0])
            self.B.setText(self.soru_siklari[self.soru_sayaci][1])
            self.C.setText(self.soru_siklari[self.soru_sayaci][2])

        options = self.soru_siklari[self.soru_sayaci]
        options[0] = self.A.text()
        options[1] = self.B.text()
        options[2] = self.C.text()

        self.sinav_soru.setText(self.soru_kalip[self.soru_sayaci][1])
        image = self.soru_kalip[self.soru_sayaci][0]
        pixmap = QPixmap(image)
        self.label_resim_soru.setPixmap(pixmap)
        self.label_resim_soru.setScaledContents(True)


        """sonraki önceki buton gösterme gizleme metni yazma"""
        self.secim_kaldir()
        if str(self.sikler_kayit[self.soru_sayaci][0]) != '0':
            self.button_group1.setExclusive(False)
            getattr(self, self.sikler_kayit[self.soru_sayaci][0]).setChecked(True)
            self.button_group1.setExclusive(True)
        if self.soru_sayaci == self.toplam_goster_soru:
            self.buton_sonraki_soru.hide()
            self.buton_sinav_bitir.show()
        if self.soru_sayaci > 1:
            self.buton_önceki_soru.show()
        """sonraki önceki buton gösterme gizleme metni yazma"""

        self.yazi_toplam_sayi.setText(str(self.toplam_goster_soru))

    def onceki_soru(self):
        self.soru_sayaci -= 1
        self.label_sinav_sayac.setText(f"{self.soru_sayaci}")

        self.soru_siklari[self.soru_sayaci + 1][0] = self.A.text()
        self.soru_siklari[self.soru_sayaci + 1][1] = self.B.text()
        self.soru_siklari[self.soru_sayaci + 1][2] = self.C.text()

        self.cümle_soru.setText(f"{self.soru_kalip[self.soru_sayaci][3]}")

        self.A.setText(str(self.soru_siklari[self.soru_sayaci][0]))
        self.B.setText(str(self.soru_siklari[self.soru_sayaci][1]))
        self.C.setText(str(self.soru_siklari[self.soru_sayaci][2]))

        self.label_resim_soru.setPixmap(QPixmap())
        self.label_resim_soru.setScaledContents(False)
        image = self.soru_kalip[self.soru_sayaci][0]
        pixmap = QPixmap(image)
        self.label_resim_soru.setPixmap(pixmap)
        self.label_resim_soru.setScaledContents(True)

        self.sinav_soru.setText(self.soru_kalip[self.soru_sayaci][1])


        """sonraki önceki buton gösterme gizleme metni yazma"""
        self.secim_kaldir()
        if str(self.sikler_kayit[self.soru_sayaci][0]) != '0':
            self.button_group1.setExclusive(False)
            getattr(self, self.sikler_kayit[self.soru_sayaci][0]).setChecked(True)
            self.button_group1.setExclusive(True)
        if self.soru_sayaci == 1:
            self.buton_önceki_soru.hide()
        if self.soru_sayaci < self.sinav_soru_sayisi:
            self.buton_sonraki_soru.show()
            self.buton_sinav_bitir.hide()
        """sonraki önceki buton gösterme gizleme metni yazma"""

    def resim_sec(self):
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "","Resim Dosyaları (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        self.resim = cv2.imread(self.file_name)
        if self.file_name:
            pixmap = QPixmap(self.file_name)
            self.label_ekleme_resim.setPixmap(pixmap.scaled(self.label_ekleme_resim.size(), aspectRatioMode=True))
            self.label_ekleme_resim.setScaledContents(True)
            self.onay = 1

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def secim_kaldir(self):
        self.button_group1.setExclusive(False)
        self.A.setChecked(False)
        self.B.setChecked(False)
        self.C.setChecked(False)
        self.button_group1.setExclusive(True)

    def siklari_kaydet(self):
        sender_button = self.sender()
        bilgi = sender_button.property("bilgi")

        arama = getattr(self, bilgi).text()
        conn = sqlite3.connect('database/Kelimeler.db')
        cursor = conn.cursor()
        cursor.execute('SELECT kelime_id, ingilizce_kelime FROM Kelimeler WHERE türkçe_kelime = ? OR ingilizce_kelime = ? COLLATE NOCASE',
                       (arama,arama,))

        işlemler = cursor.fetchall()
        conn.commit()
        conn.close()

        self.sikler_kayit[self.soru_sayaci][0] = str(bilgi)
        self.sikler_kayit[self.soru_sayaci][1] = getattr(self, bilgi).text()
        self.sikler_kayit[self.soru_sayaci][2] = işlemler[0][0]
        self.sikler_kayit[self.soru_sayaci][3] = işlemler[0][1]

    def seslendirme(self, pos):
        corrected_pos = pos - QPoint(160, 0)
        buton_metni = self.childAt(corrected_pos).text()

        if self.dil == 'tr':
            if corrected_pos.y() > 100:
                language = 'en'
            else:
                language = 'tr'
        else:
            if corrected_pos.y() > 100:
                language = 'tr'
            else:
                language = 'en'

        cikti = gTTS(text=buton_metni, lang=language, slow=False)
        cikti.save("dosya/ses" + str(self.sayac) + ".mp3")
        playsound("dosya/ses" + str(self.sayac) + ".mp3")
        self.sayac += 1

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def yazdir(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])

        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Kullaniciİstatistik WHERE kullanici_id = ?;', (self.kullanici_id,))
        kullanici_verileri = cursor.fetchone()
        conn.commit()
        conn.close()

        c = canvas.Canvas(file_path, pagesize=letter)

        c.drawString(250, 750, "- ANALIZ -")

        c.setFont("Helvetica", 16)
        c.drawString(15, 720, "Toplam Dogru Sayisi : " + str(kullanici_verileri[1]) + "    Toplam Yanlis Sayisi : " + str(kullanici_verileri[2]) + "    Toplam Bos Sayisi : " + str(kullanici_verileri[3]))
        c.drawString(115, 690, "Toplam Soru Sayisi : " + str(kullanici_verileri[4]) + "    Ortalama : %" + str("{:.2f}".format((kullanici_verileri[1] / kullanici_verileri[4])*100)))

        c.drawString(25, 530, "EZBERLENMIS")
        c.drawString(25, 500, "★★★★★★")
        c.drawString(25, 470, "★★★★★")
        c.drawString(25, 440, "★★★★")
        c.drawString(25, 410, "★★★")
        c.drawString(25, 380, "★★")
        c.drawString(25, 350, "★")

        c.drawString(180, 530, self._ezber_yazi.text())


        metin1 = self._1lik_yazi.text()
        yeni_metin1 = metin1.replace("\n", "      ")
        metin2 = self._2lik_yazi.text()
        yeni_metin2 = metin2.replace("\n", "      ")
        metin3 = self._3lik_yazi.text()
        yeni_metin3 = metin3.replace("\n", "      ")
        metin4 = self._4lik_yazi.text()
        yeni_metin4 = metin4.replace("\n", "      ")
        metin5 = self._5lik_yazi.text()
        yeni_metin5 = metin5.replace("\n", "      ")
        metin6 = self._6lik_yazi.text()
        yeni_metin6 = metin6.replace("\n", "      ")
        c.drawString(180, 500, yeni_metin1)
        c.drawString(180, 470, yeni_metin2)
        c.drawString(180, 440, yeni_metin3)
        c.drawString(180, 410, yeni_metin4)
        c.drawString(180, 380, yeni_metin5)
        c.drawString(180, 350, yeni_metin6)


        c.save()
        print(file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = Ana_Pencere123()
    giris_sayfasi.show()
    sys.exit(app.exec_())