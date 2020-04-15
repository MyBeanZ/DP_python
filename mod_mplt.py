from PyQt5 import QtCore, QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

"""----------------------------- DEFINICE TRID pro vykresleni garfu----------------------------------------------"""
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
        self.s_time_mpl_old = 100
        self.disp_set_plt = 'rel'
        self.val_343 = 3.43

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
        self.val_343 = 1
        self.frame_x = [self.val_343, -self.val_343, -self.val_343, self.val_343, self.val_343]
        self.frame_y = [-self.val_343, -self.val_343, self.val_343, self.val_343, -self.val_343]
        self.frame_x1 = [0, 0]
        self.frame_y1 = [self.val_343, -self.val_343]
        self.frame_y2 = [0, 0]
        self.frame_x2 = [self.val_343, -self.val_343]

    def compute_initial_figure(self):  # inicializace
        pass

    def update_figure(self):
        if len(self.x_old) != self.tab_len:  # Reset pri zmene parametru
            self.x_old = np.zeros(self.tab_len)
            self.y_old = np.zeros(self.tab_len)

        self.x_old = np.append(self.x_old, self.X_data)  # spojeni novych a starych dat
        self.y_old = np.append(self.y_old, self.Y_data)

        if len(self.x_old) > (self.tab_len):  # zobrazeni max "10" minulych prvku
            self.x_old = np.delete(self.x_old, 0)
            self.y_old = np.delete(self.y_old, 0)

        self.axes.cla()
        self.axes.plot(self.frame_x, self.frame_y, color='#8f8483', linestyle='--', linewidth=1)
        self.axes.plot(self.frame_x1, self.frame_y1, color='#8f8483', linestyle='--', linewidth=1)
        self.axes.plot(self.frame_x2, self.frame_y2, color='#8f8483', linestyle='--', linewidth=1)

        self.axes.plot(self.x_old, self.y_old, color='#f2c16d', marker='o', linestyle = ':', label='stare pozice', markersize=2)
        self.axes.plot(self.X_data, self.Y_data, color='r', marker='o', label='aktualni pozice', markersize=2)

        self.draw()


class MplTwo(MyMplCanvas):   # ----------------------- DOLNI GRAFY -------------------------#
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        """------- PROMENNE ----------"""
        self.d_len = 100    # pocet prvku v grafu (Time samples)
        self.x_y_old = np.zeros(self.d_len)
        self.x_y_new = 0
        self.s_time = 100   # perioda vzorkovani (ms)

    def update_figure_two(self):
        if len(self.x_y_old) != self.d_len: # Indikace zmeny delky vzorku v Case - RESET vzorku
            self.x_y_old = np.zeros(self.d_len)

        self.axes.cla()
        x1 = np.linspace(0, self.d_len*self.s_time, self.d_len, endpoint=False)
        self.axes.plot(x1, self.x_y_old, 'r')

        self.draw()

        self.x_y_old = np.append(self.x_y_old, self.x_y_new) # pripoji nakonec
        self.x_y_old = np.delete(self.x_y_old,0)
