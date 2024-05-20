import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SinavLabelOlusturma(QWidget):
    def Olustur(self):
        self.labels = []
        labels_info = [
            {"bilgi": "label_soru", "text": "", "position": (350, 400, 500, 40)},
            {"bilgi": "label_sik", "text": "", "position": (600, 540, 500, 40)},
        ]

        for label_info in labels_info:
            bilgi = label_info["bilgi"]
            label = QLabel(label_info["text"], self)
            label.setGeometry(*label_info["position"])
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("""
                QLabel {
                    color: #FFFFFF;
                    font-family: "Arial", sans-serif; /* Yazı fontu */
                    font-size: 20px;
                }
            """)
            self.labels.append(label)
            setattr(self, bilgi, label)

