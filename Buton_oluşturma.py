import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale

from Ana_menu import *

class Buton_Olustur_Modul(QWidget):
    def createButtons(self):
        buttons_info = [
            {"bilgi": "1", "text": "ÇIKIŞ", "position": (10, 560, 180, 30), "function": self.exitFunction},
            {"bilgi": "2", "text": "AYARLAR", "position": (10, 520, 180, 30), "function": self.ayarlarFunction},
            {"bilgi": "3", "text": "SINAV SAYFASI", "position": (10, 80, 180, 30), "function": self.menu1Function},
            {"bilgi": "4", "text": "RAPOR SAYFASI", "position": (10, 120, 180, 30), "function": self.menu2Function},
            {"bilgi": "5", "text": "KELİME EKLEME", "position": (10, 160, 180, 30), "function": self.menu3Function},

            {"bilgi": "6", "text": "SINAVA BAŞLA", "position": (610, 285, 180, 30), "function": self.baslaFunction},
            {"bilgi": "7", "text": "SONRAKİ SORU", "position": (1010, 560, 180, 30), "function": self.sonrakisoruFunction},
            {"bilgi": "8", "text": "ÖNCEKİ SORU", "position": (200, 560, 180, 30), "function": self.oncekisoruFunction},
        ]

        for button_info in buttons_info:
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])