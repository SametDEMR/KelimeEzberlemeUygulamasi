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
            {"bilgi": "toplam_dogru_sayi", "text": "TOPLAM DOĞRU SAYISI : ", "position": (130, 100, 300, 40)},
            {"bilgi": "toplam_yanlis_sayi", "text": "TOPLAM YANLIŞ SAYISI : ", "position": (450, 100, 300, 40)},
            {"bilgi": "toplam_bos_sayi", "text": "TOPLAM BOŞ SAYISI : ", "position": (770, 100, 300, 40)},
            {"bilgi": "toplam_soru_sayi", "text": "TOPLAM SORU SAYISI : ", "position": (290, 160, 300, 40)},
            {"bilgi": "ortalama_sayi", "text": "ORTALAMA : ", "position": (610, 160, 300, 40)},

            {"bilgi": "yazi_dogru", "text": "DOĞRU", "position": (140, 250, 200, 40)},
            {"bilgi": "yazi_yanlis", "text": "YANLIŞ", "position": (380, 250, 200, 40)},
            {"bilgi": "yazi_bos", "text": "BOŞ", "position": (620, 250, 200, 40)},
            {"bilgi": "yazi_toplam", "text": "TOPLAM SORU", "position": (860, 250, 200, 40)},

            {"bilgi": "yazi_dogru_sayi", "text": "DOĞRU", "position": (140, 310, 200, 40)},
            {"bilgi": "yazi_yanlis_sayi", "text": "YANLIŞ", "position": (380, 310, 200, 40)},
            {"bilgi": "yazi_bos_sayi", "text": "BOŞ", "position": (620, 310, 200, 40)},
            {"bilgi": "yazi_toplam_sayi", "text": str(self.sinav_soru_sayisi), "position": (860, 310, 200, 40)},

            {"bilgi": "_6lik", "text": "★★★★★★", "position": (10, 250, 180, 40)},
            {"bilgi": "_5lik", "text": "★★★★★", "position": (210, 250, 180, 40)},
            {"bilgi": "_4lik", "text": "★★★★", "position": (410, 250, 180, 40)},
            {"bilgi": "_3lik", "text": "★★★", "position": (610, 250, 180, 40)},
            {"bilgi": "_2lik", "text": "★★", "position": (810, 250, 180, 40)},
            {"bilgi": "_1lik", "text": "★", "position": (1010, 250, 180, 40)},

            {"bilgi": "_6lik_yazi", "text": "", "position": (10, 300, 180, 200)},
            {"bilgi": "_5lik_yazi", "text": "", "position": (210, 300, 180, 200)},
            {"bilgi": "_4lik_yazi", "text": "", "position": (410, 300, 180, 200)},
            {"bilgi": "_3lik_yazi", "text": "", "position": (610, 300, 180, 200)},
            {"bilgi": "_2lik_yazi", "text": "", "position": (810, 300, 180, 200)},
            {"bilgi": "_1lik_yazi", "text": "", "position": (1010, 300, 180, 200)},

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