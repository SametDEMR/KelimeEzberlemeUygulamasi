from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class TabloOlustur(QWidget):
    def KelimelerTablosu(self):
        self.KelimelerTablosu = QTableWidget(self)
        self.KelimelerTablosu.setGeometry(20, 60, 1180, 480)

        self.KelimelerTablosu.setColumnCount(5)
        self.KelimelerTablosu.setHorizontalHeaderLabels(
            ["İNGİLİZCE", "TÜRKÇE", "İNGİLİZCE CÜMLE", "TÜRKÇE CÜMLE", "RESİM"])

        self.KelimelerTablosu.setColumnWidth(0, 120)
        self.KelimelerTablosu.setColumnWidth(1, 120)
        self.KelimelerTablosu.setColumnWidth(2, 400)
        self.KelimelerTablosu.setColumnWidth(3, 400)
        self.KelimelerTablosu.setColumnWidth(4, 120)

        # Tabloya satır eklenmişse, her satırın yüksekliğini ayarla
        for row in range(self.KelimelerTablosu.rowCount()):
            self.KelimelerTablosu.setRowHeight(row, 120)

        self.KelimelerTablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.KelimelerTablosu.setSelectionMode(QAbstractItemView.NoSelection)
        self.KelimelerTablosu.verticalHeader().setVisible(False)

        # Çizgileri kaldır
        self.KelimelerTablosu.setShowGrid(False)
        self.KelimelerTablosu.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.KelimelerTablosu.setStyleSheet("""
                QTableWidget {
                    background-color: #1E468F;
                    alternate-background-color: #1E468F;
                    color: #FFFFFF;
                    font-size: 20px;
                    border: 0px solid #1E468F;
                }

                QTableWidget::item {
                    padding: 5px;
                    font-size: 20px;
                }
            """)

        header = self.KelimelerTablosu.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #FFB347;
                color: #333333;
                font-size: 20px;
                border: 0px solid #FFB347;
                border-radius: 20px;
                padding: 5px;
                font-family: Arial; /* veya istediğiniz bir yazı tipi */
            }
        """)

        self.KelimelerTablosu.insertRow(self.KelimelerTablosu.rowCount())
        self.KelimelerTablosu.setRowHeight(self.KelimelerTablosu.rowCount() - 1, 120)

    def Yildiz1TablosuOlustur(self):
        self.Yildiz1Tablosu = QTableWidget(self)
        self.Yildiz1Tablosu.setGeometry(10, 272, 228, 200)

        self.Yildiz1Tablosu.setColumnCount(1)
        self.Yildiz1Tablosu.setHorizontalHeaderLabels(
            ["★"])

        self.Yildiz1Tablosu.setColumnWidth(0, 160)

        self.Yildiz1Tablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Yildiz1Tablosu.setSelectionMode(QAbstractItemView.NoSelection)
        self.Yildiz1Tablosu.verticalHeader().setVisible(False)

        self.Yildiz1Tablosu.setStyleSheet("""
            QTableWidget {
                background-color: #1E468F;
                alternate-background-color: #1E468F;
                color: #FFFFFF;
                font-size: 24px;
                border: 0px solid #1E468F;
                text-align: center; /* Metni ortaladık */
            }

            QTableWidget::item {
                padding: 5px;
                font-size: 24px;
                text-align: center; /* Metni ortaladık */
            }
        """)

        header = self.Yildiz1Tablosu.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #FFB347;
                color: #333333;
                font-size: 20px;
                border: 0px solid #FFB347;
                border-radius: 20px;
                padding: 5px;
                font-family: Arial; /* veya istediğiniz bir yazı tipi */
            }
        """)


        self.Yildiz1Tablosu.insertRow(self.Yildiz1Tablosu.rowCount())

    def Yildiz2TablosuOlustur(self):
        self.Yildiz2Tablosu = QTableWidget(self)
        self.Yildiz2Tablosu.setGeometry(180, 272, 228, 200)

        self.Yildiz2Tablosu.setColumnCount(1)
        self.Yildiz2Tablosu.setHorizontalHeaderLabels(
            ["★★"])

        self.Yildiz2Tablosu.setColumnWidth(0, 160)

        self.Yildiz2Tablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Yildiz2Tablosu.setSelectionMode(QAbstractItemView.NoSelection)
        self.Yildiz2Tablosu.verticalHeader().setVisible(False)

        self.Yildiz2Tablosu.setStyleSheet("""
            QTableWidget {
                background-color: #1E468F;
                alternate-background-color: #1E468F;
                color: #FFFFFF;
                font-size: 24px;
                border: 0px solid #1E468F;
                text-align: center; /* Metni ortaladık */
            }

            QTableWidget::item {
                padding: 5px;
                font-size: 24px;
                text-align: center; /* Metni ortaladık */
            }
        """)

        header = self.Yildiz2Tablosu.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #FFB347;
                color: #333333;
                font-size: 20px;
                border: 0px solid #FFB347;
                border-radius: 20px;
                padding: 5px;
                font-family: Arial; /* veya istediğiniz bir yazı tipi */
            }
        """)


        self.Yildiz2Tablosu.insertRow(self.Yildiz2Tablosu.rowCount())

    def Yildiz3TablosuOlustur(self):
        self.Yildiz3Tablosu = QTableWidget(self)
        self.Yildiz3Tablosu.setGeometry(350, 272, 228, 200)

        self.Yildiz3Tablosu.setColumnCount(1)
        self.Yildiz3Tablosu.setHorizontalHeaderLabels(
            ["★★★"])

        self.Yildiz3Tablosu.setColumnWidth(0, 160)

        self.Yildiz3Tablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Yildiz3Tablosu.setSelectionMode(QAbstractItemView.NoSelection)
        self.Yildiz3Tablosu.verticalHeader().setVisible(False)

        self.Yildiz3Tablosu.setStyleSheet("""
            QTableWidget {
                background-color: #1E468F;
                alternate-background-color: #1E468F;
                color: #FFFFFF;
                font-size: 24px;
                border: 0px solid #1E468F;
                text-align: center; /* Metni ortaladık */
            }

            QTableWidget::item {
                padding: 5px;
                font-size: 24px;
                text-align: center; /* Metni ortaladık */
            }
        """)

        header = self.Yildiz3Tablosu.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #FFB347;
                color: #333333;
                font-size: 20px;
                border: 0px solid #FFB347;
                border-radius: 20px;
                padding: 5px;
                font-family: Arial; /* veya istediğiniz bir yazı tipi */
            }
        """)


        self.Yildiz3Tablosu.insertRow(self.Yildiz3Tablosu.rowCount())

    def Yildiz4TablosuOlustur(self):
        self.Yildiz4Tablosu = QTableWidget(self)
        self.Yildiz4Tablosu.setGeometry(520, 272, 228, 200)

        self.Yildiz4Tablosu.setColumnCount(1)
        self.Yildiz4Tablosu.setHorizontalHeaderLabels(
            ["★★★★"])

        self.Yildiz4Tablosu.setColumnWidth(0, 160)

        self.Yildiz4Tablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Yildiz4Tablosu.setSelectionMode(QAbstractItemView.NoSelection)
        self.Yildiz4Tablosu.verticalHeader().setVisible(False)

        self.Yildiz4Tablosu.setStyleSheet("""
            QTableWidget {
                background-color: #1E468F;
                alternate-background-color: #1E468F;
                color: #FFFFFF;
                font-size: 24px;
                border: 0px solid #1E468F;
                text-align: center; /* Metni ortaladık */
            }

            QTableWidget::item {
                padding: 5px;
                font-size: 24px;
                text-align: center; /* Metni ortaladık */
            }
        """)

        header = self.Yildiz4Tablosu.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #FFB347;
                color: #333333;
                font-size: 20px;
                border: 0px solid #FFB347;
                border-radius: 20px;
                padding: 5px;
                font-family: Arial; /* veya istediğiniz bir yazı tipi */
            }
        """)


        self.Yildiz4Tablosu.insertRow(self.Yildiz4Tablosu.rowCount())

    def Yildiz5TablosuOlustur(self):
        self.Yildiz5Tablosu = QTableWidget(self)
        self.Yildiz5Tablosu.setGeometry(690, 272, 228, 200)

        self.Yildiz5Tablosu.setColumnCount(1)
        self.Yildiz5Tablosu.setHorizontalHeaderLabels(
            ["★★★★★"])

        self.Yildiz5Tablosu.setColumnWidth(0, 160)

        self.Yildiz5Tablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Yildiz5Tablosu.setSelectionMode(QAbstractItemView.NoSelection)
        self.Yildiz5Tablosu.verticalHeader().setVisible(False)

        self.Yildiz5Tablosu.setStyleSheet("""
            QTableWidget {
                background-color: #1E468F;
                alternate-background-color: #1E468F;
                color: #FFFFFF;
                font-size: 24px;
                border: 0px solid #1E468F;
                text-align: center; /* Metni ortaladık */
            }

            QTableWidget::item {
                padding: 5px;
                font-size: 24px;
                text-align: center; /* Metni ortaladık */
            }
        """)

        header = self.Yildiz5Tablosu.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #FFB347;
                color: #333333;
                font-size: 20px;
                border: 0px solid #FFB347;
                border-radius: 20px;
                padding: 5px;
                font-family: Arial; /* veya istediğiniz bir yazı tipi */
            }
        """)


        self.Yildiz5Tablosu.insertRow(self.Yildiz5Tablosu.rowCount())

    def Yildiz6TablosuOlustur(self):
        self.Yildiz6Tablosu = QTableWidget(self)
        self.Yildiz6Tablosu.setGeometry(860, 272, 228, 200)

        self.Yildiz6Tablosu.setColumnCount(1)
        self.Yildiz6Tablosu.setHorizontalHeaderLabels(
            ["★★★★★★"])

        self.Yildiz6Tablosu.setColumnWidth(0, 160)

        self.Yildiz6Tablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Yildiz6Tablosu.setSelectionMode(QAbstractItemView.NoSelection)
        self.Yildiz6Tablosu.verticalHeader().setVisible(False)

        self.Yildiz6Tablosu.setStyleSheet("""
            QTableWidget {
                background-color: #1E468F;
                alternate-background-color: #1E468F;
                color: #FFFFFF;
                font-size: 24px;
                border: 0px solid #1E468F;
                text-align: center; /* Metni ortaladık */
            }

            QTableWidget::item {
                padding: 5px;
                font-size: 24px;
                text-align: center; /* Metni ortaladık */
            }
        """)

        header = self.Yildiz6Tablosu.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #FFB347;
                color: #333333;
                font-size: 20px;
                border: 0px solid #FFB347;
                border-radius: 20px;
                padding: 5px;
                font-family: Arial; /* veya istediğiniz bir yazı tipi */
            }
        """)


        self.Yildiz6Tablosu.insertRow(self.Yildiz6Tablosu.rowCount())

    def EzberlenmisTablosuOlustur(self):
        self.EzberlenmisTablosu = QTableWidget(self)
        self.EzberlenmisTablosu.setGeometry(1030, 272, 228, 200)

        self.EzberlenmisTablosu.setColumnCount(1)
        self.EzberlenmisTablosu.setHorizontalHeaderLabels(
            ["Ezberlenmiş"])

        self.EzberlenmisTablosu.setColumnWidth(0, 160)

        self.EzberlenmisTablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.EzberlenmisTablosu.setSelectionMode(QAbstractItemView.NoSelection)
        self.EzberlenmisTablosu.verticalHeader().setVisible(False)

        self.EzberlenmisTablosu.setStyleSheet("""
            QTableWidget {
                background-color: #1E468F;
                alternate-background-color: #1E468F;
                color: #FFFFFF;
                font-size: 24px;
                border: 0px solid #1E468F;
            }
            QTableWidget::item {
                padding: 5px;
                font-size: 24px;
            }
        """)

        header = self.EzberlenmisTablosu.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #FFB347;
                color: #333333;
                font-size: 20px;
                border: 0px solid #FFB347;
                border-radius: 20px;
                padding: 5px;
                font-family: Arial; /* veya istediğiniz bir yazı tipi */
                font-weight: bold;
            }
        """)


        self.EzberlenmisTablosu.insertRow(self.EzberlenmisTablosu.rowCount())