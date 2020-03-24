
# embedding_in_qt5.py --- Simple Qt5 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#               2015 Jens H Nielsen
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')  #Agg je renderer - vykreslujici process - moznosti WXAgg, GTKAgg, QT4Agg
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import serial

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

"""------------------------------------------ DEFINICE TRID pro vykresleni garfu------------------------------------------------------"""
class MyMplCanvas(FigureCanvas):
    """---------------------- MATERSKA TRIDA  - v podstate QWidget ---------------------"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        """ ---- PROMENNE -------"""
        self.s_time_mpl = 100  #inicializace

    def compute_initial_figure(self):
        pass


class MplQuad(MyMplCanvas):  # --------------------------------------------- HLAVNI GRAF-------------------------
    """A canvas that updates itself every second with a new plot."""
    """self pridat pred timer, tak aby by pristupny"""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

        self.X_data = 0
        self.Y_data = 0
        self.d_len = 10
        self.x_old = np.zeros(self.d_len)
        self.y_old = np.zeros(self.d_len)

        self.frame_x = [1, -1, -1, 1, 1]
        self.frame_y = [-1, -1, 1, 1, -1]
        self.frame_x1 = [0, 0]
        self.frame_y1 = [1, -1]
        self.frame_y2 = [0, 0]
        self.frame_x2 = [1, -1]

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(self.s_time_mpl)

    def compute_initial_figure(self):  # inicializace
        pass


    def update_figure(self):
        self.axes.cla()
        self.axes.plot(self.frame_x, self.frame_y, color='#8f8483', linestyle='--', linewidth=1)
        self.axes.plot(self.frame_x1, self.frame_y1, color='#8f8483', linestyle='--', linewidth=1)
        self.axes.plot(self.frame_x2, self.frame_y2, color='#8f8483', linestyle='--', linewidth=1)

        self.axes.plot(self.x_old, self.y_old, color='#f2c16d', marker='o', label='stare pozice', markersize=1)
        self.axes.plot(self.X_data, self.Y_data, color='r', marker='o', label='aktualni pozice', markersize=2)

        self.x_old = np.append(self.x_old, self.X_data)  # spojeni novych a starych dat
        self.y_old = np.append(self.y_old, self.Y_data)
        if len(self.x_old) > self.d_len:  # zobrazeni max 10 minulych prvku
            self.x_old = np.delete(self.x_old, 0)
            self.y_old = np.delete(self.y_old, 0)
        self.draw()


class MplTwo(MyMplCanvas):  #---------------------------------------- DOLNI GRAFY ------------------------------#
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        """------- PROMENNE ----------"""
        self.d_len = 100
        self.x_y_old = np.zeros(self.d_len)
        self.x_y_new = 0

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure_two)
        self.timer.start(self.s_time_mpl)

    def update_figure_two(self):
        self.axes.cla()
        x1 = np.linspace(0, self.d_len, self.d_len, endpoint=False)
        self.axes.plot(x1, self.x_y_old, 'r')
        self.draw()

        self.x_y_old = np.append(self.x_y_old, self.x_y_new) # pripoji nakonec
        self.x_y_old = np.delete(self.x_y_old,0)


"""--------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------------------------"""

class ApplicationWindow(QtWidgets.QMainWindow):
    """--------------------------------------GUI ----------------------------------------------------------------------------"""
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        #self.resize(900, 880)
        self.setGeometry(300, 150, 900, 860)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("PSD - test")

        """ ---- PROMENNE -------"""
        self.s_time = 100
        self.port_name = 'COM5'

        """----lista menu ------"""
        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)
        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        """----------QT widget layout -----------------"""
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        """ graf quad  """
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 500, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.quad = MplQuad(self.verticalLayoutWidget, width=5, height=4, dpi=100) # dc - graf XY
        self.quad.timer.stop()

        self.layout_plot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_plot.setContentsMargins(0, 0, 0, 0)
        self.layout_plot.setObjectName("layout_plot")
        self.layout_plot.addWidget(self.quad)
        """graf X v case - LAYOUT """
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 500, 400, 300))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.x_time = MplTwo(self.verticalLayoutWidget_2, width=5, height=2, dpi=100)  # dc - graf XY
        self.x_time.timer.stop()

        self.label_X = QtWidgets.QLabel(self.verticalLayoutWidget_2)  # self pred label kvuli pristupu z cele tridy
        self.label_X.setText("X samples in time")
        self.label_X.setGeometry(0, 15, 130, 18)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 50, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addWidget(self.x_time)
        """graf Y v case - LAYOUT """
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(450, 500, 400, 300))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.y_time = MplTwo(self.verticalLayoutWidget_3, width=5, height=2, dpi=100)  # dc - graf XY
        self.y_time.timer.stop()

        self.label_Y = QtWidgets.QLabel(self.verticalLayoutWidget_3)  # self pred label kvuli pristupu z cele tridy
        self.label_Y.setText("Y samples in time")
        self.label_Y.setGeometry(0, 15, 130, 20)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 50, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.addWidget(self.y_time)

        """tlacitko STart/STOP"""
        self.butt_start = QtWidgets.QPushButton(self.centralwidget)
        self.butt_start.setGeometry(QtCore.QRect(585, 440, 93, 28))
        self.butt_start.setCheckable(True)
        self.butt_start.setChecked(False)  #pocatecni stav STOP => setChecked(False)
        self.butt_start.setEnabled(False)
        self.butt_start.setObjectName("pushButton")
        self.butt_start.clicked.connect(self.clicked)
        self.butt_start.setText("Start")
        """tlacitko CONNECT """
        self.butt_conn = QtWidgets.QPushButton(self.centralwidget)
        self.butt_conn.setGeometry(QtCore.QRect(685, 440, 93, 28))
        self.butt_conn.setEnabled(True)
        self.butt_conn.setText("Connect")
        self.butt_conn.clicked.connect(self.connect)

        self.centralwidget.setFocus()
        self.setCentralWidget(self.centralwidget)

        self.statusBar().showMessage("Welcome", 2000)
        """ ----- DATA X Y prompt (table)  ------"""
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(self.quad.d_len)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, 108)
        self.tableWidget.setColumnWidth(1, 108)
        self.tableWidget.setGeometry(550, 40, 270, 350)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("X coordinates"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Y coordinates"))
        """--------------- CASOVAC cteni dat -----------------"""
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.read_data)
        #self.timer.start(self.s_time)

    """ostatni fce"""
    def read_data(self): # Tato fce bezi nepretrzite - z duvodu kontroli pripojeni

        try:
            data = (self.s.readline())
            data_str = data.decode("utf-8")
            data_list = data_str.rsplit(" ")
            sum_data = float(data_list[0])
            x_data = float(data_list[1])
            y_data = float(data_list[2])
            print(sum_data, x_data, y_data)

            if sum_data == 0:  #ochrana deleni nulou
                x_div = 0
                y_div = 0
            else:
                x_div = (x_data/sum_data)
                y_div = (y_data/sum_data)

            # if (x_data > 1.5 or x_data < -1.5):
            #     self.statusBar().showMessage("Output saturated", 2000)
            #     x_data = 0
            # if (y_data > 1.5 or y_data < -1.5):
            #     self.statusBar().showMessage("Output saturated", 2000)
            #     y_data = 0

            self.x_time.x_y_new = x_div
            self.y_time.x_y_new = y_div
            self.quad.X_data = x_div
            self.quad.Y_data = y_div
        except:
            self.statusBar().showMessage("Unable to read - Disconnected", 3000)
            self.butt_conn.setEnabled(True)
            self.butt_start.setEnabled(False)
            self.butt_start.setChecked(False)
            self.butt_start.setText("Start")

            self.timer.stop()  # zastaveni fce read
            self.quad.timer.stop()  # zasatveni update vykreslovani
            self.x_time.timer.stop()
            self.y_time.timer.stop()

        for x in range(self.quad.d_len):
            self.tableWidget.setItem(x, 0, QTableWidgetItem(format(self.quad.x_old[x], '.4f')))
            self.tableWidget.setItem(x, 1, QTableWidgetItem(format(self.quad.y_old[x], '.4f')))




    def clicked(self):
        cond = self.butt_start.isChecked()
        if not (cond):
            self.butt_start.setText("Start")
            self.quad.timer.stop() # zasatveni update vykreslovani
            self.x_time.timer.stop()
            self.y_time.timer.stop()
            self.statusBar().showMessage("Stopped", 2000)

        else:
            self.butt_start.setText("Stop")
            self.quad.timer.start(self.s_time)
            self.x_time.timer.start(self.s_time)
            self.y_time.timer.start(self.s_time)
            self.statusBar().showMessage("Started", 2000)


    def connect (self):
        try:
            """ ----- pripojeni serioveho portu ----------"""
            self.s = serial.Serial(self.port_name, baudrate=115200, timeout=None, bytesize=8, parity='N', rtscts=0)
            print(self.s.name)
            self.timer.start(self.s_time)
            stat_con = "Connected to: " + self.s.name
            self.statusBar().showMessage(self.s.name, 3000)
            self.butt_start.setEnabled(True)
            self.butt_conn.setEnabled(False)
            self.statusBar().showMessage(stat_con, 2000)
        except:
            self.statusBar().showMessage("Unable to connect", 2000)



    """  funkce z Menu"""
    def fileQuit(self):
        self.s.close()
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
