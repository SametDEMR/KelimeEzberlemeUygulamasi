import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale

from Ana_menu import *

class Buton_Olustur_Modul(QWidget):
    def createButtons(self):
        self.buttons = []
        buttons_info = [
            {"bilgi": "buton_çıkış", "text": "ÇIKIŞ", "position": (10, 560, 180, 30), "function": self.exit},
            {"bilgi": "buton_ayarlar", "text": "AYARLAR", "position": (10, 520, 180, 30), "function": self.ayarlar},
            {"bilgi": "buton_sinav_sayfasi", "text": "SINAV SAYFASI", "position": (10, 80, 180, 30), "function": self.sinavSayfasi},
            {"bilgi": "buton_rapor_sayfasi", "text": "RAPOR SAYFASI", "position": (10, 120, 180, 30), "function": self.raporSayfasi},
            {"bilgi": "buton_kelime_ekleme", "text": "KELİME EKLEME", "position": (10, 160, 180, 30), "function": self.kelimeEkleme},
            {"bilgi": "buton_6", "text": "SINAVA BAŞLA", "position": (610, 285, 180, 30), "function": self.baslaFunction},
            {"bilgi": "buton_7", "text": "SONRAKİ SORU", "position": (1010, 560, 180, 30),"function": self.sonrakisoruFunction},
            {"bilgi": "buton_8", "text": "ÖNCEKİ SORU", "position": (200, 560, 180, 30), "function": self.oncekisoruFunction},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])
            self.buttons.append(button)
            setattr(self, bilgi, button)

