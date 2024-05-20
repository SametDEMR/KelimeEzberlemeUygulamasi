import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

from AAnaMenu import *

class Analizler(QWidget):
    def SinavSonuAnalizSayfasi(self):
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

    def AnaAnalizSayfasi(self):
        self.button_group = QButtonGroup()
        buttons_info = [
            {"bilgi": "toplam_dogru_yazi", "text": "TOPLAM DOĞRU SAYISI", "position": (130, 70, 300, 40)},
            {"bilgi": "toplam_yanlis_yazi", "text": "TOPLAM YANLIŞ SAYISI", "position": (450, 70, 300, 40)},
            {"bilgi": "toplam_bos_yazi", "text": "TOPLAM BOŞ SAYISI", "position": (770, 70, 300, 40)},
            {"bilgi": "toplam_soru_yazi", "text": "TOPLAM SORU SAYISI", "position": (290, 166, 300, 40)},
            {"bilgi": "ortalama_yazi", "text": "ORTALAMA", "position": (610, 166, 300, 40)},

            {"bilgi": "toplam_dogru_sayi", "text": "", "position": (130, 106, 300, 40)},
            {"bilgi": "toplam_yanlis_sayi", "text": "", "position": (450, 106, 300, 40)},
            {"bilgi": "toplam_bos_sayi", "text": "", "position": (770, 106, 300, 40)},
            {"bilgi": "toplam_soru_sayi", "text": "", "position": (290, 202, 300, 40)},
            {"bilgi": "ortalama_sayi", "text": "", "position": (610, 202, 300, 40)},
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