import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale

from AAnaMenu import *

class ButonOlustur(QWidget):
    def GirisMenuButonlari(self):
        self.AnaMenuButonlari = []
        self.selected_button = None

        buttons_info = [
            {"bilgi": "CikisButonu", "text": "ÇIKIŞ", "position": (500, 500, 200, 40), "function": self.Cikis},

            {"bilgi": "GirisButonu", "text": "GİRİŞ", "position": (500, 440, 200, 40), "function": self.GirisButonunaBasildi},
            {"bilgi": "SifremiUnuttumButonu", "text": "ŞİFREMİ UNUTTUM", "position": (280, 500, 200, 40), "function": lambda: self.SayfalaraYonlendir("SifreUnuttumMenusu")},
            {"bilgi": "KayitOlmaButonu", "text": "KAYIT", "position": (720, 500, 200, 40), "function": lambda: self.SayfalaraYonlendir("KayitMenusu")},
            {"bilgi": "SifreGosterGizleButonu", "text": "", "position": (710, 240, 40, 40), "function": self.SifreGosterGizle},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFB347;
                    border-radius: 20px;
                    color: #333333;
                    font-size: 20px;
                    padding: 0px 0px;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            self.AnaMenuButonlari.append(button)
            setattr(self, bilgi, button)


            if bilgi == "SifreGosterGizleButonu":
                button.setStyleSheet("""
                    QPushButton {
                        border: 2px solid #FFB347;
                        border-radius: 20px;
                        padding: 10px 20px;
                        background-image: url('program/kapalı1.png');
                        background-repeat: no-repeat;
                        background-position: center;
                    }
                    QPushButton:checked {
                        background-image: url('program/açık1.png');
                        background-repeat: no-repeat;
                        background-position: center;
                    }
                    QPushButton:hover {
                        background-image: url('program/kapalı2.png');
                        background-repeat: no-repeat;
                        background-position: center;
                    }
                    QPushButton:checked:hover {
                    background-image: url('program/açık2.png');
                    background-repeat: no-repeat;
                    background-position: center;
                }
                }
                """)
                button.setCheckable(True)
                button.clicked.connect(lambda: self.SifreGosterGizle)

            if bilgi == "CikisButonu":
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #FF0000;
                        border-radius: 20px;
                        color: #333333;
                        font-size: 20px;
                        padding: 0px 0px;
                    }
                    QPushButton:hover {
                        background-color: #CE0000;
                    }
                """)

    def GirisMenuIcIslemButonlari(self):
        self.AnaMenuButonlari = []
        self.selected_button = None

        buttons_info = [
            {"bilgi": "GirisSayfasiGeriGitme", "text": "GERİ", "position": (10, 10, 200, 40), "function": lambda: self.SayfalaraYonlendir("GirisAnaMenu")},
            {"bilgi": "KaydolButonu", "text": "KAYDOL", "position": (500, 440, 200, 40), "function": self.KayitButonunaBasildi},
            {"bilgi": "SifremiGetirButonu", "text": "ŞİFREMİ UNUTTUM", "position": (500, 450, 200, 40), "function": self.SifreUnuttumButonunaBasildi},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFB347;
                    border-radius: 20px;
                    color: #333333;
                    font-size: 20px;
                    padding: 0px 0px;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            self.AnaMenuButonlari.append(button)
            setattr(self, bilgi, button)

    def SinavAnaMenuButonlari(self):
        self.buttons = []
        self.selected_button = None

        buttons_info = [
            {"bilgi": "SinavSayfasiButonu", "text": "SINAV", "position": (500, 100, 200, 40), "function": lambda: self.SayfalaraYonlendir("SinavaBaslamaOncesi")},
            {"bilgi": "AnalizSayfasiButonu", "text": "ANALİZ", "position": (500, 160, 200, 40), "function": lambda: self.SayfalaraYonlendir("AnalizSayfasi")},
            {"bilgi": "KelimelerSayfasiButonu", "text": "KELİMELER", "position": (500, 220, 200, 40), "function": lambda: self.SayfalaraYonlendir("Kelimeler")},
            {"bilgi": "SoruEklemeSayfasiButonu", "text": "KELİME EKLEME", "position": (500, 280, 200, 40), "function": lambda: self.SayfalaraYonlendir("SoruEklemeKismi")},
            {"bilgi": "AyarlarSayfasiButonu", "text": "AYARLAR", "position": (500, 340, 200, 40), "function": lambda: self.SayfalaraYonlendir("Ayarlar")},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFB347;
                    border-radius: 20px;
                    color: #333333;
                    font-size: 20px;
                    padding: 0px 0px;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            self.buttons.append(button)
            setattr(self, bilgi, button)

    def SinavMenuIcIslemButonlari(self):
        self.buttons = []
        self.selected_button = None

        buttons_info = [
            {"bilgi": "SinavAnaMenuGeriGitme", "text": "GERİ", "position": (10, 10, 200, 40), "function": lambda: self.SayfalaraYonlendir("SinavUygulamasiAnaMenu")},

            {"bilgi": "SinavaBaslaButonu", "text": "SINAVA BAŞLA", "position": (500, 280, 200, 40), "function": lambda: self.SayfalaraYonlendir("SinavaBaslamaSonrasi")},
            {"bilgi": "SonrakiSoruButonu", "text": "SONRAKİ SORU", "position": (960, 540, 200, 40), "function": lambda: self.SoruDegistir(1)},
            {"bilgi": "ÖncekiSoruButonu", "text": "ÖNCEKİ SORU", "position": (20, 540, 200, 40), "function": lambda: self.SoruDegistir(-1)},
            {"bilgi": "SinavBitirButonu", "text": "SINAVI BİTİR", "position": (960, 540, 200, 40), "function": lambda: self.SayfalaraYonlendir("SinavSonuAnaliz")},

            {"bilgi": "KelimeyiEkleButonu", "text": "KELİME EKLE", "position": (500, 500, 200, 40), "function": self.KelimeEklemeButonuBasildi},
            {"bilgi": "ResimSecmeButonu", "text": "RESİM SEÇ", "position": (500, 240, 200, 40), "function": self.ResimSecmeButonuBasildi},

            {"bilgi": "AnalizleriYazdir", "text": "YAZDIR", "position": (450, 520, 300, 40), "function": self.AnalizleriYazdir},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFB347;
                    border-radius: 20px;
                    color: #333333;
                    font-size: 20px;
                    padding: 0px 0px;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            self.buttons.append(button)
            setattr(self, bilgi, button)

            if bilgi == "SinavBitirButonu":
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #FF0000;
                        border-radius: 20px;
                        color: #333333;
                        font-size: 20px;
                        padding: 0px 0px;
                    }
                    QPushButton:hover {
                        background-color: #CE0000;
                    }
                """)

    def SinavSikButonlari(self):
        self.button_group1 = QButtonGroup()
        buttons_info = [
            {"bilgi": "SoruKelimeYeri", "text": "SORU YERİ", "position": (400, 40, 400, 40)},

            {"bilgi": "A", "text": "Buton 1", "position": (250, 400, 200, 40)},
            {"bilgi": "B", "text": "Buton 2", "position": (500, 400, 200, 40)},
            {"bilgi": "C", "text": "Buton 3", "position": (750, 400, 200, 40)},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setProperty("bilgi", bilgi)
            button.setGeometry(*button_info["position"])
            button.setCheckable(True)
            self.button_group1.addButton(button)

            if bilgi != "sinav_soru":
                button.clicked.connect(self.SinavSiklariniKaydet)

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFB347;
                    border-radius: 20px;
                    color: #FFFFFF;
                    font-size: 20px;
                    padding: 0px 0px;
                }
                QPushButton:checked {
                    background-color: #8B4513;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            setattr(self, bilgi, button)

            if bilgi == "sinav_soru":
                self.sinav_soru.setEnabled(False)

    def AyarlarSoruSayisiSecmeButonlari(self):
        self.button_group2 = QButtonGroup()
        buttons_info = [
            {"bilgi": "_5", "text": "5", "position": (140, 450, 200, 40)},
            {"bilgi": "_10", "text": "10", "position": (380, 450, 200, 40)},
            {"bilgi": "_15", "text": "15", "position": (620, 450, 200, 40)},
            {"bilgi": "_20", "text": "20", "position": (860, 450, 200, 40)},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])

            button.clicked.connect(self.Ayarlar)

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFB347;
                    border-radius: 20px;
                    color: #FFFFFF;
                    font-size: 20px;
                    padding: 0px 0px;
                }
                QPushButton:checked {
                    background-color: #8B4513  ;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            button.setCheckable(True)
            self.button_group2.addButton(button)

            setattr(self, bilgi, button)
    def SoruDilDegistirButonlari(self):
        self.button_group3 = QButtonGroup()
        buttons_info = [
            {"bilgi": "ing", "text": "İNGİLİZCE", "position": (370, 200, 200, 40)},
            {"bilgi": "tr", "text": "TÜRKÇE", "position": (610, 200, 200, 40)},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setProperty("bilgi", bilgi)
            button.setGeometry(*button_info["position"])
            button.setCheckable(True)
            self.button_group1.addButton(button)

            button.clicked.connect(self.Ayarlar)

            button.setStyleSheet("""
                       QPushButton {
                           background-color: #FFB347;
                           border-radius: 20px;
                           color: #FFFFFF;
                           font-size: 20px;
                           padding: 0px 0px;
                       }
                       QPushButton:checked {
                           background-color: #8B4513;
                       }
                       QPushButton:hover {
                           background-color: #FF6600;
                       }
                   """)

            setattr(self, bilgi, button)
    def MetinleriSeslendirmeButonlari(self):
        self.buttons = []
        self.selected_button = None

        buttons_info = [
            {"bilgi": "SoruKelimeMetniSeslendirme", "text": "", "position": (760, 40, 40, 40)},
            {"bilgi": "SoruCumleMetniSeslendirme", "text": "", "position": (910, 100, 40, 40)},

            {"bilgi": "ses_A", "text": "", "position": (410, 400, 40, 40)},
            {"bilgi": "ses_B", "text": "", "position": (660, 400, 40, 40)},
            {"bilgi": "ses_C", "text": "", "position": (910, 400, 40, 40)},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])

            button.clicked.connect(lambda _, pos=button.pos(): self.SinavMetinleriniSeslendirma(pos))

            button.setStyleSheet("""
                QPushButton {
                    border: 2px solid #FFB347;
                    border-radius: 20px;
                    padding: 10px 20px;
                    background-image: url('program/ses1.png');
                    background-repeat: no-repeat;
                    background-position: center;
                    }
                QPushButton:hover {
                        background-image: url('program/ses2.png');
                        background-repeat: no-repeat;
                        background-position: center;
                    }
            }
            """)

            self.buttons.append(button)
            setattr(self, bilgi, button)