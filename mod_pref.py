
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Preferences_win(object):
    def setupUi(self, OtherWindow,tab_len ,d_len, s_time, disp_set, port_name):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.setGeometry(500, 300, 300, 200)
        OtherWindow.setWindowTitle("Preferences")
        """ PROMENNE"""
        max_tab_len = 300
        min_tab_len = 10
        max_time = 3000
        min_time = 50
        self.p_d_len = d_len
        self.p_s_time = s_time
        self.p_port_name = port_name
        self.p_disp_set = disp_set
        self.p_tab_len = tab_len


        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        OtherWindow.setCentralWidget(self.centralwidget)
        """---------------- DELKA vzorku TIME--------------"""
        coor_len = [20, 30]
        self.label_len = QtWidgets.QLabel(self.centralwidget)
        self.label_len.setGeometry(QtCore.QRect(coor_len[0], coor_len[1], 40, 20))
        self.label_len.setText(str(self.p_d_len))

        self.text_len = QLineEdit(self.centralwidget)
        self.text_len.setPlaceholderText("Table length")
        self.text_len.setGeometry(QtCore.QRect(coor_len[0] + 60, coor_len[1], 130, 20))

        self.butt_len = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_len.setGeometry(220, coor_len[1], 40, 20)
        self.butt_len.clicked.connect(self.Set_len)

        """---------------- DELKA Tabulky--------------"""

        coor_tab = [coor_len[0], coor_len[1] + 24]
        self.label_tab_len = QtWidgets.QLabel(self.centralwidget)
        self.label_tab_len.setGeometry(QtCore.QRect(coor_tab[0], coor_tab[1], 40, 20))
        self.label_tab_len.setText(str(self.p_tab_len))

        self.text_tab_len = QLineEdit(self.centralwidget)
        self.text_tab_len.setPlaceholderText("Time length")
        self.text_tab_len.setGeometry(QtCore.QRect(coor_tab[0] + 60, coor_tab[1], 130, 20))

        self.butt_tab_len = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_tab_len.setGeometry(QtCore.QRect(220, coor_tab[1], 40, 20))
        self.butt_tab_len.clicked.connect(self.Set_len)
        """--------------cas aktualizace ------------------"""
        coor_time = [coor_tab[0], coor_tab[1] + 24]
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(coor_time[0], coor_time[1], 40, 20))
        self.label_time.setText(str(s_time))

        self.text_time = QLineEdit(self.centralwidget)
        self.text_time.setPlaceholderText("Update delay (ms)")
        self.text_time.setGeometry(QtCore.QRect(coor_time[0] + 60, coor_time[1], 130, 20))

        self.butt_time = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_time.setGeometry(QtCore.QRect(220, coor_time[1], 40, 20))
        self.butt_time.clicked.connect(self.Set_len)
        """ -------------- jmeno portu -----------------"""
        coor_port = [coor_time[0], coor_time[1] + 24]
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(coor_port[0], coor_port[1], 40, 20))
        self.label_port.setText(port_name)

        self.text_port = QLineEdit(self.centralwidget)
        self.text_port.setPlaceholderText('Port name ("COM5")')
        self.text_port.setGeometry(QtCore.QRect(coor_port[0] + 60, coor_port[1], 130, 20))

        self.butt_port = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_port.setGeometry(QtCore.QRect(220, coor_port[1], 40, 20))
        self.butt_port.clicked.connect(self.Set_len)
        """ ------------Zobrazeni v REL nabo ABS"""
        coor_disp = [coor_port[0], coor_port[1] + 24]
        self.label_disp = QtWidgets.QLabel(self.centralwidget)
        self.label_disp.setGeometry(QtCore.QRect(coor_disp[0], coor_disp[1], 40, 20))
        self.label_disp.setText(disp_set)

        self.disp_box = QCheckBox(self.centralwidget)
        self.disp_box.setText("Absolute/Relative display")
        self.disp_box.setChecked(True)
        self.disp_box.setGeometry(QtCore.QRect(coor_disp[0] + 60, coor_disp[1], 200, 20))
        #self.disp_box.move(coor_disp[0] + 60, coor_disp[1])
        self.disp_box.toggled.connect(self.disp_clik)

        # font = QtGui.QFont()
        # font.setPointSize(22)
        #self.label.setFont(font)


        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        #self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)
    def Set_len(self):
        try:
            name = self.text_len.text()
            print(str(name))
            self.label_len.setText(str(name))
            self.p_d_len = int(name)

        except:
            self.label_len.setText(str(self.p_d_len))

    def disp_clik(self):
        if self.disp_box.isChecked():
            self.p_disp_set = 'abs'
        else:
            self.p_disp_set = 'rel'
        pass



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