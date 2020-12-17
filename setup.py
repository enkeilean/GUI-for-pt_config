# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import *
import pt_config



class demo(pt_config.Ui_Dialog):
    def __init__(self, Dialog):
        super().setupUi(Dialog)

        # self.haha = QPushButton('test')
        # self.verticalLayout_4.addWidget(self.haha)
        self.lib_dir_6.clicked.connect(self.bindlist)

    def bindlist(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.DirectoryOnly)
        dir.setDirectory("/home")
        if dir.exec_():
            self.listView.setModel(dir.selectedFiles())
            print(dir.selectedFiles())
            print(type(dir.selectedFiles()))



if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # mainWindow = QDialog()
    # ui = demo(mainWindow)
    # ui.setupUi(mainWindow)
    # mainWindow.show()
    # sys.exit(app.exec_())
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = demo(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())