import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
import json

class SiklarOlustur(QWidget):
    def Olustur(self):
        self.button_group1 = QButtonGroup()
        buttons_info = [
            {"bilgi": "sinav_soru", "text": "SORU YERİ", "position": (400, 40, 400, 40), "function": self.cikis},

            {"bilgi": "A", "text": "Buton 1", "position": (250, 400, 200, 40), "function": self.siklari_kaydet},
            {"bilgi": "B", "text": "Buton 2", "position": (500, 400, 200, 40), "function": self.siklari_kaydet},
            {"bilgi": "C", "text": "Buton 3", "position": (750, 400, 200, 40), "function": self.siklari_kaydet},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setProperty("bilgi", bilgi)
            button.setGeometry(*button_info["position"])
            button.setCheckable(True)
            self.button_group1.addButton(button)

            button.clicked.connect(button_info["function"])

            button.setStyleSheet("""
                QPushButton {
                    background-color: #FFB347;
                    border-radius: 20px;
                    color: #333333;
                    font-size: 20px;
                    padding: 0px 0px;
                }
                QPushButton:checked {
                    background-color: #FF6600;
                }
                QPushButton:hover {
                    background-color: #FF6600;
                }
            """)

            setattr(self, bilgi, button)

            if bilgi == "sinav_soru":
                self.sinav_soru.setEnabled(False)
