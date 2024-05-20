import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont


class Text_box_olustur_Modul(QWidget):
    def createTextBox(self):
        self.line_edits = []
        line_edit_info = [
            {"bilgi": "line_edit_kullanici_adi", "placeholder": "Kullanıcı Adı", "position": (450, 180, 200, 40)},
            {"bilgi": "line_edit_sifre", "placeholder": "Şifre", "position": (450, 240, 200, 40)},

            {"bilgi": "line_edit_isim", "placeholder": "İsim", "position": (450, 60, 200, 40)},
            {"bilgi": "line_edit_soyisim", "placeholder": "Soyisim", "position": (450, 120, 200, 40)},
            {"bilgi": "line_edit_mail", "placeholder": "Mail", "position": (450, 180, 200, 40)},
            {"bilgi": "line_edit_kaydol_kullanici_adi", "placeholder": "Kullanıcı Adı", "position": (450, 300, 200, 40)},

            {"bilgi": "line_edit_sifre_kullanici_adi", "placeholder": "Kullanıcı Adı", "position": (450, 160, 200, 40)},
            {"bilgi": "line_edit_sifre_mail", "placeholder": "Mail", "position": (450, 220, 200, 40)},
        ]

        for edit_info in line_edit_info:
            bilgi = edit_info["bilgi"]
            line_edit = QLineEdit(self)
            line_edit.setPlaceholderText(edit_info["placeholder"])
            line_edit.setGeometry(*edit_info["position"])
            line_edit.setStyleSheet("""
            QLineEdit {
            border: 2px solid black;
            border-radius: 20px;
            padding: 0 8px;
            background-color: rgba(246, 246, 246, 100); /* Saydam beyaz */
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