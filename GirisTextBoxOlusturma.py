import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPalette, QColor


class Giris_Text_box_Olustur(QWidget):
    def createTextBox(self):
        self.line_edits = []
        line_edit_info = [
            {"bilgi": "line_edit_kullanici_adi", "placeholder": "KULLANICI ADI", "position": (450, 180, 200, 40)},
            {"bilgi": "line_edit_sifre", "placeholder": "ŞİFRE", "position": (450, 240, 200, 40)},

            {"bilgi": "line_edit_isim", "placeholder": "İSİM", "position": (450, 60, 200, 40)},
            {"bilgi": "line_edit_soyisim", "placeholder": "SOYİSİM", "position": (450, 120, 200, 40)},
            {"bilgi": "line_edit_mail", "placeholder": "MAİL", "position": (450, 180, 200, 40)},
            {"bilgi": "line_edit_kaydol_kullanici_adi", "placeholder": "KULLANICI ADI", "position": (450, 300, 200, 40)},

            {"bilgi": "line_edit_sifre_kullanici_adi", "placeholder": "KULLANICI ADI", "position": (450, 180, 200, 40)},
            {"bilgi": "line_edit_sifre_mail", "placeholder": "MAİL", "position": (450, 240, 200, 40)},
        ]

        for edit_info in line_edit_info:
            bilgi = edit_info["bilgi"]
            line_edit = QLineEdit(self)
            line_edit.setPlaceholderText(edit_info["placeholder"])
            line_edit.setGeometry(*edit_info["position"])

            # Set placeholder text color to white
            palette = line_edit.palette()
            palette.setColor(QPalette.PlaceholderText, QColor("#FFFFFF"))
            line_edit.setPalette(palette)

            line_edit.setStyleSheet("""
            QLineEdit {
                color: white; /* Metin rengi */
                border-radius: 20px;
                padding: 0 15px;
                background-color: #FFA500; /* Saydam beyaz */
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
