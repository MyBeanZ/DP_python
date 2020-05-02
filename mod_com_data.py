
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Data_win(object):
    def setupUi(self, OtherWindow, tab_len):
        x_y_coor = [100, 300]
        x_y_geo = [370, 600]
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.setGeometry(x_y_coor[0], x_y_coor[1], x_y_geo[0], x_y_geo[1])
        OtherWindow.setWindowTitle("COM data")

        self.tab_len = tab_len

        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        OtherWindow.setCentralWidget(self.centralwidget)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(self.tab_len)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setGeometry(0, 0, 350, 600)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("data SUM"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("data X"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("data Y"))


if __name__ == "__main__":  # pro testovani
    import sys
    test_data = [30, 80 , 89, 998.09890, 7]
    test_data_2 = [90, 0.0007454235, 40, 40, 4]
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Data_win()
    ui.setupUi(OtherWindow, 30)
    OtherWindow.show()
    sys.exit(app.exec_())