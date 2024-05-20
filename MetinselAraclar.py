import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPalette, QColor


class MetinselAraclar(QWidget):
    def GirisKismi(self):
        self.line_edits = []
        line_edit_info = [
            {"bilgi": "line_edit_kullanici_adi", "placeholder": "KULLANICI ADI", "position": (450, 180, 200, 40)},
            {"bilgi": "line_edit_sifre", "placeholder": "ŞİFRE", "position": (450, 240, 200, 40)},

            {"bilgi": "line_edit_isim", "placeholder": "İSİM", "position": (450, 120, 200, 40)},
            {"bilgi": "line_edit_soyisim", "placeholder": "SOYİSİM", "position": (450, 180, 200, 40)},
            {"bilgi": "line_edit_kaydol_kullanici_adi", "placeholder": "KULLANICI ADI", "position": (450, 240, 200, 40)},
            {"bilgi": "line_edit_kaydol_sifre", "placeholder": "ŞİFRE", "position": (450, 300, 200, 40)},
            {"bilgi": "line_edit_sifre_kullanici_adi", "placeholder": "KULLANICI ADI", "position": (450, 240, 200, 40)},
        ]

        for edit_info in line_edit_info:
            bilgi = edit_info["bilgi"]
            line_edit = QLineEdit(self)
            line_edit.setPlaceholderText(edit_info["placeholder"])
            line_edit.setGeometry(*edit_info["position"])

            palette = line_edit.palette()
            palette.setColor(QPalette.PlaceholderText, QColor("#333333"))
            line_edit.setPalette(palette)

            line_edit.setStyleSheet("""
            QLineEdit {
                color: #333333;
                border-radius: 20px;
                padding: 0 15px;
                background-color: #FFB347;
            }
            """)

            line_edit.setFixedWidth(300)
            line_edit.setFixedHeight(40)
            font = QFont()
            font.setPointSize(14)
            line_edit.setFont(font)
            self.line_edits.append(line_edit)
            setattr(self, bilgi, line_edit)

            if bilgi == "line_edit_sifre":
                line_edit.setEchoMode(QLineEdit.Password)

    def KelimeEkleme(self):
        self.line_edits = []
        line_edit_info = [
            {"bilgi": "line_edit_kelime_ingilizce", "placeholder": "KELİMENİN İNGİLİZCESİ", "position": (450, 60, 200, 40)},
            {"bilgi": "line_edit_kelime_turkce", "placeholder": "KELİMENİN TÜRKÇESİ", "position": (450, 120, 200, 40)},
            {"bilgi": "line_edit_ingilizce_cümle", "placeholder": "İNGİLİZCE CÜMLE", "position": (290, 180, 200, 40)},
            {"bilgi": "line_edit_türkçe_cümle", "placeholder": "TÜRKÇE CÜMLE", "position": (610, 180, 200, 40)},
        ]

        for edit_info in line_edit_info:
            bilgi = edit_info["bilgi"]
            line_edit = QLineEdit(self)
            line_edit.setPlaceholderText(edit_info["placeholder"])
            line_edit.setGeometry(*edit_info["position"])

            palette = line_edit.palette()
            palette.setColor(QPalette.PlaceholderText, QColor("#333333"))
            line_edit.setPalette(palette)

            line_edit.setStyleSheet("""
            QLineEdit {
                color: #333333;
                border-radius: 20px;
                padding: 0 15px;
                background-color: #FFB347;
            }
            """)

            line_edit.setFixedWidth(300)
            line_edit.setFixedHeight(40)
            font = QFont()
            font.setPointSize(14)
            line_edit.setFont(font)
            self.line_edits.append(line_edit)
            setattr(self, bilgi, line_edit)

    def Metinler(self):
        self.labels = []
        labels_info = [
            {"bilgi": "label_giris", "text": "", "position": (200, 400, 800, 40)},
            {"bilgi": "label_sinav_sayac", "text": "", "position": (350, 540, 500, 40)},
            {"bilgi": "label_kelime_ekle", "text": "", "position": (200, 460, 800, 40)},

            {"bilgi": "cümle_soru", "text": "CÜMLE SORU", "position": (250, 100, 700, 40)},
            {"bilgi": "label_resim_soru", "text": "", "position": (550, 160, 100, 100)},

            {"bilgi": "label_soru_metin", "text": "", "position": (200, 270, 800, 40)},
            {"bilgi": "label_ayarlar_dil", "text": "DİLİ DEĞİŞTİRİNİZ", "position": (300, 130, 600, 40)},
            {"bilgi": "label_ayarlar_sayi", "text": "SORU SAYISINI DEĞİŞTİRİNİZ", "position": (300, 380, 600, 40)},
            {"bilgi": "label_ekleme_resim", "text": "", "position": (550, 300, 100, 100)},
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
