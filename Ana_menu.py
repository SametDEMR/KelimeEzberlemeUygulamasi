import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import locale

from Gizleme import *
from Gosterme import *
from Buton_oluşturma import *

locale.setlocale(locale.LC_ALL, 'turkish')

class Ana_Pencere1(QWidget):
    def __init__(self):
        super().__init__()
        self.pencereler = []
        self.text_inputs = []

        self.setWindowTitle("Depo Yönetim Sistemi")
        self.setFixedSize(1200, 600)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.paintEvent(self)

        self.createButtons()
        self.createTextInput()
        Gizle_Modul.hepsini_gizle(self)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        font = QFont("Script MT Bold", 20)
        painter.setFont(font)
        painter.setPen(QColor(0, 127, 255))
        painter.drawText(10, 30, "Kelime Ezberleme Modülü")

    def createButtons(self):
        Buton_Olustur_Modul.createButtons(self)

    def createTextInput(self):
        texts_info = [
            {"özellik": "1", "text": "<-- 1 -->", "position": (300, 300, 150, 30)},
            {"özellik": "2", "text": "<-- 2 -->", "position": (300, 350, 150, 30)},
            {"özellik": "3", "text": "<-- 3 -->", "position": (300, 400, 150, 30)},
            {"özellik": "4", "text": "<-- 4 -->", "position": (300, 450, 150, 30)},
        ]

        for text_info in texts_info:
            text_input = QLineEdit(self)
            text_input.setGeometry(*text_info["position"])
            sayi = text_info["özellik"]
            setattr(self, f"text{sayi}_label", text_input)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def exitFunction(self):
        sys.exit(app.exec_())

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def menu1Function(self):
        Gizle_Modul.buton1_gizle(self)
        Goster_Modul.buton1_goster(self)

    def menu2Function(self):
        Gizle_Modul.buton2_gizle(self)
        Goster_Modul.buton2_goster(self)

    def menu3Function(self):
        Gizle_Modul.buton3_gizle(self)
        Goster_Modul.buton3_goster(self)

    def menu4Function(self):
        Gizle_Modul.buton4_gizle(self)
        Goster_Modul.buton4_goster(self)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ana_pencere = Ana_Pencere1()
    ana_pencere.show()
    sys.exit(app.exec_())
