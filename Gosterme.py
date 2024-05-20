import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
from Ana_menu import *

class Goster_Modul(QWidget):
    def hepsini_goster(self):
        self.text1_label.show()
        self.text2_label.show()
        self.text3_label.show()
        self.text4_label.show()

    def buton1_goster(self):
        self.text1_label.show()

    def buton2_goster(self):
        self.text2_label.show()

    def buton3_goster(self):
        self.text3_label.show()

    def buton4_goster(self):
        self.text4_label.show()
