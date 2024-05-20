import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale

from ana_menu import *

class MetinSesButonOlustur(QWidget):
    def Olustur(self):
        self.buttons = []
        self.selected_button = None

        buttons_info = [
            {"bilgi": "ses_soru", "text": "", "position": (760, 40, 40, 40)},
            {"bilgi": "ses_soru_cümle", "text": "", "position": (910, 100, 40, 40)},

            {"bilgi": "ses_A", "text": "", "position": (410, 400, 40, 40)},
            {"bilgi": "ses_B", "text": "", "position": (660, 400, 40, 40)},
            {"bilgi": "ses_C", "text": "", "position": (910, 400, 40, 40)},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])

            button.clicked.connect(lambda _, pos=button.pos(): self.seslendirme(pos))

            button.setStyleSheet("""
                QPushButton {
                    border: 2px solid #FFB347;
                    border-radius: 20px;
                    padding: 10px 20px;
                    background-image: url('program/ses1.png');
                    background-repeat: no-repeat;
                    background-position: center;
                    }
                QPushButton:hover {
                        background-image: url('program/ses2.png');
                        background-repeat: no-repeat;
                        background-position: center;
                    }
            }
            """)

            self.buttons.append(button)
            setattr(self, bilgi, button)
