import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale

from Ana_menu import *

class Buton_Olustur_Modul(QWidget):
    def createButtons(self):
        self.buttons = []
        buttons_info = [
            {"bilgi": "buton_giriş", "text": "GİRİŞ", "position": (500, 340, 200, 40), "function": self.login},
            {"bilgi": "buton_sifreunuttum", "text": "ŞİFREMİ UNUTTUM", "position": (380, 400, 200, 40), "function": self.sifre_unuttum},
            {"bilgi": "buton_kayit", "text": "KAYIT", "position": (620, 400, 200, 40), "function": self.kayit},
            {"bilgi": "buton_sifre_goster", "text": "", "position": (710, 240, 40, 40), "function": self.sifre_goster_gizle},
            {"bilgi": "buton_geri", "text": "GERİ", "position": (10, 10, 200, 40), "function": self.geri},
            {"bilgi": "buton_kaydol", "text": "KAYDOL", "position": (500, 400, 200, 40), "function": self.kaydol},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])
            button.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    border: 0px solid #2980b9;
                    border-radius: 20px;
                    color: white;
                    font-size: 16px;
                    padding: 10px 20px;
                    transition: background-color 0.3s ease; /* Renk geçiş efekti */
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            button.setFont(QFont("Times New Roman", 12))
            self.buttons.append(button)
            setattr(self, bilgi, button)

            if bilgi == "buton_sifre_goster":
                button.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border: 2px solid black;
                        border-radius: 20px;
                        color: white;
                        font-size: 16px;
                        padding: 10px 20px;
                        transition: background-color 0.3s ease; /* Renk geçiş efekti */
                        background-image: url('kapalı.png');
                        background-repeat: no-repeat;
                        background-position: center;
                    }
                    QPushButton:checked {
                        background-image: url('açık.png');
                        background-repeat: no-repeat;
                        background-position: center;
                    }
                }
                """)
                button.setCheckable(True)  # Butonun durumunu izlemek için kontrollü yapma
                button.clicked.connect(self.sifre_goster_gizle)  # Butona tıklandığında işlevi çağır


