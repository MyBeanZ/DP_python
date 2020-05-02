
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Preferences_win(object):
    def setupUi(self, OtherWindow, tab_len,  d_len, s_time, disp_set, port_name, in_mode):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.setGeometry(1300, 100, 435, 570)
        OtherWindow.setWindowTitle("Preferences")

        """ PROMENNE"""
        self.val_343 = 3.43  # mm
        """ Limits """
        self.max_tab_len = 5000  # delka tabulky
        self.min_tab_len = 1
        self.max_time = 10000    #update delay
        self.min_time = 1
        self.max_d_len = 500000   #casova osa
        self.min_d_len = 5
        self.max_freq = 120000  # AC frekvence
        self.min_freq = 1500
        self.max_dis = 5000
        self.max_spot_x = self.val_343
        self.max_spot_y = self.val_343
        """ Actual values"""
        self.p_d_len = d_len
        self.p_s_time = s_time
        self.p_port_name = port_name
        self.p_disp_set = disp_set
        self.p_tab_len = tab_len
        self.p_in_mode = in_mode
        self.p_carry_f = 100000
        self.p_phase = 0
        self.p_distance = 0
        self.p_spot_rad_x = 1
        self.p_spot_rad_y = 1
        self.p_circ_elips = "circ"

        self.p_cal_factor_x = 1
        self.p_cal_factor_y = 1

        self.x_res = 1
        self.y_res = 1
        self.max_res = self.val_343*2



        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        OtherWindow.setCentralWidget(self.centralwidget)

        """------- General setup LINE ------------"""
        gen_line_coor = [25, 10]
        self.line_spot_gen = QtWidgets.QFrame(self.centralwidget)
        self.line_spot_gen.setGeometry(QtCore.QRect(gen_line_coor[0] + 100, gen_line_coor[1], 170, 20))
        self.line_spot_gen.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_spot_gen.setFrameShadow(QtWidgets.QFrame.Sunken)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_spot_gen = QtWidgets.QLabel(self.centralwidget)  # self pred label kvuli pristupu z cele tridy
        self.label_spot_gen.setFont(font)
        self.label_spot_gen.setText("General settings")
        self.label_spot_gen.setGeometry(gen_line_coor[0] - 15, gen_line_coor[1], 110, 20)
        """labels Actual val."""
        self.label_val = QtWidgets.QLabel(self.centralwidget)
        self.label_val.setGeometry(gen_line_coor[0] + 290, gen_line_coor[1], 100, 20)
        self.label_val.setText("Current values:")
        self.label_val.setFont(font)
        """---------------- DELKA vzorku TIME d_len--------------"""
        coor_len = [gen_line_coor[0], gen_line_coor[1] + 24]
        self.label_len = QtWidgets.QLabel(self.centralwidget)
        self.label_len.setGeometry(QtCore.QRect(coor_len[0], coor_len[1], 100, 20))
        self.label_len.setText("Time samples:")

        self.text_len = QLineEdit(self.centralwidget)
        self.text_len.setPlaceholderText("Max: " + str(self.max_d_len) + ", Min: " + str(self.min_d_len))
        self.text_len.setGeometry(QtCore.QRect(coor_len[0] + 110, coor_len[1], 130, 20))

        self.label_val_d_len = QtWidgets.QLabel(self.centralwidget)
        self.label_val_d_len.setGeometry(QtCore.QRect(309, coor_len[1], 100, 20))
        self.label_val_d_len.setText(str(self.p_d_len) + " samples")


        self.butt_len = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_len.setGeometry(265, coor_len[1], 40, 20)
        self.butt_len.clicked.connect(lambda: self.set_d_len())
        """---------------- DELKA Tabulky tab_len--------------"""

        coor_tab = [coor_len[0], coor_len[1] + 24]
        self.label_tab_len = QtWidgets.QLabel(self.centralwidget)
        self.label_tab_len.setGeometry(QtCore.QRect(coor_tab[0], coor_tab[1], 100, 20))
        self.label_tab_len.setText("Table length:")

        self.text_tab_len = QLineEdit(self.centralwidget)
        self.text_tab_len.setPlaceholderText("Max: " + str( self.max_tab_len) + ", Min:" + str(self.min_tab_len))
        self.text_tab_len.setGeometry(QtCore.QRect(coor_tab[0] + 110, coor_tab[1], 130, 20))

        self.label_val_tab_len = QtWidgets.QLabel(self.centralwidget)
        self.label_val_tab_len.setGeometry(QtCore.QRect(309, coor_tab[1], 100, 20))
        self.label_val_tab_len.setText(str(self.p_tab_len) + " samples")

        self.butt_tab_len = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_tab_len.setGeometry(QtCore.QRect(265, coor_tab[1], 40, 20))
        self.butt_tab_len.clicked.connect(lambda: self.set_tab())

        """--------------cas aktualizace time ------------------"""
        coor_time = [coor_tab[0], coor_tab[1] + 24]
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(coor_time[0], coor_time[1], 110, 20))
        self.label_time.setText("Update delay (ms):")

        self.text_time = QLineEdit(self.centralwidget)
        self.text_time.setPlaceholderText("Max:" + str(self.max_time) + ", Min: " + str(self.min_time))
        self.text_time.setGeometry(QtCore.QRect(coor_time[0] + 110, coor_time[1], 130, 20))

        self.label_val_time = QtWidgets.QLabel(self.centralwidget)
        self.label_val_time.setGeometry(QtCore.QRect(309, coor_time[1], 100, 20))
        self.label_val_time.setText(str(self.p_s_time)+" ms")

        self.butt_time = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_time.setGeometry(QtCore.QRect(265, coor_time[1], 40, 20))
        self.butt_time.clicked.connect(lambda: self.set_time())

        """ -------------- jmeno portu -----------------"""
        coor_port = [coor_time[0], coor_time[1] + 24]
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(coor_port[0], coor_port[1], 100, 20))
        self.label_port.setText('Port name:')

        self.text_port = QLineEdit(self.centralwidget)
        self.text_port.setPlaceholderText("example: COM5")
        self.text_port.setGeometry(QtCore.QRect(coor_port[0] + 110, coor_port[1], 130, 20))

        self.butt_port = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_port.setGeometry(QtCore.QRect(265, coor_port[1], 40, 20))
        self.butt_port.clicked.connect(self.Set_port)

        self.label_val_port = QtWidgets.QLabel(self.centralwidget)
        self.label_val_port.setGeometry(QtCore.QRect(309, coor_port[1], 100, 20))
        self.label_val_port.setText(self.p_port_name)

        """ ------------Zobrazeni v REL nabo ABS"""
        coor_disp = [coor_port[0], coor_port[1] + 24]
        self.label_disp = QtWidgets.QLabel(self.centralwidget)
        self.label_disp.setGeometry(QtCore.QRect(coor_disp[0], coor_disp[1], 200, 20))
        self.label_disp.setText("Relative val.:")

        self.disp_box = QCheckBox(self.centralwidget)
        self.disp_box.setText("Absolute/Relative display")
        self.disp_box.setChecked(False)
        self.disp_box.setGeometry(QtCore.QRect(coor_disp[0] + 110, coor_disp[1], 200, 20))
        self.disp_box.toggled.connect(self.disp_clik)

        """------- Firmware setup LINE ------------"""
        firm_line_coor = [coor_disp[0], coor_disp[1] + 24]
        self.line_spot_dim = QtWidgets.QFrame(self.centralwidget)
        self.line_spot_dim.setGeometry(QtCore.QRect(firm_line_coor[0] + 90, firm_line_coor[1], 300, 20))
        self.line_spot_dim.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_spot_dim.setFrameShadow(QtWidgets.QFrame.Sunken)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_spot_dim = QtWidgets.QLabel(self.centralwidget)  # self pred label kvuli pristupu z cele tridy
        self.label_spot_dim.setFont(font)
        self.label_spot_dim.setText("Firmware setup")
        self.label_spot_dim.setGeometry(firm_line_coor[0] - 15, firm_line_coor[1], 100, 20)
        """ ------------AC/DC mode - Correlation / RMS ------------"""
        coor_mode = [firm_line_coor[0], firm_line_coor[1] + 24]
        self.label_mode = QtWidgets.QLabel(self.centralwidget)
        self.label_mode.setGeometry(QtCore.QRect(coor_mode[0], coor_mode[1], 40, 20))
        self.label_mode.setText("Mode:")

        self.label_mode_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_mode_2.setGeometry(QtCore.QRect(coor_mode[0]+40, coor_mode[1], 100, 20))
        self.label_mode_2.setText("RMS")
        self.label_mode_2.setStyleSheet('color: red')

        self.mode_box = QCheckBox(self.centralwidget)
        self.mode_box.setText("Correlation / RMS")
        self.mode_box.setChecked(False)
        self.mode_box.setGeometry(QtCore.QRect(coor_mode[0] + 110, coor_mode[1], 200, 20))
        self.mode_box.toggled.connect(self.set_mode)

        """--------------freq set ------------------"""
        coor_ac = [coor_mode[0], coor_mode[1] + 24]
        self.label_ac = QtWidgets.QLabel(self.centralwidget)
        self.label_ac.setGeometry(QtCore.QRect(coor_ac[0], coor_ac[1], 110, 20))
        self.label_ac.setText("Carry freq. (Hz):")

        self.text_ac = QLineEdit(self.centralwidget)
        self.text_ac.setPlaceholderText("Max:" + str(self.max_freq/1000)+" kHz" + ", Min:" + str(self.min_freq)+" Hz")
        self.text_ac.setGeometry(QtCore.QRect(coor_ac[0] + 110, coor_ac[1], 180, 20))

        self.label_val_ac = QtWidgets.QLabel(self.centralwidget)
        self.label_val_ac.setGeometry(QtCore.QRect(359, coor_ac[1], 100, 20))
        self.label_val_ac.setText(str(self.p_carry_f) + " Hz")

        self.butt_ac = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_ac.setGeometry(QtCore.QRect(315, coor_ac[1], 40, 20))
        self.butt_ac.clicked.connect(lambda: self.set_freq())

        """--------------Distance set ------------------"""
        coor_dis = [coor_ac[0], coor_ac[1] + 24]
        self.label_dis = QtWidgets.QLabel(self.centralwidget)
        self.label_dis.setGeometry(QtCore.QRect(coor_dis[0], coor_dis[1], 110, 20))
        self.label_dis.setText("Distance (m):")

        self.text_dis = QLineEdit(self.centralwidget)
        self.text_dis.setPlaceholderText("Max:" + str(self.max_dis)+" m")
        self.text_dis.setGeometry(QtCore.QRect(coor_dis[0] + 110, coor_dis[1], 130, 20))

        self.label_val_dis = QtWidgets.QLabel(self.centralwidget)
        self.label_val_dis.setGeometry(QtCore.QRect(309, coor_dis[1], 100, 20))
        self.label_val_dis.setText(str(self.p_distance) + " m")

        self.butt_dis = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_dis.setGeometry(QtCore.QRect(265, coor_dis[1], 40, 20))
        self.butt_dis.clicked.connect(lambda: self.set_dis())

        """------- line & label SPOT Dimensions------------"""
        dim_line_coor = [coor_dis[0], coor_dis[1] + 24]
        self.line_spot_dim = QtWidgets.QFrame(self.centralwidget)
        self.line_spot_dim.setGeometry(QtCore.QRect(dim_line_coor[0] + 90, dim_line_coor[1], 300, 20))
        self.line_spot_dim.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_spot_dim.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_spot_dim.setObjectName("line_time")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_spot_dim = QtWidgets.QLabel(self.centralwidget)  # self pred label kvuli pristupu z cele tridy
        self.label_spot_dim.setFont(font)
        self.label_spot_dim.setText("Spot dimensions ")
        self.label_spot_dim.setGeometry(dim_line_coor[0] - 15, dim_line_coor[1], 100, 20)
        """--------------X - Spot radius (width) set ------------------"""
        coor_spot_x = [dim_line_coor[0], dim_line_coor[1] + 24]
        self.label_spot_x = QtWidgets.QLabel(self.centralwidget)
        self.label_spot_x.setGeometry(QtCore.QRect(coor_spot_x[0], coor_spot_x[1], 110, 20))
        self.label_spot_x.setText("Spot X rad. (mm):")

        self.text_spot_x = QLineEdit(self.centralwidget)
        self.text_spot_x.setPlaceholderText("Max:" + str(self.max_spot_x) + " mm")
        self.text_spot_x.setGeometry(QtCore.QRect(coor_spot_x[0] + 110, coor_spot_x[1], 130, 20))

        self.label_val_spot_x = QtWidgets.QLabel(self.centralwidget)
        self.label_val_spot_x.setGeometry(QtCore.QRect(309, coor_spot_x[1], 100, 20))
        self.label_val_spot_x.setText(str(self.p_spot_rad_x) + " mm")


        self.butt_spot_x = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_spot_x.setGeometry(QtCore.QRect(265, coor_spot_x[1], 40, 20))
        self.butt_spot_x.clicked.connect(lambda: self.set_rad_x())

        """--------------Y - Spot radius (width) set ------------------"""
        coor_spot_y = [coor_spot_x[0], coor_spot_x[1] + 24]
        self.label_spot_y = QtWidgets.QLabel(self.centralwidget)
        self.label_spot_y.setGeometry(QtCore.QRect(coor_spot_y[0], coor_spot_y[1], 110, 20))
        self.label_spot_y.setText("Spot Y rad. (mm):")

        self.text_spot_y = QLineEdit(self.centralwidget)
        self.text_spot_y.setPlaceholderText("Max:" + str(self.max_spot_y) + " mm")
        self.text_spot_y.setGeometry(QtCore.QRect(coor_spot_y[0] + 110, coor_spot_y[1], 130, 20))

        self.label_val_spot_y = QtWidgets.QLabel(self.centralwidget)
        self.label_val_spot_y.setGeometry(QtCore.QRect(309, coor_spot_y[1], 100, 20))
        self.label_val_spot_y.setText(str(self.p_spot_rad_y) + " mm")

        self.butt_spot_y = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_spot_y.setGeometry(QtCore.QRect(265, coor_spot_y[1], 40, 20))
        self.butt_spot_y.clicked.connect(lambda: self.set_rad_y())

        """------------- line & label Calibration ------------------------------------------------------"""
        cal_line_coor = [coor_spot_y[0], coor_spot_y[1] + 24]

        self.line_spot_cal = QtWidgets.QFrame(self.centralwidget)
        self.line_spot_cal.setGeometry(QtCore.QRect(cal_line_coor[0] + 90, cal_line_coor[1], 300, 20))
        self.line_spot_cal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_spot_cal.setFrameShadow(QtWidgets.QFrame.Sunken)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_spot_cal = QtWidgets.QLabel(self.centralwidget)  # self pred label kvuli pristupu z cele tridy
        self.label_spot_cal.setFont(font)
        self.label_spot_cal.setText("Spot calibration ")
        self.label_spot_cal.setGeometry(cal_line_coor[0] - 15, cal_line_coor[1], 100, 20)
        """ ------------Calibration ON/OFF ------------"""
        coor_cal_onof = [cal_line_coor[0], cal_line_coor[1] + 24]

        self.label_cal_onof = QtWidgets.QLabel(self.centralwidget)
        self.label_cal_onof.setGeometry(QtCore.QRect(coor_cal_onof[0], coor_cal_onof[1], 100, 20))
        self.label_cal_onof.setText("Calibration: OFF")

        self.mode_cal_onof = QCheckBox(self.centralwidget)
        self.mode_cal_onof.setText("ON / OFF")
        self.mode_cal_onof.setChecked(False)
        self.mode_cal_onof.setGeometry(QtCore.QRect(coor_cal_onof[0] + 110, coor_cal_onof[1], 200, 20))
        self.mode_cal_onof.toggled.connect(self.set_cal_onof)
        """-------------- X min - X max lables------------------"""
        coor_x_min_max = [coor_cal_onof[0], coor_cal_onof[1] + 24]

        self.label_x_min = QtWidgets.QLabel(self.centralwidget)
        self.label_x_min.setGeometry(QtCore.QRect(coor_x_min_max[0], coor_x_min_max[1], 80, 20))
        self.label_x_min.setText("X min (mm):")

        self.label_x_max = QtWidgets.QLabel(self.centralwidget)
        self.label_x_max.setGeometry(QtCore.QRect(coor_x_min_max[0] + 115, coor_x_min_max[1], 80, 20))
        self.label_x_max.setText("X max (mm):")

        self.label_x_min_max = QtWidgets.QLabel(self.centralwidget)
        self.label_x_min_max.setGeometry(QtCore.QRect(coor_x_min_max[0] + 230, coor_x_min_max[1], 105, 20))
        self.label_x_min_max.setText("X max-min (mm):")
        """ ----------- X min max boxes--------------"""
        coor_x_min_max_box = [coor_x_min_max[0], coor_x_min_max[1] + 24]

        self.text_x_min = QLineEdit(self.centralwidget)
        #self.text_x_min.setPlaceholderText("Max:" + str(self.max_res) + " mm")
        self.text_x_min.setGeometry(QtCore.QRect(coor_x_min_max_box[0], coor_x_min_max_box[1], 100, 20))

        self.text_x_max = QLineEdit(self.centralwidget)
        #self.text_x_max.setPlaceholderText("Max:" + str(self.max_res) + " mm")
        self.text_x_max.setGeometry(QtCore.QRect(coor_x_min_max_box[0] + 115, coor_x_min_max_box[1], 100, 20))

        self.text_x_min_max = QLineEdit(self.centralwidget)
        self.text_x_min_max.setPlaceholderText("Max:" + str(self.max_res) + " mm")
        self.text_x_min_max.setGeometry(QtCore.QRect(coor_x_min_max_box[0] + 230, coor_x_min_max_box[1], 100, 20))

        self.butt_x_res = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_x_res.setGeometry(QtCore.QRect(coor_x_min_max_box[0] + 340, coor_x_min_max_box[1], 40, 20))
        self.butt_x_res.clicked.connect(lambda: self.set_cal_x())

        coor_x_result = [coor_x_min_max_box[0], coor_x_min_max_box[1] + 24]

        self.label_x_res = QtWidgets.QLabel(self.centralwidget)
        self.label_x_res.setGeometry(QtCore.QRect(coor_x_result[0] , coor_x_result[1], 105, 20))
        self.label_x_res.setText("X max-min (mm):")

        self.label_x_res_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_x_res_2.setGeometry(QtCore.QRect(coor_x_result[0] + 110, coor_x_result[1], 110, 20))
        self.label_x_res_2.setText(" ")

        """-------------- Y min - Y max lables------------------"""
        coor_y_min_max = [coor_x_result[0], coor_x_result[1] + 24]

        self.label_y_min = QtWidgets.QLabel(self.centralwidget)
        self.label_y_min.setGeometry(QtCore.QRect(coor_y_min_max[0], coor_y_min_max[1], 80, 20))
        self.label_y_min.setText("Y min (mm):")

        self.label_y_max = QtWidgets.QLabel(self.centralwidget)
        self.label_y_max.setGeometry(QtCore.QRect(coor_y_min_max[0] + 115, coor_y_min_max[1], 80, 20))
        self.label_y_max.setText("Y max (mm):")

        self.label_y_min_max = QtWidgets.QLabel(self.centralwidget)
        self.label_y_min_max.setGeometry(QtCore.QRect(coor_y_min_max[0] + 230, coor_y_min_max[1], 105, 20))
        self.label_y_min_max.setText("Y max-min (mm):")
        """ ----------- Y min max boxes--------------"""
        coor_y_min_max_box = [coor_y_min_max[0], coor_y_min_max[1] + 24]

        self.text_y_min = QLineEdit(self.centralwidget)
        #self.text_y_min.setPlaceholderText("Max:" + str(self.max_res) + " mm")
        self.text_y_min.setGeometry(QtCore.QRect(coor_y_min_max_box[0], coor_y_min_max_box[1], 100, 20))

        self.text_y_max = QLineEdit(self.centralwidget)
        #self.text_y_max.setPlaceholderText("Max:" + str(self.max_res) + " mm")
        self.text_y_max.setGeometry(QtCore.QRect(coor_y_min_max_box[0] + 115, coor_y_min_max_box[1], 100, 20))

        self.text_y_min_max = QLineEdit(self.centralwidget)
        self.text_y_min_max.setPlaceholderText("Max:" + str(self.max_res) + " mm")
        self.text_y_min_max.setGeometry(QtCore.QRect(coor_y_min_max_box[0] + 230, coor_y_min_max_box[1], 100, 20))

        self.butt_y_res = QtWidgets.QPushButton("Set", self.centralwidget)
        self.butt_y_res.setGeometry(QtCore.QRect(coor_y_min_max_box[0] + 340, coor_y_min_max_box[1], 40, 20))
        self.butt_y_res.clicked.connect(lambda: self.set_cal_y())

        coor_y_result = [coor_y_min_max_box[0], coor_y_min_max_box[1] + 24]

        self.label_y_res = QtWidgets.QLabel(self.centralwidget)
        self.label_y_res.setGeometry(QtCore.QRect(coor_y_result[0], coor_y_result[1], 105, 20))
        self.label_y_res.setText("Y max-min (mm):")

        self.label_y_res_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_y_res_2.setGeometry(QtCore.QRect(coor_y_result[0] + 110, coor_y_result[1], 170, 20))
        self.label_y_res_2.setText(" ")


        """vypocet faktoru"""
        coor_factor = [coor_y_result[0], coor_y_result[1] + 24]

        self.label_factor = QtWidgets.QLabel(self.centralwidget)
        self.label_factor.setGeometry(QtCore.QRect(coor_factor[0], coor_factor[1], 40, 20))
        self.label_factor.setText("Factor:")

        self.label_factor_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_factor_2.setGeometry(QtCore.QRect(coor_factor[0] + 50, coor_factor[1], 250, 20))
        self.label_factor_2.setText(" ")


        self.butt_factor = QtWidgets.QPushButton("Calculate", self.centralwidget)
        self.butt_factor.setGeometry(QtCore.QRect(coor_factor[0] + 300, coor_factor[1], 70, 20))
        self.butt_factor.clicked.connect(lambda: self.set_factor())

        self.set_cal_onof()
        """grayout freq"""
        self.butt_ac.setEnabled(False)
        self.label_val_ac.setStyleSheet('color: grey')
        self.label_ac.setStyleSheet('color: grey')
        """grayout distance set"""
        self.butt_dis.setEnabled(False)
        self.label_val_dis.setStyleSheet('color: grey')
        self.label_dis.setStyleSheet('color: grey')
        """-----------others -----------------------"""
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(OtherWindow)
    """------------------------------------ FCE/METODY -------------------------------------------"""
    def Set_port(self):
        name = self.text_port.text()
        if name == "":
            self.label_val_port.setText(self.p_port_name)
            self.label_val_port.setStyleSheet('color: black')
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

    def set_mode(self):
        if not (self.mode_box.checkState()):
            self.label_mode_2.setText(' RMS')
            self.label_mode_2.setStyleSheet('color: red')
            """grayout freq"""
            self.butt_ac.setEnabled(False)
            self.label_val_ac.setStyleSheet('color: grey')
            self.label_ac.setStyleSheet('color: grey')
            self.p_in_mode = 'DC'
            """grayout distance set"""
            self.butt_dis.setEnabled(False)
            self.label_val_dis.setStyleSheet('color: grey')
            self.label_dis.setStyleSheet('color: grey')
        else:
            self.label_mode_2.setText('Correlation')
            self.label_mode_2.setStyleSheet('color: blue')
            """enable freq set"""
            self.butt_ac.setEnabled(True)
            self.label_val_ac.setStyleSheet('color: black')
            self.label_ac.setStyleSheet('color: black')
            """enable distance set"""
            self.butt_dis.setEnabled(True)
            self.label_val_dis.setStyleSheet('color: black')
            self.label_dis.setStyleSheet('color: black')
            self.p_in_mode = 'AC'

    def set_val_gen(self, text_obj, label_val, p_val, max_val, min_val, unit, type):
        name = text_obj.text()
        text_obj.clear()
        if name == "":
            label_val.setText(str(p_val) + " " + unit)
            label_val.setStyleSheet('color: black')
        else:
            try:
                if type == 'f':
                    if float(name) > max_val:
                        p_val = max_val
                    elif float(name) < min_val:
                        p_val = min_val
                    else:
                        p_val = float(name)
                else:
                    if int(name) > max_val:
                        p_val = max_val
                    elif int(name) < min_val:
                        p_val = min_val
                    else:
                        p_val = int(name)

                label_val.setText(str(p_val) + " " + unit)
                label_val.setStyleSheet('color: black')
                print(p_val)
            except:
                label_val.setStyleSheet('color: red')
                label_val.setText("NaN")
        return p_val

    def set_d_len(self):
        val = self.p_d_len
        self.p_d_len = self.set_val_gen(self.text_len, self.label_val_d_len, val, self.max_d_len, self.min_d_len, "samples", 'int')

    def set_tab(self):
        val = self.p_tab_len
        self.p_tab_len = self.set_val_gen(self.text_tab_len, self.label_val_tab_len, val, self.max_tab_len, self.min_tab_len, "samples", 'int')

    def set_time(self):
        val = self.p_s_time
        self.p_s_time = self.set_val_gen(self.text_time, self.label_val_time, val, self.max_time, self.min_time, "ms", 'int')

    def set_freq(self):
        val = self.p_carry_f
        self.p_carry_f = self.set_val_gen(self.text_ac, self.label_val_ac, val, self.max_freq, self.min_freq, "Hz",'int')

    def set_dis(self):
        val = self.p_distance
        self.p_distance = self.set_val_gen(self.text_dis, self.label_val_dis, val, self.max_dis, 0, "m", 'f')

    def set_rad_x(self):
        val = self.p_spot_rad_x
        self.p_spot_rad_x = self.set_val_gen(self.text_spot_x, self.label_val_spot_x, val, self.max_spot_x, 0, "mm", 'f')

    def set_rad_y(self):
        val = self.p_spot_rad_y
        self.p_spot_rad_y = self.set_val_gen(self.text_spot_y, self.label_val_spot_y, val, self.max_spot_y, 0, "mm", 'f')

    def set_cal_onof(self):
        if self.mode_cal_onof.checkState():
            self.label_cal_onof.setText("Calibration: ON")

            self.butt_x_res.setEnabled(True)
            self.label_x_min.setStyleSheet('color: black')
            self.label_x_max.setStyleSheet('color: black')
            self.label_x_min_max.setStyleSheet('color: black')
            self.label_x_res_2.setStyleSheet('color: black')
            self.label_x_res.setStyleSheet('color: black')

            self.butt_y_res.setEnabled(True)
            self.label_y_min.setStyleSheet('color: black')
            self.label_y_max.setStyleSheet('color: black')
            self.label_y_min_max.setStyleSheet('color: black')
            self.label_y_res_2.setStyleSheet('color: black')
            self.label_y_res.setStyleSheet('color: black')

            self.label_factor.setStyleSheet('color: black')
            self.label_factor_2.setStyleSheet('color: black')
            self.butt_factor.setEnabled(True)

            self.label_spot_x.setStyleSheet('color: grey')
            self.label_val_spot_x.setStyleSheet('color: grey')
            self.butt_spot_x.setEnabled(False)
            self.label_spot_y.setStyleSheet('color: grey')
            self.label_val_spot_y.setStyleSheet('color: grey')
            self.butt_spot_y.setEnabled(False)

        else:
            self.label_cal_onof.setText("Calibration: OFF")

            self.butt_x_res.setEnabled(False)
            self.label_x_min.setStyleSheet('color: grey')
            self.label_x_max.setStyleSheet('color: grey')
            self.label_x_min_max.setStyleSheet('color: grey')
            self.label_x_res_2.setStyleSheet('color: grey')
            self.label_x_res.setStyleSheet('color: grey')

            self.butt_y_res.setEnabled(False)
            self.label_y_min.setStyleSheet('color: grey')
            self.label_y_max.setStyleSheet('color: grey')
            self.label_y_min_max.setStyleSheet('color: grey')
            self.label_y_res_2.setStyleSheet('color: grey')
            self.label_y_res.setStyleSheet('color: grey')

            self.label_factor.setStyleSheet('color: grey')
            self.label_factor_2.setStyleSheet('color: grey')
            self.butt_factor.setEnabled(False)

            self.label_spot_x.setStyleSheet('color: black')
            self.label_val_spot_x.setStyleSheet('color: black')
            self.butt_spot_x.setEnabled(True)
            self.label_spot_y.setStyleSheet('color: black')
            self.label_val_spot_y.setStyleSheet('color: black')
            self.butt_spot_y.setEnabled(True)

            self.p_cal_factor_x = 1
            self.p_cal_factor_y = 1
            self.label_factor_2.setText(" ")
            self.x_res = 1
            self.label_x_res_2.setText(str(self.x_res) + " mm")
            self.y_res = 1
            self.label_y_res_2.setText(str(self.y_res) + " mm")

    def set_cal_x(self):
        name_min = self.text_x_min.text()
        name_max = self.text_x_max.text()
        name_res = self.text_x_min_max.text()
        self.text_x_min.clear()
        self.text_x_max.clear()
        self.text_x_min_max.clear()

        if (name_min == "") and (name_res == "") and (name_min == ""):
            self.label_x_res_2.setText(str(self.x_res) + " mm")
            self.label_x_res_2.setStyleSheet('color: black')
        else:
            try:
                if name_res:
                    self.x_res = float(name_res)

                    if self.x_res > self.max_res:
                        self.x_res = self.max_res
                    elif self.x_res < -self.max_res:
                        self.x_res = -self.max_res
                    else:
                        pass
                    self.label_x_res_2.setText(str(self.x_res) + " mm")
                    self.p_spot_rad_x = self.x_res/2

                elif name_min and name_max:
                    self.x_res = float(name_max) - float(name_min)

                    if self.x_res > self.max_res:
                        self.x_res = self.max_res
                    elif self.x_res < -self.max_res:
                        self.x_res = -self.max_res
                    else:
                        pass
                    self.p_spot_rad_x = self.x_res/2
                    self.label_x_res_2.setText(str(self.x_res) + " mm")

                else:
                    self.label_x_res_2.setText("Values uncomplete")
                    self.label_x_res_2.setStyleSheet('color: red')
            except:
                self.label_x_res_2.setStyleSheet('color: red')
                self.label_x_res_2.setText("NaN")

    def set_cal_y(self):
        name_min = self.text_y_min.text()
        name_max = self.text_y_max.text()
        name_res = self.text_y_min_max.text()
        self.text_y_min.clear()
        self.text_y_max.clear()
        self.text_y_min_max.clear()
        if (name_min == "") and (name_res == "") and (name_min == ""):
            self.label_y_res_2.setText(str(self.y_res) + " mm")
            self.label_y_res_2.setStyleSheet('color: black')
        else:
            try:
                if name_res:
                    self.y_res = float(name_res)

                    if self.y_res > self.max_res:
                        self.y_res = self.max_res
                    elif self.y_res < -self.max_res:
                        self.y_res = -self.max_res
                    else:
                        pass
                    self.label_y_res_2.setText(str(self.y_res) + " mm")
                    self.p_spot_rad_y = self.y_res/2

                elif name_min and name_max:
                    self.y_res = float(name_max) - float(name_min)

                    if self.y_res > self.max_res:
                        self.y_res = self.max_res
                    elif self.y_res < -self.max_res:
                        self.y_res = -self.max_res
                    else:
                        pass
                    self.p_spot_rad_y = self.y_res/2
                    self.label_y_res_2.setText(str(self.y_res) + " mm")

                else:
                    self.label_y_res_2.setText("Values uncomplete")
                    self.label_y_res_2.setStyleSheet('color: red')
            except:
                self.label_y_res_2.setStyleSheet('color: red')
                self.label_y_res_2.setText("NaN")

    def set_factor(self):
        if self.x_res > self.y_res:
            self.p_cal_factor_x = self.y_res/self.x_res
            self.p_cal_factor_y = 1
            #self.label_factor_2.setText("X scaled down with factor: " + str(self.p_cal_factor_x))
            self.label_factor_2.setText("X scaled down with factor: " + "{:6.4f}".format(self.p_cal_factor_x))
            self.label_factor_2.setStyleSheet('color: #990000')
        elif self.x_res < self.y_res:
            self.p_cal_factor_x = 1
            self.p_cal_factor_y = self.x_res/self.y_res
            self.label_factor_2.setText("Y scaled down with factor: " +"{:6.4f}".format(self.p_cal_factor_y))
            self.label_factor_2.setStyleSheet('color: #990000')
        else:
            self.p_cal_factor_x = 1
            self.p_cal_factor_y = 1
            self.label_factor_2.setText("1")
            self.label_factor_2.setStyleSheet('color: black')


if __name__ == "__main__":  # pro testovani
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Preferences_win()
    ui.setupUi(OtherWindow,10,100,1000,'rel','COM5', 'AC')
    OtherWindow.show()
    sys.exit(app.exec_())