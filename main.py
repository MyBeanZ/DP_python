
from __future__ import unicode_literals
import sys
import os
import matplotlib

matplotlib.use('Qt5Agg')  #Agg je renderer - vykreslujici process - moznosti WXAgg, GTKAgg, QT4Agg
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
import serial
from mod_mplt import MplQuad, MplTwo
from mod_pref import Preferences_win
from mod_txt import Txt_win
import numpy as np

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

"""--------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------------------------"""

class ApplicationWindow(QtWidgets.QMainWindow):
    """--------------------------------------GUI ----------------------------------------------------------------------------"""
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setGeometry(300, 130, 900, 880)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("PSD - test")

        """ --------------------- PROMENNE ------------------------"""
        self.s_time = 100  #perioda vzorkovani
        self.port_name = 'COM5'
        self.disp_set = 'rel' # / 'abs'
        self.d_len = 100
        self.tab_len = 30
        self.val_343 = 1
        self.draw_enable = 0
        self.con_enable = True

        """----lista menu ------"""
        self.file_menu = QtWidgets.QMenu('&File', self)

        self.file_menu.addAction('&Preferences', self.prefClick,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_R)
        self.file_menu.addAction('&Save data', self.prefTxt,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_T)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)

        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        """----------------------Central Widget - Base ----------------------------"""
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFocus()  # pohled na central widget - Qapp velka plocha
        self.setCentralWidget(self.centralwidget)
        self.statusBar().showMessage("Welcome", 3000)

        """   -----------------  graf QUAD  layout-------------"""
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 510, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.quad = MplQuad(self.verticalLayoutWidget, width=5, height=4, dpi=90) # dc - graf XY

        self.layout_plot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_plot.setContentsMargins(0, 0, 0, 0)
        self.layout_plot.setObjectName("layout_plot")
        self.layout_plot.addWidget(self.quad)

        font_lab = QtGui.QFont()
        font_lab.setPointSize(9)
        self.Y_label = QtWidgets.QLabel(self.centralwidget)
        self.Y_label.setGeometry(48, 40, 70, 20)
        self.Y_label.setText("coord. Y")
        self.Y_label.setFont(font_lab)

        self.Y_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Y_label_2.setGeometry(60, 58, 50, 20)
        self.Y_label_2.setText("[-]")
        self.Y_label_2.setFont(font_lab)

        self.X_label = QtWidgets.QLabel(self.centralwidget)
        self.X_label.setGeometry(255, 418, 90, 20)
        self.X_label.setText("coord. X [-]")
        self.X_label.setFont(font_lab)

        """   -----------------  graf X v case - LAYOUT -----------------"""

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 510, 400, 300))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.x_time = MplTwo(self.verticalLayoutWidget_2, width=3, height=2, dpi=90)  # dc - graf XY

        font_time = QtGui.QFont()
        font_time.setPointSize(9)
        self.label_X = QtWidgets.QLabel(self.verticalLayoutWidget_2)  # self pred label kvuli pristupu z cele tridy
        self.label_X.setText("X samples in time")
        self.label_X.setFont(font_time)
        self.label_X.setGeometry(0, 15, 130, 18)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 50, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addWidget(self.x_time)

        self.X_label_time = QtWidgets.QLabel(self.centralwidget)
        self.X_label_time.setGeometry(43, 560, 110, 20)
        self.X_label_time.setText("coord. X [-]")
        self.X_label_time.setFont(font_lab)

        self.time_label_x = QtWidgets.QLabel(self.centralwidget)
        self.time_label_x.setGeometry(200, 810, 90, 20)
        self.time_label_x.setText("Time [ms]")
        self.time_label_x.setFont(font_lab)
        """   -----------------   graf Y v case - LAYOUT --------------------"""
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(460, 510, 400, 300))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.y_time = MplTwo(self.verticalLayoutWidget_3, width=6, height=2, dpi=90)  # dc - graf XY

        self.label_Y = QtWidgets.QLabel(self.verticalLayoutWidget_3)  # self pred label kvuli pristupu z cele tridy
        self.label_Y.setText("Y samples in time")
        self.label_Y.setFont(font_time)
        self.label_Y.setGeometry(0, 15, 130, 20)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 50, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.addWidget(self.y_time)

        self.Y_label_time = QtWidgets.QLabel(self.centralwidget)
        self.Y_label_time.setGeometry(43+420, 560, 110, 20)
        self.Y_label_time.setText("coord. Y [-]")
        self.Y_label_time.setFont(font_lab)

        self.time_label_Y = QtWidgets.QLabel(self.centralwidget)
        self.time_label_Y.setGeometry(200+420, 810, 90, 20)
        self.time_label_Y.setText("Time [ms]")
        self.time_label_Y.setFont(font_lab)

        """ ----------------------------preferences window---------------------------"""
        self.window = QtWidgets.QMainWindow()
        self.prefWin = Preferences_win()
        self.prefWin.setupUi(self.window, self.tab_len, self.d_len, self.s_time, self.disp_set, self.port_name)

        self.window_txt = QtWidgets.QMainWindow()
        self.txtWin = Txt_win()
        self.txtWin.setupUi(self.window_txt, self.quad.x_old, self.quad.y_old)

        """tlacitko STart/STOP --------- tlacitko CONNECT """
        self.butt_start = QtWidgets.QPushButton(self.centralwidget)
        self.butt_start.setGeometry(QtCore.QRect(585, 410, 93, 28))
        self.butt_start.setCheckable(True)
        self.butt_start.setChecked(False)  #pocatecni stav STOP => setChecked(False)
        self.butt_start.setEnabled(False)
        self.butt_start.setObjectName("pushButton")
        self.butt_start.clicked.connect(self.clicked_st)
        self.butt_start.setText("Start")

        self.butt_conn = QtWidgets.QPushButton(self.centralwidget)
        self.butt_conn.setGeometry(QtCore.QRect(685, 410, 93, 28))
        self.butt_conn.setEnabled(True)
        self.butt_conn.setCheckable(True)
        self.butt_conn.setChecked(False)
        self.butt_conn.setText("Connect")
        self.butt_conn.clicked.connect(self.connect)

        """ --------- connection labels ----------"""
        font_con = QtGui.QFont()
        font_con.setPointSize(9)

        self.label_con = QtWidgets.QLabel(self.centralwidget)  # self pred label kvuli pristupu z cele tridy
        self.label_con.setFont(font_con)
        self.label_con.setText("Connection: ")
        self.label_con.setGeometry(585, 450, 100, 20)

        self.lab_stat = QtWidgets.QLabel(self.centralwidget)  # self pred label kvuli pristupu z cele tridy
        self.lab_stat.setFont(font_con)
        self.lab_stat.setStyleSheet('color: red')
        self.lab_stat.setText("Not connected")
        self.lab_stat.setGeometry(685, 450, 300, 20)

        """------- line & label Time ------------30, 500, 400, 300"""
        time_line_coor = [100,480]
        self.line_time = QtWidgets.QFrame(self.centralwidget)
        self.line_time.setGeometry(QtCore.QRect(time_line_coor[0], time_line_coor[1], 730, 20))
        self.line_time.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_time.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_time.setObjectName("line_time")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time = QtWidgets.QLabel(self.centralwidget)  # self pred label kvuli pristupu z cele tridy
        self.label_time.setFont(font)
        self.label_time.setText("Time ")
        self.label_time.setGeometry(time_line_coor[0] - 60, time_line_coor[1], 70, 20)

        """------- line & label X - Y ------------30, 500, 400, 300"""
        x_y_line_coor = [100, 10]
        self.line_x_y = QtWidgets.QFrame(self.centralwidget)
        self.line_x_y.setGeometry(QtCore.QRect(x_y_line_coor[0], x_y_line_coor[1], 730, 20))
        self.line_x_y.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_x_y.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_x_y.setObjectName("line_time")
        font_x_y = QtGui.QFont()
        font_x_y.setPointSize(10)
        self.label_x_y = QtWidgets.QLabel(self.centralwidget)  # self pred label kvuli pristupu z cele tridy
        self.label_x_y.setFont(font_x_y)
        self.label_x_y.setText("X - Y ")
        self.label_x_y.setGeometry(x_y_line_coor[0]- 60, x_y_line_coor[1], 70, 20)

        """ ----- DATA X Y prompt (table)  ------"""
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(self.quad.tab_len)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 108)
        self.tableWidget.setColumnWidth(1, 108)
        self.tableWidget.setGeometry(580, 40, 270, 350)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("X coordinates"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Y coordinates"))
        """--------------- CASOVAC cteni dat - inicializace -----------------"""
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time_update)

    """-----------------------------------FUNKCE/METODY TRID GUI ----------------------------------------------------"""
    def Time_update(self):

        """labely grafů"""
        if self.draw_enable == 1:
            self.quad.update_figure()
            self.x_time.update_figure_two()
            self.y_time.update_figure_two()
        self.update_data()
        self.read_data()

    def update_data(self):  # fce, ktera aktualizuje parametry GUI (TABULKA, PROMENNE, LABELY)
        """AKTUALIZACE promennych z preferences"""
        """         Adaptivni osa Time      """
        if (self.d_len != self.prefWin.p_d_len) or (self.s_time != self.prefWin.p_s_time):  # prekeresleni a ukladani pouze pri zmene
            self.d_len = self.prefWin.p_d_len
            self.s_time = self.prefWin.p_s_time  # cas pro rychlost cteni
            self.x_time.s_time = self.prefWin.p_s_time  # cas pro grafy Time
            self.y_time.s_time = self.prefWin.p_s_time
            self.x_time.d_len = self.d_len  # pocet vzorku pro grafy Time
            self.y_time.d_len = self.d_len

            if (self.d_len*self.s_time) > 9000:
                self.time_label_Y.setText("Time [s]")
                self.time_label_x.setText("Time [s]")
                self.x_time.s_time = self.prefWin.p_s_time/1000  # cas pro grafy Time
                self.y_time.s_time = self.prefWin.p_s_time/1000
            else:
                self.time_label_Y.setText("Time [ms]")
                self.time_label_x.setText("Time [ms]")

            self.x_time.x_y_old = np.zeros(self.d_len)      #Reset Time - pri zmene
            self.y_time.x_y_old = np.zeros(self.d_len)

        if self.port_name != self.prefWin.p_port_name:
            self.s.close()
            self.connect()
        self.port_name = self.prefWin.p_port_name

        if self.disp_set != self.prefWin.p_disp_set:  # reaguje na zmenu
            if self.prefWin.p_disp_set == 'abs':
                self.Y_label_2.setText("[mm]")
                self.X_label.setText("coord. X [mm]")
                self.Y_label_time.setText("coord. Y [mm]")
                self.X_label_time.setText("coord. X [mm]")
                self.val_343 = 3.43
            else:
                self.Y_label_2.setText("[-]")
                self.X_label.setText("coord. X [-]")
                self.Y_label_time.setText("coord. Y [-]")
                self.X_label_time.setText("coord. X [-]")
                self.val_343 = 1

            self.quad.frame_x = [self.val_343, -self.val_343, -self.val_343, self.val_343, self.val_343]
            self.quad.frame_y = [-self.val_343, -self.val_343, self.val_343, self.val_343, -self.val_343]
            self.quad.frame_x1 = [0, 0]
            self.quad.frame_y1 = [self.val_343, -self.val_343]
            self.quad.frame_y2 = [0, 0]
            self.quad.frame_x2 = [self.val_343, -self.val_343]

            self.quad.x_old = np.zeros(self.tab_len)     #  Nulovani garfu a tabulky
            self.quad.y_old = np.zeros(self.tab_len)
            self.x_time.x_y_old = np.zeros(self.d_len)
            self.y_time.x_y_old = np.zeros(self.d_len)

        self.disp_set = self.prefWin.p_disp_set  # --- bastaveni disp - abs/rel
        self.quad.disp_set_plt = self.prefWin.p_disp_set
        self.x_time.disp_set_plt = self.prefWin.p_disp_set
        self.y_time.disp_set_plt = self.prefWin.p_disp_set
        """Zmena labelu - rel/abs"""


        """nutna podmika pro prekopani tabulky"""
        if self.tab_len != self.prefWin.p_tab_len:   # tab_len stara hosnota/ p_tab_len nova hodnota
            self.tab_len = self.prefWin.p_tab_len
            self.tableWidget.setRowCount(self.prefWin.p_tab_len)  #  Prenastaveni velikosti tabulky
            self.quad.x_old = np.zeros(self.tab_len)     #  Vytvoreni vektoru o prislusne velikosti
            self.quad.y_old = np.zeros(self.tab_len)
            self.quad.tab_len = self.tab_len
        """ PLNENI TABULKY"""
        for x in range(self.quad.tab_len):
            self.tableWidget.setItem((self.quad.tab_len-1) - x, 0, QTableWidgetItem(format(self.quad.x_old[x], '.4f')))
            self.tableWidget.setItem((self.quad.tab_len-1) - x, 1, QTableWidgetItem(format(self.quad.y_old[x], '.4f')))

        """Aktualizace dat pro vytvoreni TXT"""
        self.txtWin.data_test_x = self.x_time.x_y_old
        self.txtWin.data_test_y = self.y_time.x_y_old

        self.timer.setInterval(self.s_time)

    def read_data(self):        # Tato fce bezi NEPRETRZITE - z duvodu kontroli pripojeni Serioveho portu
        try:
            data = (self.s.readline())  # cteni z portu
            data_str = data.decode("utf-8")
            data_list = data_str.rsplit(" ")
            sum_data = float(data_list[0])
            x_data = float(data_list[1])
            y_data = float(data_list[2])
            print(sum_data, x_data, y_data)  # vypis do konzole debugging

            if sum_data == 0:  #ochrana deleni nulou
                x_div = 0
                y_div = 0
            else:
                x_div = (x_data/sum_data)
                y_div = (y_data/sum_data)

            if self.disp_set == 'abs':
                val_343 = 3.43
            else:
                val_343 = 1

            self.x_time.x_y_new = x_div * val_343
            self.y_time.x_y_new = y_div * val_343
            self.quad.X_data = x_div* val_343
            self.quad.Y_data = y_div* val_343
        except:
            self.statusBar().showMessage("Unable to read - Disconnected", 3000)
            self.lab_stat.setText("Disconnected")
            self.lab_stat.setStyleSheet('color: red')

            self.butt_conn.setText("Connect")
            self.butt_conn.setEnabled(True)
            self.con_enable = True
            self.butt_start.setEnabled(False)
            self.butt_start.setChecked(False)
            self.butt_start.setText("Start")
            self.draw_enable = 0
            self.s.close()
            self.timer.stop()  # zastaveni fce update

    """-----------------start/stop fce -----------------"""
    def clicked_st(self):
        cond = self.butt_start.isChecked()
        if not (cond):
            self.butt_start.setText("Start")
            self.draw_enable = 0
            self.statusBar().showMessage("Stopped", 2000)

        else:
            self.butt_start.setText("Stop")
            self.draw_enable = 1
            self.statusBar().showMessage("Started", 2000)

    """-----------------------connect ---------------------"""
    def connect(self):
        self.port_name = self.prefWin.p_port_name
        if self.con_enable:
            try:
                """ ----- pripojeni serioveho portu ----------"""
                self.s = serial.Serial(self.port_name, baudrate=115200, timeout=None, bytesize=8, parity='N', rtscts=0)
                print(self.s.name)
                self.timer.start(self.s_time)
                stat_con = "Connected to: " + self.s.name
                self.statusBar().showMessage(self.s.name, 3000)
                self.butt_start.setEnabled(True)
                self.butt_conn.setText("Disconnect")
                self.lab_stat.setText(str(self.s.name))
                self.lab_stat.setStyleSheet('color: green')
                self.statusBar().showMessage(stat_con, 2000)
                self.con_enable = False
            except:
                self.statusBar().showMessage("Unable to connect", 2000)
                string = "Unable to connect to: " + self.port_name
                self.lab_stat.setText(string)
                self.lab_stat.setStyleSheet('color: orange')
        else:
            self.s.close()
            self.statusBar().showMessage("Disconnected", 3000)
            self.con_enable = True
            self.butt_start.setEnabled(False)
            self.butt_conn.setText("Connect")
            self.butt_start.setText("Start")
            self.draw_enable = 0
            self.statusBar().showMessage("Stopped", 2000)

    def prefClick(self):
        self.window.show()

    def prefTxt(self):
        self.window_txt.show()


    """  ------------------ funkce z Menu --------------------"""
    def fileQuit(self):
        try:
            self.s.close()
        except:
            pass
        self.window_txt.close()
        self.window.close()
        self.close()


    def closeEvent(self, ce):
        self.fileQuit()



    def about(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """
    This is testing version of PSD, this version expect data in this order: SUM, X, Y.
    
    The PSD application is part of the Diploma thesis."""
                                    )


qApp = QtWidgets.QApplication(sys.argv)
aw = ApplicationWindow()
#aw.setWindowTitle("%s" % progname)  # nastavi titulku na nazev souboru
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()
