import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

from GirisButonOlusturma import *
from GirisTextBoxOlusturma import *
from GirisLabelOlusturma import *
from GirisShowHide import *
from SinavButonOlusturma import *
from SinavShowHide import *
from SinavLabelOlusturma import *

class Sinav_Buton_Olustur(QWidget):
    def Sinav_Buton(self):
        self.buttons = []
        buttons_info = [
            {"bilgi": "buton_geri2", "text": "GERİ", "position": (10, 10, 200, 40), "function": self.geri2},
            {"bilgi": "buton_sinav", "text": "SINAV", "position": (500, 100, 200, 40), "function": self.sinav},
            {"bilgi": "buton_soru_ekleme", "text": "KELİME EKLEME", "position": (500, 160, 200, 40), "function": self.soru_ekleme},
            {"bilgi": "buton_analiz", "text": "ANALİZ", "position": (500, 220, 200, 40), "function": self.analiz},
            {"bilgi": "buton_çıkış", "text": "ÇIKIŞ", "position": (500, 500, 200, 40), "function": self.cikis},

            {"bilgi": "buton_sonraki_soru", "text": "SONRAKİ SORU", "position": (960, 540, 200, 40), "function": self.sonraki_soru},
            {"bilgi": "buton_önceki_soru", "text": "ÖNCEKİ SORU", "position": (20, 540, 200, 40), "function": self.onceki_soru},

            {"bilgi": "buton_soru_ekle_ekle", "text": "SORU EKLE", "position": (500, 500, 200, 40), "function": self.soruyu_ekle},

            {"bilgi": "sik_a", "text": "A", "position": (300, 280, 40, 40), "function": self.buton_yazi_gonder},
            {"bilgi": "sik_b", "text": "B", "position": (300, 340, 40, 40), "function": self.buton_yazi_gonder},
            {"bilgi": "sik_c", "text": "C", "position": (300, 400, 40, 40), "function": self.buton_yazi_gonder},
            {"bilgi": "sik_d", "text": "D", "position": (300, 460, 40, 40), "function": self.buton_yazi_gonder},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])

            if bilgi.startswith("sik_"):
                # Connect each answer button to the method buton_yazi_gonder
                button.clicked.connect(lambda _, btn=button: self.buton_yazi_gonder(btn))
            else:
                button.clicked.connect(button_info["function"])

            button.show()

            button.setStyleSheet("""
                        QPushButton {
                            background-color: #FFA500;
                            border: 2px solid #FFA500;
                            border-radius: 20px;
                            color: #FFFFFF;
                            font-size: 16px;
                            padding: 0px 0px;
                        }
                        QPushButton:hover {
                            background-color: #FF9900;
                        }
                    """)