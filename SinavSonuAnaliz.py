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
            {"bilgi": "cümle_1", "text": "CÜMLE 1", "position": (40, 300, 400, 40)},
            {"bilgi": "cümle_2", "text": "CÜMLE 2", "position": (40, 540, 400, 40)},
            {"bilgi": "cümle_3", "text": "CÜMLE 3", "position": (760, 300, 400, 40)},
            {"bilgi": "cümle_4", "text": "CÜMLE 4", "position": (760, 540, 400, 40)},

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
                    background-color: #3c64c8;
                    border: 4px solid #FFA500;
                    border-radius: 20px;
                    color: #FFFFFF;
                    font-size: 20px;
                }
            """)

            setattr(self, bilgi, button)