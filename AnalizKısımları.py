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

            {"bilgi": "toplam_dogru_sayi", "text": "TOPLAM DOĞRU SAYISI : ", "position": (130, 60, 300, 40)},
            {"bilgi": "toplam_yanlis_sayi", "text": "TOPLAM YANLIŞ SAYISI : ", "position": (450, 60, 300, 40)},
            {"bilgi": "toplam_bos_sayi", "text": "TOPLAM BOŞ SAYISI : ", "position": (770, 60, 300, 40)},
            {"bilgi": "toplam_soru_sayi", "text": "TOPLAM SORU SAYISI : ", "position": (290, 120, 300, 40)},
            {"bilgi": "ortalama_sayi", "text": "ORTALAMA : ", "position": (610, 120, 300, 40)},


            {"bilgi": "_6lik", "text": "★★★★★★", "position": (10, 64, 180, 40)},
            {"bilgi": "_5lik", "text": "★★★★★", "position": (210, 64, 180, 40)},
            {"bilgi": "_4lik", "text": "★★★★", "position": (410, 64, 180, 40)},
            {"bilgi": "_3lik", "text": "★★★", "position": (610, 64, 180, 40)},
            {"bilgi": "_2lik", "text": "★★", "position": (810, 64, 180, 40)},
            {"bilgi": "_1lik", "text": "★", "position": (1010, 64, 180, 40)},

            {"bilgi": "_6lik_yazi", "text": "", "position": (10, 100, 180, 200)},
            {"bilgi": "_5lik_yazi", "text": "", "position": (210, 100, 180, 200)},
            {"bilgi": "_4lik_yazi", "text": "", "position": (410, 100, 180, 200)},
            {"bilgi": "_3lik_yazi", "text": "", "position": (610, 100, 180, 200)},
            {"bilgi": "_2lik_yazi", "text": "", "position": (810, 100, 180, 200)},
            {"bilgi": "_1lik_yazi", "text": "", "position": (1010, 100, 180, 200)},

            {"bilgi": "_ezber_yazi", "text": "", "position": (100, 320, 1000, 180)},
            {"bilgi": "_ezber", "text": "EZBERLENMİŞ", "position": (100, 320, 1000, 40)},

        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setProperty("bilgi", bilgi)
            button.setGeometry(*button_info["position"])

            button.setEnabled(False)

            button.setStyleSheet("""
                QPushButton {
                    background-color: #3c64c8;
                    border: 4px solid #FFA500;
                    border-radius: 20px;
                    color: #FFFFFF;
                    font-size: 20px;
                }
            """)

            setattr(self, bilgi, button)