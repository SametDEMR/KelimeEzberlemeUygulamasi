import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class LabelOlustur(QWidget):
    def Olustur(self):
        self.labels = []
        labels_info = [
            {"bilgi": "label_giris", "text": "", "position": (200, 400, 800, 40)},
            {"bilgi": "label_sinav_sayac", "text": "", "position": (350, 540, 500, 40)},
            {"bilgi": "label_kelime_ekle", "text": "", "position": (200, 460, 800, 40)},

            {"bilgi": "cümle_soru", "text": "CÜMLE SORU", "position": (250, 100, 700, 40)},

            {"bilgi": "label_metin", "text": "Yukarıda Verilen Kelimenin Nedir?", "position": (300, 270, 600, 40)},
            {"bilgi": "label_ayarlar_dil", "text": "DİLİ DEĞİŞTİRİNİZ", "position": (300, 130, 600, 40)},
            {"bilgi": "label_ayarlar_sayi", "text": "SORU SAYISINI DEĞİŞTİRİNİZ", "position": (300, 380, 600, 40)},

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
                    font-size: 30px;
                }
            """)

            label.setAlignment(Qt.AlignCenter)

            if bilgi == 'cümle_soru':
                label.setStyleSheet("""
                    QLabel {
                        color: #FFFFFF;
                        font-family: "Arial", sans-serif; /* Yazı fontu */
                        font-size: 30px;
                        border: 3px solid #FFA500;
                        border-radius: 20px;
                    }
                """)

            self.labels.append(label)
            setattr(self, bilgi, label)
