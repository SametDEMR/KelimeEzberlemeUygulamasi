import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class LabelOlustur(QWidget):
    def Olustur(self):
        self.labels = []
        labels_info = [
            {"bilgi": "label_giris", "text": "", "position": (200, 400, 800, 40)},
            {"bilgi": "label_sinav_sayac", "text": "", "position": (350, 540, 500, 40)},
            {"bilgi": "label_kelime_ekle", "text": "", "position": (350, 460, 500, 40)},

            {"bilgi": "label_metin", "text": "Yukarıda Verilen Kelimenin Türkçesi Nedir?", "position": (300, 270, 600, 40)},
            {"bilgi": "label_ayarlar", "text": "SORU SAYISINI DEĞİŞTİRİNİZ", "position": (300, 200, 600, 40)},

            {"bilgi": "label_ekleme_resim", "text": "", "position": (550, 300, 100, 100)},
            {"bilgi": "label_resim_soru", "text": "", "position": (550, 160, 100, 100)},
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
