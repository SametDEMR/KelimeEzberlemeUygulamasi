import inspect

from AnaButonlar import *
from MetinselAraclar import *
from ShowHide import *
from Analizler import *

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

        self.tiklama = 0
        self.onay = 0
        self.sinav_soru_sayisi = 5
        self.kullan_soru_sayisi = self.sinav_soru_sayisi
        self.dil = 'ing'

        self.seslendirme_sayaci = 1

        self.sifirla()

        self.SinavSiklariKaydet = [[0 for j in range(2)] for i in range(25)]

        self.kontrol()

        self.setWindowTitle("Kelime Ezberleme Modülü")
        self.setStyleSheet("background-color: #1E468F")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(1200, 600)

        MetinselAraclar.Metinler(self)
        MetinselAraclar.KelimeEkleme(self)
        MetinselAraclar.GirisKismi(self)

        ButonOlustur.AnaMenuButonlari(self)
        ButonOlustur.SinavAnaButonlari(self)
        ButonOlustur.SinavIcButonlari(self)
        ButonOlustur.SinavSikButonlari(self)
        ButonOlustur.SoruSayisiButonlari(self)
        ButonOlustur.Seslendirme(self)
        ButonOlustur.DilDegistir(self)

        Analizler.SinavSonuSayfasi(self)
        Analizler.AnalizSayfasi(self)

        ShowHide.hepsini_gizleme(self)
        ShowHide.giris(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def sifirla(self):
        self.test_dogru_sayisi = 0
        self.test_yanlis_sayisi = 0
        self.test_bos_sayisi = 0

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
        self.sifirla()

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

                        cursor.execute(
                            "INSERT INTO Kelimeler (ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2, resim) VALUES (?, ?, ?, ?, ?)",
                            (ingilizce, turkce, cumle1, cumle2, self.resim_dosya_yolu))

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
                self.ortalama_sayi.setText(
                    "%" + str("{:.2f}".format((kullanici_verileri[1] / kullanici_verileri[4]) * 100)))

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

            cursor.execute('SELECT kelime FROM KaliciBilinen WHERE kullanici_id = ?;', (self.kullanici_id,))
            kalici_bilinen = cursor.fetchall()

            if kalici_bilinen:
                metin = "      ".join(k[0] for k in kalici_bilinen)
                self._ezber_yazi.setText(metin)

            conn.close()

        else:
            ShowHide.hepsini_gizleme(self)
            ShowHide.sinav_sonu_analiz(self)

            for sayac in range(self.kullan_soru_sayisi):
                if self.SinavSiklariKaydet[sayac][0] == 0:
                    self.test_bos_sayisi += 1
                elif str(self.SinavSiklariKaydet[sayac][1]) == str(self.Sorular[sayac]["cevabı"]):
                    self.test_dogru_sayisi += 1

                    conn = sqlite3.connect('database/KullaniciBilgileri.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        'SELECT bilinen, tarih, kelime_id, kelime FROM KullaniciBilinen WHERE kullanici_id = ? AND kelime = ?',
                        (self.kullanici_id, self.Sorular[sayac]["kelime"],))
                    islem = cursor.fetchone()

                    if islem:
                        bilinen = islem[0]
                        bilinen += 1
                        if bilinen == 7:
                            cursor.execute("INSERT INTO KaliciBilinen VALUES (?, ?, ?)",
                                           (self.kullanici_id, islem[2], islem[4]))

                            cursor.execute('DELETE FROM KullaniciBilinen WHERE kullanici_id = ? AND kelime_id = ?',
                                           (self.kullanici_id, islem[2], islem[3]))
                        else:
                            tarih = islem[1]

                            gun_ekle = {1: 1, 2: 3, 3: 7, 4: 0, 5: 0, 6: 0}
                            ay_ekle = {1: 0, 2: 0, 3: 0, 4: 1, 5: 6, 6: 0}
                            yil_ekle = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}
                            gun, ay, yil = map(int, tarih.split('.'))
                            gun += gun_ekle.get(bilinen, 0)
                            ay += ay_ekle.get(bilinen, 0)
                            yil += yil_ekle.get(bilinen, 0)

                            while gun > 30:
                                gun -= 30
                                ay += 1
                            while ay > 12:
                                ay -= 12
                                yil += 1

                            yeni_tarih = (f"{gun}.{ay}.{yil}")
                            cursor.execute(
                                'UPDATE KullaniciBilinen SET bilinen = ?, tarih = ? WHERE kullanici_id = ? AND kelime_id = ?',
                                (bilinen, yeni_tarih, self.kullanici_id, islem[2]))

                    else:
                        tarih = datetime.now().strftime('%x')
                        gun, ay, yil = map(int, tarih.split('.'))
                        yeni_tarih = f"{gun + 1}.{ay}.{yil}"
                        cursor.execute('INSERT INTO KullaniciBilinen VALUES (?, ?, ?, ?, ?)',
                                       (self.kullanici_id, self.Sorular[sayac]["id"], 1, self.Sorular[sayac]["kelime"],
                                        yeni_tarih))
                    conn.commit()
                    conn.close()
                else:
                    self.test_yanlis_sayisi += 1

            conn = sqlite3.connect('database/KullaniciBilgileri.db')
            cursor = conn.cursor()
            cursor.execute('''UPDATE Kullaniciİstatistik 
                    SET dogru_cevaplar = dogru_cevaplar + ?, yanlis_cevaplar = yanlis_cevaplar + ?, bos_cevaplar = bos_cevaplar + ?, toplam_sorular = toplam_sorular + ?
                    WHERE kullanici_id = ?''', (
            self.test_dogru_sayisi, self.test_yanlis_sayisi, self.test_bos_sayisi, self.sinav_soru_sayaci,
            self.kullanici_id))

            conn.commit()
            conn.close()

            self.yazi_dogru_sayi.setText(str(self.test_dogru_sayisi))
            self.yazi_yanlis_sayi.setText(str(self.test_yanlis_sayisi))
            self.yazi_bos_sayi.setText(str(self.test_bos_sayisi))
            self.yazi_toplam_sayi.setText(str(self.sinav_soru_sayaci))

            self.kullan_soru_sayisi = self.sinav_soru_sayisi

    def ayarlar(self):
        if self.tiklama == 0:
            self.button_group3.setExclusive(False)
            self.__dict__[f"{self.dil}"].setChecked(True)
            self.button_group3.setExclusive(True)

            self.button_group2.setExclusive(False)
            self.__dict__[f"_{self.kullan_soru_sayisi}"].setChecked(True)
            self.button_group2.setExclusive(True)

            ShowHide.hepsini_gizleme(self)
            ShowHide.ayarlar(self)
            self.tiklama += 1
        else:
            sender = self.sender()

            if len(sender.text()) < 3:
                self.sinav_soru_sayisi = int(sender.text())
                self.kullan_soru_sayisi = self.sinav_soru_sayisi
                self.yazi_toplam_sayi.setText(str(self.sinav_soru_sayisi))
            else:
                bilgi = sender.property("bilgi")
                self.dil = str(bilgi)

    """"""""""""""""""""""""

    def SoruOlustur(self):
        self.tiklama = 1
        self.Sorular = []
        self.sinav_soru_sayaci = 1
        ShowHide.hepsini_gizleme(self)
        ShowHide.sinav_sayfasi_sonra(self)

        tarih = datetime.now().strftime('%x')
        gun, ay, yil = map(int, tarih.split('.'))
        tarih = f"{gun}.{ay}.{yil}"

        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('SELECT kelime_id FROM KullaniciBilinen WHERE kullanici_id = ? AND tarih = ?',
                       (self.kullanici_id, tarih,))
        bugun_cikacak_kelimeler = cursor.fetchall()

        cursor.execute('SELECT kelime_id FROM KaliciBilinen WHERE kullanici_id = ?', (self.kullanici_id,))
        artik_cikmayacak_kelimeler = cursor.fetchall()
        conn.commit()
        conn.close()
        artik_cikmayacak_kelimeler += bugun_cikacak_kelimeler

        bugun_yazilacak = ["asd"] * len(bugun_cikacak_kelimeler)

        self.kullan_soru_sayisi += len(bugun_cikacak_kelimeler)

        conn = sqlite3.connect("database/Kelimeler.db")
        cursor = conn.cursor()
        for sayac in range(len(bugun_cikacak_kelimeler)):
            cursor.execute("SELECT * FROM kelimeler WHERE kelime_id = ?", (bugun_cikacak_kelimeler[sayac][0],))
            bugunkiler = cursor.fetchall()
            bugun_yazilacak[sayac] = (bugunkiler[0])

        if len(bugun_cikacak_kelimeler) == 0:
            cursor.execute("SELECT * FROM kelimeler ORDER BY RANDOM() LIMIT ?", (self.kullan_soru_sayisi,))
        else:
            for sayac in range(len(artik_cikmayacak_kelimeler)):
                çikmaycak = int(artik_cikmayacak_kelimeler[sayac][0])
                cursor.execute("SELECT * FROM kelimeler WHERE NOT kelime_id = ? ORDER BY RANDOM() LIMIT ?",
                               (çikmaycak, self.kullan_soru_sayisi,))

        rows = cursor.fetchall()
        conn.close()
        bugun_yazilacak += rows

        for row in bugun_yazilacak:
            data = list(row)
            id, ingilizce, turkce, cumle_ing, cumle_tr, image_path = data
            if self.dil == 'tr':
                correct_answer = ingilizce
                other_answers = [r[1] for r in bugun_yazilacak if r[0] != id]
            else:
                correct_answer = turkce
                other_answers = [r[2] for r in bugun_yazilacak if r[0] != id]
            wrong_answers = random.sample(other_answers, 2)

            choices = {"A": None, "B": None, "C": None}
            answers = [correct_answer] + wrong_answers[:2]
            random.shuffle(answers)
            choices["A"], choices["B"], choices["C"] = answers

            if self.dil == 'tr':
                self.label_soru_metin.setText("YUKARIDAKİ KELİMENİN İNGİLİZCESİ NEDİR?")
                question = {
                    "id": id,
                    "image_path": image_path,
                    "kelime": turkce,
                    "cumle": cumle_tr,
                    "choices": choices,
                    "cevabı": ingilizce
                }
            else:
                self.label_soru_metin.setText("YUKARIDAKİ KELİMENİN TÜRKÇESİ NEDİR?")
                question = {
                    "id": id,
                    "image_path": image_path,
                    "kelime": ingilizce,
                    "cumle": cumle_ing,
                    "choices": choices,
                    "cevabı": turkce
                }
            self.Sorular.append(question)

        self.label_sinav_sayac.setText(str(self.sinav_soru_sayaci))
        image = self.Sorular[self.sinav_soru_sayaci - 1]['image_path']
        pixmap = QPixmap(image)
        self.label_resim_soru.setPixmap(pixmap)
        self.label_resim_soru.setScaledContents(True)
        self.sinav_soru.setText(self.Sorular[self.sinav_soru_sayaci - 1]['kelime'])
        self.cümle_soru.setText(self.Sorular[self.sinav_soru_sayaci - 1]['cumle'])
        self.A.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['A'])
        self.B.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['B'])
        self.C.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['C'])

    def SoruDegistir(self, degistirme):
        self.sinav_soru_sayaci += int(degistirme)

        self.label_sinav_sayac.setText(str(self.sinav_soru_sayaci))
        image = self.Sorular[self.sinav_soru_sayaci - 1]['image_path']
        pixmap = QPixmap(image)
        self.label_resim_soru.setPixmap(pixmap)
        self.label_resim_soru.setScaledContents(True)
        self.sinav_soru.setText(self.Sorular[self.sinav_soru_sayaci - 1]['kelime'])
        self.cümle_soru.setText(self.Sorular[self.sinav_soru_sayaci - 1]['cumle'])
        self.A.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['A'])
        self.B.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['B'])
        self.C.setText(self.Sorular[self.sinav_soru_sayaci - 1]['choices']['C'])

        self.secim_kaldir()
        if str(self.SinavSiklariKaydet[self.sinav_soru_sayaci][0]) != '0':
            self.button_group1.setExclusive(False)
            getattr(self, self.SinavSiklariKaydet[self.sinav_soru_sayaci][2]).setChecked(True)
            self.button_group1.setExclusive(True)

        if self.sinav_soru_sayaci == self.kullan_soru_sayisi:
            self.buton_sonraki_soru.hide()
            self.buton_sinav_bitir.show()
        else:
            self.buton_sonraki_soru.show()
            self.buton_sinav_bitir.hide()
        if self.sinav_soru_sayaci != 1:
            self.buton_önceki_soru.show()
        else:
            self.buton_önceki_soru.hide()

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

        self.SinavSiklariKaydet[self.sinav_soru_sayaci - 1] = (str(self.sinav_soru.text()), str(getattr(self, bilgi).text()), str(bilgi))

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
        cikti.save("dosya/ses" + str(self.seslendirme_sayaci) + ".mp3")
        playsound("dosya/ses" + str(self.seslendirme_sayaci) + ".mp3")
        self.seslendirme_sayaci += 1

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = Ana_Pencere123()
    giris_sayfasi.show()
    sys.exit(app.exec_())