import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPalette, QColor


class MetinselAraclar(QWidget):
    def GirisSayfasiMetinGirisleri(self):
        self.line_edits = []
        line_edit_info = [
            {"bilgi": "GirisKismiKullaniciAdi", "placeholder": "KULLANICI ADI", "position": (450, 180, 200, 40)},
            {"bilgi": "GirisKismiSifre", "placeholder": "ŞİFRE", "position": (450, 240, 200, 40)},

            {"bilgi": "KayitKismiIsim", "placeholder": "İSİM", "position": (450, 120, 200, 40)},
            {"bilgi": "KayitKismiSoyisim", "placeholder": "SOYİSİM", "position": (450, 180, 200, 40)},
            {"bilgi": "KayitKismiKullaniciAdi", "placeholder": "KULLANICI ADI", "position": (450, 240, 200, 40)},
            {"bilgi": "KayitKismiSifre", "placeholder": "ŞİFRE", "position": (450, 300, 200, 40)},

            {"bilgi": "SifremiUnuttumKismiKullaniciAdi", "placeholder": "KULLANICI ADI", "position": (450, 240, 200, 40)},
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

            if bilgi == "GirisKismiSifre":
                line_edit.setEchoMode(QLineEdit.Password)

    def KelimeEklemeSayfasiMetinGirisleri(self):
        self.line_edits = []
        line_edit_info = [
            {"bilgi": "SoruEklemeIngilizce", "placeholder": "KELİMENİN İNGİLİZCESİ", "position": (450, 60, 200, 40)},
            {"bilgi": "SoruEklemeTurkce", "placeholder": "KELİMENİN TÜRKÇESİ", "position": (450, 120, 200, 40)},
            {"bilgi": "SoruEklemeIngilizceCumle", "placeholder": "İNGİLİZCE CÜMLE", "position": (290, 180, 200, 40)},
            {"bilgi": "SoruEklemeTurkceCumle", "placeholder": "TÜRKÇE CÜMLE", "position": (610, 180, 200, 40)},
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

    def UyariMetinGirisleri(self):
        self.labels = []
        labels_info = [
            {"bilgi": "GirisKismiUyariMesaji", "text": "", "position": (200, 400, 800, 40)},
            {"bilgi": "KelimeEklemeUyariMesaji", "text": "", "position": (200, 460, 800, 40)},
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

            if bilgi == 'SoruCümleKismi':
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

    def BilgilendirmeMetinGirisleri(self):
        self.labels = []
        labels_info = [
            {"bilgi": "AyarlarDilKismi", "text": "DİLİ DEĞİŞTİRİNİZ", "position": (300, 130, 600, 40)},
            {"bilgi": "AyarlarSoruSayisiKismi", "text": "SORU SAYISINI DEĞİŞTİRİNİZ", "position": (300, 380, 600, 40)},
            {"bilgi": "KelimeEklemeResimKismi", "text": "", "position": (550, 300, 100, 100)},

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

            self.labels.append(label)
            setattr(self, bilgi, label)

    def SoruMetinGirisleri(self):
        self.labels = []
        labels_info = [
            {"bilgi": "SoruCümleKismi", "text": "CÜMLE SORU", "position": (250, 100, 700, 40)},
            {"bilgi": "SoruResimKismi", "text": "", "position": (550, 160, 100, 100)},
            {"bilgi": "SinavSayaci", "text": "", "position": (350, 540, 500, 40)},
            {"bilgi": "SoruAciklamasi", "text": "", "position": (200, 270, 800, 40)},

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

            if bilgi == 'SoruCümleKismi':
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