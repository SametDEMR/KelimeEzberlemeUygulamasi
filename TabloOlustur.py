from PyQt5.QtWidgets import *

class TabloOlustur(QWidget):
    def Olustur(self):
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

        self.KelimelerTablosu.setStyleSheet("""
                QTableWidget {
                    background-color: #1E468F;
                    alternate-background-color: #1E468F;
                    color: #FFFFFF;
                    font-size: 20px;
                    border: 0px solid #FFFFFF;
                }

                QTableWidget::item {
                    padding: 5px;
                    font-size: 20px;
                }
            """)

        self.KelimelerTablosu.insertRow(self.KelimelerTablosu.rowCount())
        self.KelimelerTablosu.setRowHeight(self.KelimelerTablosu.rowCount() - 1, 120)