import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class LabelOlustur(QWidget):
    def Olustur(self):
        self.labels = []
        labels_info = [
            {"bilgi": "label_giris", "text": "", "position": (200, 400, 800, 40)},
            {"bilgi": "label_sinav", "text": "", "position": (350, 540, 500, 40)},

            {"bilgi": "label_metin", "text": "Yukarıda verilen kelimenin Türkçesi nedir?", "position": (300, 80, 600, 40)},
            {"bilgi": "label_ayarlar", "text": "SORU SAYISINI DEĞİŞTİRİNİZ", "position": (300, 200, 600, 40)},

            {"bilgi": "label_resim", "text": "", "position": (550, 360, 100, 100)},
        ]

        for label_info in labels_info:
            bilgi = label_info["bilgi"]
            label = QLabel(label_info["text"], self)
            label.setGeometry(*label_info["position"])

            label.show()

            label.setStyleSheet("""
                QLabel {
                    color: #FFFFFF;
                    font-family: "Arial", sans-serif; /* Yazı fontu */
                    font-size: 25px;
                }
            """)

            label.setAlignment(Qt.AlignCenter)

            self.labels.append(label)
            setattr(self, bilgi, label)
