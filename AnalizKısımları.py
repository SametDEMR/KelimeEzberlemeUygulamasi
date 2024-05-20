import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

from ana_menu import *

class SinavSonuAnaliz(QWidget):
    def Olustur(self):
        self.button_group = QButtonGroup()
        buttons_info = [
            {"bilgi": "yazi_dogru", "text": "DOĞRU", "position": (140, 250, 200, 40)},
            {"bilgi": "yazi_yanlis", "text": "YANLIŞ", "position": (380, 250, 200, 40)},
            {"bilgi": "yazi_bos", "text": "BOŞ", "position": (620, 250, 200, 40)},
            {"bilgi": "yazi_toplam", "text": "TOPLAM SORU", "position": (860, 250, 200, 40)},

            {"bilgi": "yazi_dogru_sayi", "text": "DOĞRU", "position": (140, 310, 200, 40)},
            {"bilgi": "yazi_yanlis_sayi", "text": "YANLIŞ", "position": (380, 310, 200, 40)},
            {"bilgi": "yazi_bos_sayi", "text": "BOŞ", "position": (620, 310, 200, 40)},
            {"bilgi": "yazi_toplam_sayi", "text": str(self.sinav_soru_sayisi), "position": (860, 310, 200, 40)},


            {"bilgi": "toplam_dogru_yazi", "text": "TOPLAM DOĞRU SAYISI", "position": (130, 214, 300, 40)},
            {"bilgi": "toplam_yanlis_yazi", "text": "TOPLAM YANLIŞ SAYISI", "position": (450, 214, 300, 40)},
            {"bilgi": "toplam_bos_yazi", "text": "TOPLAM BOŞ SAYISI", "position": (770, 214, 300, 40)},
            {"bilgi": "toplam_soru_yazi", "text": "TOPLAM SORU SAYISI", "position": (290, 310, 300, 40)},
            {"bilgi": "ortalama_yazi", "text": "ORTALAMA", "position": (610, 310, 300, 40)},

            {"bilgi": "toplam_dogru_sayi", "text": "", "position": (130, 250, 300, 40)},
            {"bilgi": "toplam_yanlis_sayi", "text": "", "position": (450, 250, 300, 40)},
            {"bilgi": "toplam_bos_sayi", "text": "", "position": (770, 250, 300, 40)},
            {"bilgi": "toplam_soru_sayi", "text": "", "position": (290, 346, 300, 40)},
            {"bilgi": "ortalama_sayi", "text": "", "position": (610, 346, 300, 40)},


            {"bilgi": "_6lik", "text": "★★★★★★", "position": (10, 94, 180, 40)},
            {"bilgi": "_5lik", "text": "★★★★★", "position": (210, 94, 180, 40)},
            {"bilgi": "_4lik", "text": "★★★★", "position": (410, 94, 180, 40)},
            {"bilgi": "_3lik", "text": "★★★", "position": (610, 94, 180, 40)},
            {"bilgi": "_2lik", "text": "★★", "position": (810, 94, 180, 40)},
            {"bilgi": "_1lik", "text": "★", "position": (1010, 94, 180, 40)},

            {"bilgi": "_6lik_yazi", "text": "", "position": (10, 130, 180, 200)},
            {"bilgi": "_5lik_yazi", "text": "", "position": (210, 130, 180, 200)},
            {"bilgi": "_4lik_yazi", "text": "", "position": (410, 130, 180, 200)},
            {"bilgi": "_3lik_yazi", "text": "", "position": (610, 130, 180, 200)},
            {"bilgi": "_2lik_yazi", "text": "", "position": (810, 130, 180, 200)},
            {"bilgi": "_1lik_yazi", "text": "", "position": (1010, 130, 180, 200)},

            {"bilgi": "_ezber_yazi", "text": "", "position": (100, 350, 1000, 180)},
            {"bilgi": "_ezber", "text": "EZBERLENMİŞ", "position": (100, 350, 1000, 40)},

        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setProperty("bilgi", bilgi)
            button.setGeometry(*button_info["position"])

            button.setEnabled(False)

            button.setStyleSheet("""
                QPushButton {
                    background-color: #1E468F;
                    border: 4px solid #FFB347;
                    border-radius: 20px;
                    color: #FFFFFF;
                    font-size: 25px;
                }
            """)

            setattr(self, bilgi, button)