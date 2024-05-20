import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Label_olusturma(QWidget):
    def createLabels(self):
        self.labels = []
        labels_info = [
            {"bilgi": "label_aciklama", "text": "", "position": (350, 290, 500, 40)},
        ]

        for label_info in labels_info:
            bilgi = label_info["bilgi"]
            label = QLabel(label_info["text"], self)
            label.setGeometry(*label_info["position"])
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("""
                QLabel {
                    color: #34495e;
                    font-family: "Times New Roman", sans-serif; /* Yazı fontu */
                    font-size: 16px;
                }
            """)
            self.labels.append(label)
            setattr(self, bilgi, label)

