# -*- coding: utf-8 -*-
import setup
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import gensetup


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = setup.demo(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



