import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

class SiklarOlustur(QWidget):
    def Olustur(self):
        self.button_group = QButtonGroup()
        buttons_info = [
            {"bilgi": "sinav_soru", "text": "SORU YERİ", "position": (500, 150, 200, 40), "function": self.cikis},
            {"bilgi": "A", "text": "Buton 1", "position": (140, 350, 200, 40), "function": self.siklari_kaydet},
            {"bilgi": "B", "text": "Buton 2", "position": (380, 350, 200, 40), "function": self.siklari_kaydet},
            {"bilgi": "C", "text": "Buton 3", "position": (620, 350, 200, 40), "function": self.siklari_kaydet},
            {"bilgi": "D", "text": "Buton 4", "position": (860, 350, 200, 40), "function": self.siklari_kaydet},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setProperty("bilgi", bilgi)
            button.setGeometry(*button_info["position"])
            button.setCheckable(True)
            self.button_group.addButton(button)

            button.clicked.connect(button_info["function"])

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFA500;
                    border-radius: 20px;
                    color: #FFFFFF;
                    font-size: 20px;
                    padding: 0px 0px;
                }
                QPushButton:checked {
                    background-color: #666666;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            setattr(self, bilgi, button)

            if bilgi == "sinav_soru":
                self.sinav_soru.setEnabled(False)
