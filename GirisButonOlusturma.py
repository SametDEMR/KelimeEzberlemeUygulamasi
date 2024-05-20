import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale

from Ana_menu import *

class Giris_Buton_Olustur(QWidget):
    def Giris_Buton(self):
        self.buttons = []
        buttons_info = [
            {"bilgi": "buton_geri1", "text": "GERİ", "position": (10, 10, 200, 40), "function": self.geri},

            {"bilgi": "buton_giriş", "text": "GİRİŞ", "position": (500, 440, 200, 40), "function": self.giris},
            {"bilgi": "buton_sifreunuttum", "text": "ŞİFREMİ UNUTTUM", "position": (380, 500, 200, 40), "function": self.sifre_unuttum},
            {"bilgi": "buton_kayit", "text": "KAYIT", "position": (620, 500, 200, 40), "function": self.kayit},
            {"bilgi": "buton_sifre_goster", "text": "", "position": (710, 240, 40, 40), "function": self.sifre_goster_gizle},

            {"bilgi": "buton_kaydol", "text": "KAYDOL", "position": (500, 440, 200, 40), "function": self.kaydol},
            {"bilgi": "buton_sifre_getir", "text": "ŞİFREMİ UNUTTUM", "position": (500, 440, 200, 40), "function": self.sifre_getir},
        ]

        for button_info in buttons_info:
            bilgi = button_info["bilgi"]
            button = QPushButton(button_info["text"], self)
            button.setGeometry(*button_info["position"])
            button.clicked.connect(button_info["function"])

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

            self.buttons.append(button)
            setattr(self, bilgi, button)


            if bilgi == "buton_sifre_goster":
                button.setStyleSheet("""
                    QPushButton {
                        border: 2px solid #FFA500;
                        border-radius: 20px;
                        padding: 10px 20px;
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