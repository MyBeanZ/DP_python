
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Txt_win(object):
    def setupUi(self, OtherWindow, data_x, data_y):
        x_y_coor = [1300, 720]
        x_y_geo = [320, 150]
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.setGeometry(x_y_coor[0], x_y_coor[1], x_y_geo[0], x_y_geo[1])
        OtherWindow.setWindowTitle("Create txt file")

        """ PROMENNE"""
        self.data_test_x = data_x
        self.data_test_y = data_y
        self.columns = 0
        self.separator = " "
        self.name = "default_name"
        self.decimal = 4

        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        OtherWindow.setCentralWidget(self.centralwidget)

        """ Widgety pro nastaveni cesty"""
        inside_coor = [20, 5]
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(inside_coor[0], inside_coor[1], 100, 20)
        self.label_path.setText("Enter file name:")

        self.text_path = QLineEdit(self.centralwidget)
        self.text_path.setGeometry(inside_coor[0], inside_coor[1] + 25, 150, 20)
        self.text_path.setPlaceholderText("default_name")

        self.label_dot = QtWidgets.QLabel(self.centralwidget)
        self.label_dot.setGeometry(inside_coor[0] + 155, inside_coor[1]+25, 100, 20)
        self.label_dot.setText(".txt")

        self.butt_len = QtWidgets.QPushButton("Create", self.centralwidget)
        self.butt_len.setGeometry(inside_coor[0] + 210, inside_coor[1]+ 25, 70, 20)
        self.butt_len.clicked.connect(self.create_txt)

        """ Widgety separator"""
        self.label_separator = QtWidgets.QLabel(self.centralwidget)
        self.label_separator.setGeometry(inside_coor[0], inside_coor[1] + 35+25, 60, 20)
        self.label_separator.setText("Separator:")

        self.text_sep = QLineEdit(self.centralwidget)
        self.text_sep.setGeometry(inside_coor[0] + 65, inside_coor[1] + 35+25, 60, 20)
        self.text_sep.setPlaceholderText('"space"')

        self.butt_sep = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_sep.setGeometry(inside_coor[0] + 140, inside_coor[1]+ 35+25, 35, 20)
        self.butt_sep.clicked.connect(self.create_sep)

        self.label_val_sepp = QtWidgets.QLabel(self.centralwidget)
        self.label_val_sepp.setGeometry(QtCore.QRect(inside_coor[0] + 140 + 50, inside_coor[1]+ 35+25, 50, 20))
        self.label_val_sepp.setText('"' + self.separator + '"')

        """ Widgety Pocet column """
        self.label_column = QtWidgets.QLabel(self.centralwidget)
        self.label_column.setGeometry(inside_coor[0], inside_coor[1] + 35 + 25 + 23, 90, 20)
        self.label_column.setText("No. of columns:")

        self.text_column = QLineEdit(self.centralwidget)
        self.text_column.setGeometry(inside_coor[0] + 100, inside_coor[1] + 35 + 25 + 23, 30, 20)
        self.text_column.setPlaceholderText('0')

        self.butt_column = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_column.setGeometry(inside_coor[0] + 140, inside_coor[1]+ 35+25+23, 35, 20)
        self.butt_column.clicked.connect(self.create_col)

        self.label_val_column = QtWidgets.QLabel(self.centralwidget)
        self.label_val_column.setGeometry(QtCore.QRect(inside_coor[0] + 140 + 50, inside_coor[1]+ 35+25+23, 50, 20))
        self.label_val_column.setText(str(self.columns))

        """ Widgety Pocet Decimals """
        self.label_dec = QtWidgets.QLabel(self.centralwidget)
        self.label_dec.setGeometry(inside_coor[0], inside_coor[1] + 35 + 25 + 23 +23, 90, 20)
        self.label_dec.setText("No. of decimals:")

        self.text_dec = QLineEdit(self.centralwidget)
        self.text_dec.setGeometry(inside_coor[0] + 100, inside_coor[1] + 35 + 25 + 23+23, 30, 20)
        self.text_dec.setPlaceholderText('4')

        self.butt_dec = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_dec.setGeometry(inside_coor[0] + 140, inside_coor[1]+ 35+25+23+23, 35, 20)
        self.butt_dec.clicked.connect(self.create_dec)

        self.label_val_dec = QtWidgets.QLabel(self.centralwidget)
        self.label_val_dec.setGeometry(QtCore.QRect(inside_coor[0] + 140 + 50, inside_coor[1]+ 35+25+23+23, 50, 20))
        self.label_val_dec.setText(str(self.decimal))


    def create_txt(self):
        if self.text_path.text():  # pokud vyplneny textbox
            self.name = self.text_path.text()  #nahradi default name
        file_name = self.name + ".txt"
        file_txt = open(file_name, "w")
        format_str = "." + str(self.decimal) + "f"

        file_txt.write("DATA X: \r\n")
        for i in range(len(self.data_test_x)):
            string = format(self.data_test_x[i], format_str) + self.separator
            if self.columns != 0:
                if ((i+1)%self.columns) == 0:  #podminka pro i + 1, protoze 0%cokoli == 0 -> vytvoru column
                    string = string + "\r\n"
            file_txt.write(string)

        file_txt.write("\r\nDATA Y: \r\n")
        for i in range(len(self.data_test_y)):
            string = format(self.data_test_y[i], format_str) + self.separator

            if self.columns != 0:
                if ((i + 1) % self.columns) == 0:  # podminka pro i + 1, protoze 0%cokoli == 0 -> vytvoru column
                    string = string + "\r\n"
            file_txt.write(string)
        file_txt.close()

    def create_sep(self):
        self.separator = self.text_sep.text()
        self.label_val_sepp.setText('"' + self.separator + '"')
        self.text_sep.clear()

    def create_col(self):
        if self.text_column.text() == "":
            self.label_val_column.setText(str(self.columns))
            self.label_val_column.setStyleSheet('color: black')
        else:
            try:
                self.columns = int(self.text_column.text())
            except:
                self.label_val_column.setText("NaN")
                self.label_val_column.setStyleSheet('color: red')
                #self.columns = 0
        self.text_column.clear()

    def create_dec(self):
        if self.text_dec.text() == "":
            self.label_val_dec.setText(str(self.decimal))
            self.label_val_dec.setStyleSheet('color: black')
        else:
            try:
                self.decimal = int(self.text_dec.text())
            except:
                self.label_val_dec.setText("NaN")
                self.label_val_dec.setStyleSheet('color: red')
                #self.decimal = 4
        self.text_dec.clear()


if __name__ == "__main__":  # pro testovani
    import sys
    test_data = [30, 80 , 89, 998.09890, 7]
    test_data_2 = [90, 0.0007454235, 40, 40, 4]
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Txt_win()
    ui.setupUi(OtherWindow, test_data, test_data_2)
    OtherWindow.show()
    sys.exit(app.exec_())