import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

from ana_menu import *

class AnalizOlustur(QWidget):
    def Olustur(self):
        self.button_group = QButtonGroup()
        buttons_info = [
            {"bilgi": "toplam_dogru_sayi", "text": "TOPLAM DOĞRU SAYISI : ", "position": (130, 100, 300, 40)},
            {"bilgi": "toplam_yanlis_sayi", "text": "TOPLAM YANLIŞ SAYISI : ", "position": (450, 100, 300, 40)},
            {"bilgi": "toplam_bos_sayi", "text": "TOPLAM BOŞ SAYISI : ", "position": (770, 100, 300, 40)},
            {"bilgi": "toplam_soru_sayi", "text": "TOPLAM SORU SAYISI : ", "position": (290, 160, 300, 40)},
            {"bilgi": "ortalama_sayi", "text": "ORTALAMA : ", "position": (610, 160, 300, 40)},

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