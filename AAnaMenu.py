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

        self.setWindowTitle("Kelime Ezberleme Modülü")
        self.setStyleSheet("background-color: #1E468F")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(1200, 600)

        MetinselAraclar.UyariMetinGirisleri(self)
        MetinselAraclar.KelimeEklemeSayfasiMetinGirisleri(self)
        MetinselAraclar.GirisSayfasiMetinGirisleri(self)

        ButonOlustur.GirisMenuButonlari(self)
        ButonOlustur.GirisMenuIcIslemButonlari(self)
        ButonOlustur.SinavAnaMenuButonlari(self)
        ButonOlustur.SinavMenuIcIslemButonlari(self)
        ButonOlustur.SinavSikButonlari(self)
        ButonOlustur.AyarlarSoruSayisiSecmeButonlari(self)
        ButonOlustur.MetinleriSeslendirmeButonlari(self)
        ButonOlustur.SoruDilDegistirButonlari(self)

        TabloOlustur.Olustur(self)

        Analizler.AnaAnalizSayfasi(self)
        Analizler.SinavSonuAnalizSayfasi(self)


        self.SayfalaraYonlendir("GirisAnaMenu")
        self.GenelIslemleriSifirla()

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def SayfalaraYonlendir(self, SayfaAdi):
        ShowHide.TumAraclariGizle(self)
        ShowHide.__dict__[f"{SayfaAdi}"](self)
        self.GenelIslemleriSifirla()

        if SayfaAdi == "SinavaBaslamaSonrasi":
            self.SoruOlustur()
        if SayfaAdi == "SinavSonuAnaliz":
            self.SinavSonuAnaliz()
        if SayfaAdi == "Ayarlar":
            self.button_group3.setExclusive(False)
            self.__dict__[f"{self.dil}"].setChecked(True)
            self.button_group3.setExclusive(True)
            self.button_group2.setExclusive(False)
            self.__dict__[f"_{self.kullan_soru_sayisi}"].setChecked(True)
            self.button_group2.setExclusive(True)
            ShowHide.Ayarlar(self)
        if SayfaAdi == "AnalizKismi":
            self.AnalizSayfasi()
        if SayfaAdi == "Kelimeler":
            self.TabloyaKelimeleriKoy()
    def VeritabaniKontrolEt(self):
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
    ###GİRİŞ MENÜSÜNÜN İÇERİKLERİ
    def GirisButonunaBasildi(self):
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
                ShowHide.TumAraclariGizle(self)
                ShowHide.SinavUygulamasiAnaMenu(self)
            else:
                self.label_giris.setText("Kullanıcı Adı Veya Şifre Yanlış. Tekrar Deneyiniz.")
        else:
            self.label_giris.setText("Lütfen Bilgileri Eksiksiz Giriniz.")

    def SifreUnuttumButonunaBasildi(self):
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

    def KayitButonunaBasildi(self):
        isim = self.line_edit_isim.text()
        soyisim = self.line_edit_soyisim.text()
        kullaniciadi = self.line_edit_kaydol_kullanici_adi.text()
        sifre = self.line_edit_kaydol_sifre.text()

        if not isim or not soyisim or not kullaniciadi or not sifre:
            self.label_giris.setText("Lütfen Bilgileri Eksiksiz Giriniz.")
        elif len(sifre) < 10:
            self.label_giris.setText("Şifre en az 10 karakter uzunluğunda olmalıdır.")
        else:
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

                self.label_giris.setText("Kayıt İşlemi Başarılı! Giriş İçin Ana Menüye Dönünüz.")

    def SifreGosterGizle(self):
        SifreGosterGizleButonu = self.sender()
        if SifreGosterGizleButonu.isChecked():
            self.line_edit_sifre.setEchoMode(QLineEdit.Normal)
        else:
            self.line_edit_sifre.setEchoMode(QLineEdit.Password)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    ### SİNAV MENÜSÜ İÇERİKLERİ
    def Ayarlar(self):
        TiklananButon = self.sender()
        if len(TiklananButon.text()) < 3:
            self.sinav_soru_sayisi = int(TiklananButon.text())
            self.kullan_soru_sayisi = self.sinav_soru_sayisi
            self.yazi_toplam_sayi.setText(str(self.sinav_soru_sayisi))
        else:
            bilgi = TiklananButon.property("bilgi")
            self.dil = str(bilgi)
    def AnalizSayfasi(self):
        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Kullaniciİstatistik WHERE kullanici_id = ?;', (self.kullanici_id,))
        KullaniciIstatistikleri = cursor.fetchone()
        conn.commit()
        conn.close()

        self.toplam_dogru_sayi.setText("" + str(KullaniciIstatistikleri[1]))
        self.toplam_yanlis_sayi.setText("" + str(KullaniciIstatistikleri[2]))
        self.toplam_bos_sayi.setText("" + str(KullaniciIstatistikleri[3]))
        self.toplam_soru_sayi.setText("" + str(KullaniciIstatistikleri[4]))

        if KullaniciIstatistikleri[1] == 0:
            self.ortalama_sayi.setText("ORTALAMA : %00.00")
        else:
            self.ortalama_sayi.setText(
                "%" + str("{:.2f}".format((KullaniciIstatistikleri[1] / KullaniciIstatistikleri[4]) * 100)))

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

    ### SİNAV SORULARI İŞLEMLERİ
    def SoruOlustur(self):
        self.SinavSiklariKaydet = [[0 for j in range(2)] for i in range(25)]
        self.Sorular = []
        self.sinav_soru_sayaci = 1

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
            id, ingilizce_kelime, turkce_kelime, cumle_ing, cumle_tr, image_path = data
            if self.dil == 'tr':
                correct_answer = ingilizce_kelime
                other_answers = [r[1] for r in bugun_yazilacak if r[0] != id]
            else:
                correct_answer = turkce_kelime
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
                    "kelime": turkce_kelime,
                    "cumle": cumle_tr,
                    "choices": choices,
                    "cevabı": ingilizce_kelime
                }
            else:
                self.label_soru_metin.setText("YUKARIDAKİ KELİMENİN TÜRKÇESİ NEDİR?")
                question = {
                    "id": id,
                    "image_path": image_path,
                    "kelime": ingilizce_kelime,
                    "cumle": cumle_ing,
                    "choices": choices,
                    "cevabı": turkce_kelime
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

        self.SinavSiklariSeciminiKaldir()
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
    def SinavSiklariSeciminiKaldir(self):
        self.button_group1.setExclusive(False)
        self.A.setChecked(False)
        self.B.setChecked(False)
        self.C.setChecked(False)
        self.button_group1.setExclusive(True)            

    def SinavSiklariniKaydet(self):
        TiklananSik = self.sender()
        TiklananSikMetni = TiklananSik.property("bilgi")

        self.SinavSiklariKaydet[self.sinav_soru_sayaci - 1] = (str(self.sinav_soru.text()), str(getattr(self, TiklananSikMetni).text()), str(TiklananSikMetni))

    def SinavMetinleriniSeslendirma(self, pos):
        ButonPozisyonu = pos - QPoint(160, 0)
        SeslendirilecekMetin = self.childAt(ButonPozisyonu).text()

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

        RandomSayi = random.randint(1,1111111)
        cikti = gTTS(text=SeslendirilecekMetin, lang=language, slow=False)
        cikti.save("dosya/ses" + str(RandomSayi) + ".mp3")
        playsound("dosya/ses" + str(RandomSayi) + ".mp3")

    ### SİNAV MENÜSÜ İÇ İŞLEMLERİ
    def KelimeEklemeButonuBasildi(self):
        ingilizce_kelime = self.line_edit_kelime_ingilizce.text()
        turkce_kelime = self.line_edit_kelime_turkce.text()
        ingilizce_cumle = self.line_edit_ingilizce_cümle.text()
        turkce_cumle = self.line_edit_türkçe_cümle.text()

        if ingilizce_kelime and turkce_kelime and ingilizce_cumle and turkce_cumle:
            conn = sqlite3.connect('database/Kelimeler.db')
            cursor = conn.cursor()
            ingilizce_lower = ingilizce_kelime.lower()

            cursor.execute("SELECT * FROM Kelimeler WHERE LOWER(ingilizce_kelime) = ?", (ingilizce_lower,))
            existing_word = cursor.fetchone()

            if existing_word:
                self.label_kelime_ekle.setText("Bu Kelime Zaten Mevcut. Başka Bir Kelime Deneyiniz.")
            else:
                if self.ResimSecmeYapilmasi == 0:
                    self.label_kelime_ekle.setText("Lütfen Resim Seçiniz.")
                else:
                    self.ResimDosyaYolu = 'resim/' + f"{ingilizce_kelime}" + '.png'
                    self.KaydedilecekResim = cv2.resize(self.KaydedilecekResim, (100, 100))
                    cv2.imwrite(self.ResimDosyaYolu, self.KaydedilecekResim)

                    cursor.execute(
                        "INSERT INTO Kelimeler (ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2, resim) VALUES (?, ?, ?, ?, ?)",
                        (ingilizce_kelime, turkce_kelime, ingilizce_cumle, turkce_cumle, self.ResimDosyaYolu))

                    conn.commit()

                    self.label_kelime_ekle.setText("Başarıyla Eklenmiştir.")
                    self.ResimSecmeYapilmasi = 0
        else:
            self.label_kelime_ekle.setText("Lütfen Bilgileri Eksiksiz Giriniz")
        self.GenelIslemleriSifirla()

    def SinavSonuAnaliz(self):
        for sayac in range(self.kullan_soru_sayisi):
            if self.SinavSiklariKaydet[sayac][0] == 0:
                self.test_bos_cevap_sayisi += 1
            elif str(self.SinavSiklariKaydet[sayac][1]) == str(self.Sorular[sayac]["cevabı"]):
                self.test_dogru_cevap_sayisi += 1

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
                self.test_yanlis_cevap_sayisi += 1

        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE Kullaniciİstatistik 
                SET dogru_cevaplar = dogru_cevaplar + ?, yanlis_cevaplar = yanlis_cevaplar + ?, bos_cevaplar = bos_cevaplar + ?, toplam_sorular = toplam_sorular + ?
                WHERE kullanici_id = ?''', (
            self.test_dogru_cevap_sayisi, self.test_yanlis_cevap_sayisi, self.test_bos_cevap_sayisi, self.sinav_soru_sayaci,
            self.kullanici_id))

        conn.commit()
        conn.close()

        self.yazi_dogru_sayi.setText(str(self.test_dogru_cevap_sayisi))
        self.yazi_yanlis_sayi.setText(str(self.test_yanlis_cevap_sayisi))
        self.yazi_bos_sayi.setText(str(self.test_bos_cevap_sayisi))
        self.yazi_toplam_sayi.setText(str(self.sinav_soru_sayaci))

        self.kullan_soru_sayisi = self.sinav_soru_sayisi

    def AnalizleriYazdir(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])

        conn = sqlite3.connect('database/KullaniciBilgileri.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Kullaniciİstatistik WHERE kullanici_id = ?;', (self.kullanici_id,))
        kullanici_verileri = cursor.fetchone()
        conn.commit()
        conn.close()

        c = canvas.Canvas(file_path, pagesize=letter)
        c.setFont("Helvetica", 16)
        c.drawString(250, 750, "- ANALIZ -")
        c.drawString(15, 720, "Toplam Dogru Sayisi : " + str(kullanici_verileri[1]) + "    Toplam Yanlis Sayisi : " + str(kullanici_verileri[2]) + "    Toplam Bos Sayisi : " + str(kullanici_verileri[3]))
        c.drawString(115, 690, "Toplam Soru Sayisi : " + str(kullanici_verileri[4]) + "    Ortalama : %" + str("{:.2f}".format((kullanici_verileri[1] / kullanici_verileri[4])*100)))

        c.drawString(25, 530, "Ezberlenmis")

        c.drawString(180, 530, self._ezber_yazi.text())

        yeni_metinler = []
        for i in range(1, 7):
            metin = getattr(self, f'_{i}lik_yazi').text()
            yeni_metin = metin.replace("\n", "      ")
            yeni_metinler.append(yeni_metin)

        yıldızlar = ["★" * i for i in range(6, 0, -1)]
        y_pos = 500
        for yıldız, metin in zip(yıldızlar, reversed(yeni_metinler)):
            c.drawString(25, y_pos, yıldız)
            c.drawString(180, y_pos, self.TrIngTranslate(metin))
            y_pos -= 30

        c.save()

    def TrIngTranslate(self, metin):
        turkce_karakterler = "çÇğĞıİöÖşŞüÜ"
        ingilizce_karakterler = "cCgGiIoOsSuU"
        ceviri_tablosu = str.maketrans(turkce_karakterler, ingilizce_karakterler)
        return metin.translate(ceviri_tablosu)

    def ResimSecmeButonuBasildi(self):
        options = QFileDialog.Options()
        self.DosyaAdi, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "","Resim Dosyaları (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        self.KaydedilecekResim = cv2.imread(self.DosyaAdi)
        if self.DosyaAdi:
            pixmap = QPixmap(self.DosyaAdi)
            self.label_ekleme_resim.setPixmap(pixmap.scaled(self.label_ekleme_resim.size(), aspectRatioMode=True))
            self.label_ekleme_resim.setScaledContents(True)
            self.ResimSecmeYapilmasi = 1

    def TabloyaKelimeleriKoy(self):
        conn = sqlite3.connect('database/Kelimeler.db')
        cursor = conn.cursor()
        cursor.execute("SELECT ingilizce_kelime, türkçe_kelime, cümle_1, cümle_2, resim FROM Kelimeler")
        veriler = cursor.fetchall()

        if veriler:
            row_count = len(veriler)
            column_count = len(veriler[0])

            self.KelimelerTablosu.setRowCount(row_count)
            self.KelimelerTablosu.setColumnCount(column_count)

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
    def GenelIslemleriSifirla(self):
        self.test_dogru_cevap_sayisi = 0
        self.test_yanlis_cevap_sayisi = 0
        self.test_bos_cevap_sayisi = 0

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
    def BaslatilmaIslemleri(self):
        self.ResimSecmeYapilmasi = 0
        self.sinav_soru_sayisi = 5
        self.kullan_soru_sayisi = self.sinav_soru_sayisi
        self.dil = 'ing'
        self.SinavSiklariKaydet = [[0 for j in range(2)] for i in range(25)]
        self.VeritabaniKontrolEt()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    giris_sayfasi = Ana_Pencere123()
    giris_sayfasi.show()
    sys.exit(app.exec_())