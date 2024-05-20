import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale
from Ana_menu import *

class Gizle_Modul(QWidget):
    def hepsini_gizle(self):
        self.text1_label.hide()
        self.text2_label.hide()
        self.text3_label.hide()
        self.text4_label.hide()

    def buton1_gizle(self):
        self.text2_label.hide()
        self.text3_label.hide()
        self.text4_label.hide()

    def buton2_gizle(self):
        self.text1_label.hide()
        self.text3_label.hide()
        self.text4_label.hide()

    def buton3_gizle(self):
        self.text1_label.hide()
        self.text2_label.hide()
        self.text4_label.hide()

    def buton4_gizle(self):
        self.text1_label.hide()
        self.text2_label.hide()
        self.text3_label.hide()

