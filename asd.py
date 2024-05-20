import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import locale

from AAnaMenu import *

class asdasdasd(QWidget):
    def asd(self):
        self.scroll = QScrollArea()
        self.setCentralWidget(self.scroll)

        self.widget = QWidget()
        self.scroll.setWidget(self.widget)
        self.scroll.setWidgetResizable(True)

        layout = QVBoxLayout()
        for i in range(1, 10):
            label = QLabel(f"Label {i}")
            label.setObjectName(f"label{i}")
            layout.addWidget(label)

        self.widget.setLayout(layout)

        self.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    color: #333;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 15px;
                    background-color: #f9f9f9;
                }
                QLabel:hover {
                    background-color: #e0e0e0;
                }
                QScrollArea {
                    border: none;
                }
                """)
