import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale

from ana_menu import *

class ButonOlustur(QWidget):
    def Olustur(self):
        self.buttons = []
        self.selected_button = None

        buttons_info = [
            {"bilgi": "buton_geri_giris", "text": "GERİ", "position": (10, 10, 200, 40), "function": self.geri_giris},
            {"bilgi": "buton_geri_sinav", "text": "GERİ", "position": (10, 10, 200, 40), "function": self.geri_sinav},


            {"bilgi": "buton_giriş", "text": "GİRİŞ", "position": (500, 440, 200, 40), "function": self.giris},
            {"bilgi": "buton_sifreunuttum", "text": "ŞİFREMİ UNUTTUM", "position": (280, 500, 200, 40), "function": self.sifre_unuttum},
            {"bilgi": "buton_kayit", "text": "KAYIT", "position": (720, 500, 200, 40), "function": self.kayit},
            {"bilgi": "buton_sifre_goster", "text": "", "position": (710, 240, 40, 40), "function": self.sifre_goster_gizle},


            {"bilgi": "buton_kaydol", "text": "KAYDOL", "position": (500, 440, 200, 40), "function": self.kayit},
            {"bilgi": "buton_sifre_getir", "text": "ŞİFREMİ UNUTTUM", "position": (500, 450, 200, 40), "function": self.sifre_unuttum},


            {"bilgi": "buton_sinav", "text": "SINAV", "position": (500, 100, 200, 40), "function": self.sinav},
            {"bilgi": "buton_analiz", "text": "ANALİZ", "position": (500, 160, 200, 40), "function": self.analiz},
            {"bilgi": "buton_soru_ekleme", "text": "KELİME EKLEME", "position": (500, 220, 200, 40), "function": self.kelime_ekleme},
            {"bilgi": "buton_ayarlar", "text": "AYARLAR", "position": (500, 280, 200, 40), "function": self.ayarlar},
            {"bilgi": "buton_cikis", "text": "ÇIKIŞ", "position": (500, 500, 200, 40), "function": self.cikis},


            {"bilgi": "buton_sinav_basla", "text": "SINAVA BAŞLA", "position": (500, 280, 200, 40), "function": self.sonraki_soru},
            {"bilgi": "buton_sonraki_soru", "text": "SONRAKİ SORU", "position": (960, 540, 200, 40), "function": self.sonraki_soru},
            {"bilgi": "buton_önceki_soru", "text": "ÖNCEKİ SORU", "position": (20, 540, 200, 40), "function": self.onceki_soru},
            {"bilgi": "buton_sinav_bitir", "text": "SINAVI BİTİR", "position": (960, 540, 200, 40), "function": self.analiz},


            {"bilgi": "buton_kelime_ekle_ekle", "text": "KELİME EKLE", "position": (500, 500, 200, 40), "function": self.kelime_ekleme},
            {"bilgi": "buton_resim_sec", "text": "RESİM SEÇ", "position": (500, 240, 200, 40), "function": self.resim_sec},

            {"bilgi": "yazdir", "text": "YAZDIR", "position": (450, 520, 300, 40), "function": self.yazdir},
            {"bilgi": "analiz_geri", "text": "GERİ", "position": (10, 10, 200, 40), "function": self.analiz_geri},
            {"bilgi": "analiz_sayisal", "text": "SAYISAL ANALİZ", "position": (500, 160, 200, 40), "function": self.analiz_sayisal},
            {"bilgi": "analiz_sozel", "text": "KELİME ANALİZ", "position": (500, 220, 200, 40), "function": self.analiz_sozel},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFA500;
                    border-radius: 20px;
                    color: #FFFFFF;
                    font-size: 16px;
                    padding: 0px 0px;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            self.buttons.append(button)
            setattr(self, bilgi, button)


            if bilgi == "buton_sifre_goster":
                button.setStyleSheet("""
                    QPushButton {
                        border: 2px solid #FFA500;
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
                button.clicked.connect(self.sifre_goster_gizle)

            if bilgi == "buton_cikis" or bilgi == "buton_sinav_bitir":
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #FF0000;
                        border-radius: 20px;
                        color: #FFFFFF;
                        font-size: 16px;
                        padding: 0px 0px;
                    }
                    QPushButton:hover {
                        background-color: #CE0000;
                    }
                """)