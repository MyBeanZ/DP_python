
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Txt_win(object):
    def setupUi(self, OtherWindow, data):
        x_y_coor = [1300, 670]
        x_y_geo = [360, 170]
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.setGeometry(x_y_coor[0], x_y_coor[1], x_y_geo[0], x_y_geo[1])
        OtherWindow.setWindowTitle("Create txt file")
        """ PROMENNE"""

        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        OtherWindow.setCentralWidget(self.centralwidget)

        """ Widgety pro nastaveni cesty"""
        inside_coor = [20, 5]
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(inside_coor[0], inside_coor[1], 100, 20)
        self.label_path.setText("Path:")

        self.text_path = QLineEdit(self.centralwidget)
        self.text_path.setGeometry(inside_coor[0], inside_coor[1] + 25, 260, 20)

        self.butt_len = QtWidgets.QPushButton("Create", self.centralwidget)
        self.butt_len.setGeometry(inside_coor[0] + 260, inside_coor[1]+ 25, 70, 20)
        # self.butt_len.clicked.connect(self.)


        def





if __name__ == "__main__":  # pro testovani
    import sys
    test_data = [30, 80 , 89, 90, 7]
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Txt_win()
    ui.setupUi(OtherWindow, test_data)
    OtherWindow.show()
    sys.exit(app.exec_())