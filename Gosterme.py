import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
from Ana_menu import *

class Goster_Modul(QWidget):
    def hepsini_goster(self):
        self.button.show()

    def buton1_goster(self):
        print("1 göster")

    def buton2_goster(self):
        print("2 göster")

    def buton3_goster(self):
        print("3 göster")