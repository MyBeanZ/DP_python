from PyQt5 import QtCore, QtWidgets

class Preferences_win(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # self.resize(900, 880)
        self.setGeometry(380, 210, 300, 300)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("PSD - preferences")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        """-----others -----------"""
        self.centralwidget.setFocus()  # pohled na central widget - Qapp velka plocha
        self.setCentralWidget(self.centralwidget)
        self.statusBar().showMessage("Welcome", 3000)

    def fileQuit(self):
        self.s.close()
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()



if __name__ == '__main__':
    test_cl = Preferences_win()
    test_cl.show() # test_cl.hide()