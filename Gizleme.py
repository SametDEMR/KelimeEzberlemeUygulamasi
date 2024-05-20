import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
from Buton_oluşturma import *
from Ana_menu import *

class Gizle_Modul(QWidget):
    def buton1_gizle(self):
        self.button.hide()

    def buton2_gizle(self):
        print("2 hariç gizle")

    def buton3_gizle(self):
        print("3 hariç gizle")