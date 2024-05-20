import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
from Ana_menu import *

class Buton_Olustur_Modul(QWidget):
    def createButtons(self):
        buttons_info = [
            {"text": "<-- ÇIKIŞ -->", "position": (10, 560, 150, 30), "function": self.exitFunction},
            {"text": "<-- AYARLAR -->", "position": (10, 520, 150, 30), "function": self.ayarlarFunction},
            {"text": "<-- MENÜ 1 -->", "position": (10, 80, 180, 30), "function": self.menu1Function},
            {"text": "<-- MENÜ 2 -->", "position": (10, 120, 180, 30), "function": self.menu2Function},
            {"text": "<-- MENÜ 3 -->", "position": (10, 160, 180, 30), "function": self.menu3Function},
            {"text": "<-- MENÜ 4 -->", "position": (10, 200, 180, 30), "function": self.menu4Function},
        ]

        for button_info in buttons_info:
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])