
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
        self.x_old = []
        self.y_old = []
        self.d_len = 30

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

        self.x_old.append(self.X_data)  # spojeni novych a starych dat
        self.y_old.append(self.Y_data)
        if len(self.x_old) > self.d_len:  # zobrazeni max 10 minulych prvku
            self.x_old.pop(0)
            self.y_old.pop(0)
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
        self.resize(900, 880)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("PSD - test")

        """ ---- PROMENNE -------"""
        self.s_time = 120



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
        self.quad.s_time_mpl = self.s_time
        self.layout_plot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_plot.setContentsMargins(0, 0, 0, 0)
        self.layout_plot.setObjectName("layout_plot")
        self.layout_plot.addWidget(self.quad)
        """graf X v case - LAYOUT """
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 500, 400, 300))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.x_time = MplTwo(self.verticalLayoutWidget_2, width=5, height=2, dpi=100)  # dc - graf XY
        self.x_time.s_time_mpl = self.s_time

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
        self.y_time.s_time_mpl = self.s_time

        self.label_Y = QtWidgets.QLabel(self.verticalLayoutWidget_3)  # self pred label kvuli pristupu z cele tridy
        self.label_Y.setText("Y samples in time")
        self.label_Y.setGeometry(0, 15, 130, 20)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 50, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.addWidget(self.y_time)

        """tlacitko STart/STOP"""
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 70, 93, 28))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton.setText("Stop")

        self.centralwidget.setFocus()
        self.setCentralWidget(self.centralwidget)

        self.statusBar().showMessage("Testovaci software", 2000)

        """ ----- inicializace serioveho prenosu ----------"""
        self.s = serial.Serial('COM5', baudrate=115200, timeout=None, bytesize=8, parity='N', rtscts=0)
        print(self.s.name)

        """--------------- CASOVAC cteni dat -----------------"""
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.read_data)
        self.timer.start(self.s_time)

    """ostatni fce"""
    def read_data(self):
        data = (self.s.readline())
        testing = data[len(data) - 3]
        if testing != 32:  # mezera (ASCII - 32) po Wait
            data_str = data.decode("utf-8")
            data_list = data_str.rsplit(" ")
            x_data = float(data_list[1])
            y_data = float(data_list[3])
            print(x_data, y_data)

            if (x_data > 1.5 or x_data < -1.5):
                self.statusBar().showMessage("Output saturated", 2000)
                x_data = 0
            if (y_data > 1.5 or y_data < -1.5):
                self.statusBar().showMessage("Output saturated", 2000)
                y_data = 0

            self.x_time.x_y_new = x_data
            self.y_time.x_y_new = y_data
            self.quad.X_data = x_data
            self.quad.Y_data = y_data

    def clicked(self):
        cond = self.pushButton.isChecked()
        if cond:
            self.pushButton.setText("Start")
            self.timer.stop()  # zastaveni fce read
            self.quad.timer.stop() # zasatveni update vykreslovani
            self.x_time.timer.stop()
            self.y_time.timer.stop()

        else:
            self.pushButton.setText("Stop")
            self.timer.start(self.s_time)
            self.quad.timer.start(self.s_time) # zasatveni update vykreslovani
            self.x_time.timer.start(self.s_time)
            self.y_time.timer.start(self.s_time)

    """ automaticky volajici funkce """
    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()



    def about(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """embedding_in_qt5.py example
Copyright 2005 Florent Rougon, 2006 Darren Dale, 2015 Jens H Nielsen

This program is a simple example of a Qt5 application embedding matplotlib
canvases.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.

This is modified from the embedding in qt4 example to show the difference
between qt4 and qt5"""
                                    )


qApp = QtWidgets.QApplication(sys.argv)

aw = ApplicationWindow()
#aw.setWindowTitle("%s" % progname)  # nastavi titulku na nazev souboru
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()
