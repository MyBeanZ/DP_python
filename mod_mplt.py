from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

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

    """self pridat pred timer, tak aby by pristupny"""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

        self.X_data = 0
        self.Y_data = 0
        self.tab_len = 30
        self.x_old = np.zeros(self.tab_len)
        self.y_old = np.zeros(self.tab_len)

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
        if len(self.x_old) > self.tab_len:  # zobrazeni max 10 minulych prvku
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
