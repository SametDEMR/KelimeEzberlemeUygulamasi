import sys
from PyQt5.QtWidgets import *


class SiklikOlustur(QWidget):
    def Olustur(self):
        self.button_group2 = QButtonGroup()
        buttons_info = [
            {"bilgi": "_5", "text": "5", "position": (140, 450, 200, 40)},
            {"bilgi": "_10", "text": "10", "position": (380, 450, 200, 40)},
            {"bilgi": "_15", "text": "15", "position": (620, 450, 200, 40)},
            {"bilgi": "_20", "text": "20", "position": (860, 450, 200, 40)},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])

            button.clicked.connect(self.ayarlar_degistir)

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

            button.setCheckable(True)
            self.button_group2.addButton(button)

            setattr(self, bilgi, button)