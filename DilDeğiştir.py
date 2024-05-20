import sys
from PyQt5.QtWidgets import *


class DilButonOlustur(QWidget):
    def Olustur(self):
        self.button_group3 = QButtonGroup()
        buttons_info = [
            {"bilgi": "ing", "text": "İNGİLİZCE", "position": (370, 200, 200, 40)},
            {"bilgi": "tr", "text": "TÜRKÇE", "position": (610, 200, 200, 40)},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setProperty("bilgi", bilgi)
            button.setGeometry(*button_info["position"])
            button.setCheckable(True)
            self.button_group1.addButton(button)

            button.clicked.connect(self.ayarlar)

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
