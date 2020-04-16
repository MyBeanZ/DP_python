
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Preferences_win(object):
    def setupUi(self, OtherWindow, tab_len,  d_len, s_time, disp_set, port_name):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.setGeometry(1300, 400, 360, 185)
        OtherWindow.setWindowTitle("Preferences")
        """ PROMENNE"""
        """ Limits """
        self.max_tab_len = 5000  # delka tabulky
        self.min_tab_len = 1
        self.max_time = 10000    #update delay
        self.min_time = 3
        self.max_d_len = 10000   #casova osa
        self.min_d_len = 5
        """ Actual values"""
        self.p_d_len = d_len
        self.p_s_time = s_time
        self.p_port_name = port_name
        self.p_disp_set = disp_set
        self.p_tab_len = tab_len


        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        OtherWindow.setCentralWidget(self.centralwidget)
        """labels Actual val."""
        self.label_val = QtWidgets.QLabel(self.centralwidget)
        self.label_val.setGeometry(QtCore.QRect(309, 5, 50, 20))
        self.label_val.setText("Values:")

        """---------------- DELKA vzorku TIME d_len--------------"""
        coor_len = [20, 30]
        self.label_len = QtWidgets.QLabel(self.centralwidget)
        self.label_len.setGeometry(QtCore.QRect(coor_len[0], coor_len[1], 100, 20))
        self.label_len.setText("Time samples:")

        self.text_len = QLineEdit(self.centralwidget)
        self.text_len.setPlaceholderText("Max: " + str(self.max_d_len) + ", Min: " + str(self.min_d_len))
        self.text_len.setGeometry(QtCore.QRect(coor_len[0] + 100, coor_len[1], 130, 20))

        self.butt_len = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_len.setGeometry(260, coor_len[1], 40, 20)
        self.butt_len.clicked.connect(self.Set_d_len)

        self.label_val_d_len = QtWidgets.QLabel(self.centralwidget)
        self.label_val_d_len.setGeometry(QtCore.QRect(309, coor_len[1], 50, 20))
        self.label_val_d_len.setText(str(self.p_d_len))

        """---------------- DELKA Tabulky tab_len--------------"""

        coor_tab = [coor_len[0], coor_len[1] + 24]
        self.label_tab_len = QtWidgets.QLabel(self.centralwidget)
        self.label_tab_len.setGeometry(QtCore.QRect(coor_tab[0], coor_tab[1], 100, 20))
        self.label_tab_len.setText("Table length:")

        self.text_tab_len = QLineEdit(self.centralwidget)
        self.text_tab_len.setPlaceholderText("Max: " + str( self.max_tab_len) + ", Min:" + str(self.min_tab_len))
        self.text_tab_len.setGeometry(QtCore.QRect(coor_tab[0] + 100, coor_tab[1], 130, 20))

        self.butt_tab_len = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_tab_len.setGeometry(QtCore.QRect(260, coor_tab[1], 40, 20))
        self.butt_tab_len.clicked.connect(self.Set_tab_len)

        self.label_val_tab_len = QtWidgets.QLabel(self.centralwidget)
        self.label_val_tab_len.setGeometry(QtCore.QRect(309, coor_tab[1], 50, 20))
        self.label_val_tab_len.setText(str(self.p_tab_len))

        """--------------cas aktualizace time ------------------"""
        coor_time = [coor_tab[0], coor_tab[1] + 24]
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(coor_time[0], coor_time[1], 110, 20))
        self.label_time.setText("Update delay (ms):")

        self.text_time = QLineEdit(self.centralwidget)
        self.text_time.setPlaceholderText("Max:" + str(self.max_time) + ", Min: " + str(self.min_time))
        self.text_time.setGeometry(QtCore.QRect(coor_time[0] + 100, coor_time[1], 130, 20))

        self.butt_time = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_time.setGeometry(QtCore.QRect(260, coor_time[1], 40, 20))
        self.butt_time.clicked.connect(self.Set_time)

        self.label_val_time = QtWidgets.QLabel(self.centralwidget)
        self.label_val_time.setGeometry(QtCore.QRect(309, coor_time[1], 50, 20))
        self.label_val_time.setText(str(self.p_s_time))

        """ -------------- jmeno portu -----------------"""
        coor_port = [coor_time[0], coor_time[1] + 24]
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(coor_port[0], coor_port[1], 100, 20))
        self.label_port.setText('Port name:')

        self.text_port = QLineEdit(self.centralwidget)
        self.text_port.setPlaceholderText("example: COM5")
        self.text_port.setGeometry(QtCore.QRect(coor_port[0] + 100, coor_port[1], 130, 20))

        self.butt_port = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_port.setGeometry(QtCore.QRect(260, coor_port[1], 40, 20))
        self.butt_port.clicked.connect(self.Set_port)

        self.label_val_port = QtWidgets.QLabel(self.centralwidget)
        self.label_val_port.setGeometry(QtCore.QRect(309, coor_port[1], 50, 20))
        self.label_val_port.setText(self.p_port_name)

        """ ------------Zobrazeni v REL nabo ABS"""
        coor_disp = [coor_port[0], coor_port[1] + 24]
        self.label_disp = QtWidgets.QLabel(self.centralwidget)
        self.label_disp.setGeometry(QtCore.QRect(coor_disp[0], coor_disp[1], 200, 20))
        self.label_disp.setText("Relative val.:")

        self.disp_box = QCheckBox(self.centralwidget)
        self.disp_box.setText("Absolute/Relative display")
        self.disp_box.setChecked(False)
        self.disp_box.setGeometry(QtCore.QRect(coor_disp[0] + 100, coor_disp[1], 200, 20))
        #self.disp_box.move(coor_disp[0] + 60, coor_disp[1])
        self.disp_box.toggled.connect(self.disp_clik)

        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(OtherWindow)
    def Set_d_len(self):
        name = self.text_len.text()
        self.text_len.clear()
        if name == "":
            self.label_val_d_len.setText(str(self.p_d_len))
            self.label_val_d_len.setStyleSheet('color: black')
        else:
            try:
                if int(name) > self.max_d_len:
                    self.p_d_len = self.max_d_len
                elif int(name) < self.min_time:
                    self.p_d_len = self.min_d_len
                else:
                    self.p_d_len = int(name)

                print(self.p_d_len)
                self.label_val_d_len.setText(str(self.p_d_len))
                self.label_val_d_len.setStyleSheet('color: black')
            except:
                self.label_val_d_len.setStyleSheet('color: red')
                self.label_val_d_len.setText("NaN")

    def Set_tab_len(self):
        name = self.text_tab_len.text()
        self.text_tab_len.clear()
        if name == "":
            self.label_val_tab_len.setText(str(self.p_tab_len))
            self.label_val_tab_len.setStyleSheet('color: black')
        else:
            try:
                if int(name) > self.max_tab_len:
                    self.p_tab_len = self.max_tab_len
                elif int(name) < self.min_tab_len:
                    self.p_tab_len = self.min_tab_len
                else:
                    self.p_tab_len = int(name)

                self.label_val_tab_len.setText(str(self.p_tab_len))
                self.label_val_tab_len.setStyleSheet('color: black')
                print(self.p_tab_len)
            except:
                self.label_val_tab_len.setStyleSheet('color: red')
                self.label_val_tab_len.setText("NaN")

    def Set_time(self):
        name = self.text_time.text()
        self.text_time.clear()
        if name == "":
            self.label_val_time.setText(str(self.p_s_time))
            self.label_val_time.setStyleSheet('color: black')
        else:
            try:
                if int(name) > self.max_time:
                    self.p_s_time = self.max_time
                elif int(name) < self.min_time:
                    self.p_s_time = self.min_time
                else:
                    self.p_s_time = int(name)

                self.label_val_time.setText(str(self.p_s_time))
                self.label_val_time.setStyleSheet('color: black')
                print(self.p_s_time)
            except:
                self.label_val_time.setStyleSheet('color: red')
                self.label_val_time.setText("NaN")

    def Set_port(self):
        name = self.text_port.text()
        if name == "":
            self.label_val_time.setText(self.p_port_name)
            self.label_val_time.setStyleSheet('color: black')
        else:
            self.text_port.clear()
            self.label_val_port.setText(name)
            self.label_val_port.setStyleSheet('color: black')
            print(str(name))
            self.p_port_name = name



    def disp_clik(self):
        if self.disp_box.checkState():
            self.p_disp_set = 'abs'
            self.label_disp.setText('Absolute val.')
        else:
            self.p_disp_set = 'rel'
            self.label_disp.setText('Relative val.')




    # def retranslateUi(self, OtherWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow"))
    #     self.label.setText(_translate("OtherWindow", "Welcome To This Window"))


if __name__ == "__main__":  # pro testovani
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Preferences_win()
    ui.setupUi(OtherWindow,10,100,1000,'rel','COM5')
    OtherWindow.show()
    sys.exit(app.exec_())