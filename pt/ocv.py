# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import ocv_config
import genocv
class ocv(ocv_config.Ui_Dialog):
    def __init__(self,Dialog):
        super().setupUi(Dialog)
        self.fileDir = ''
        self.ocvlines = ''
        self.initUI()

    def initUI(self):
        with open('./ocv.init','r') as f:
            self.plainTextEdit.setPlainText(f.read())
        self.plainTextEdit.textChanged.connect(self.get_ocvlines)
        self.font_btn.clicked.connect(self.set_font)
        self.fileDir_btn.clicked.connect(self.set_fileDir)
        self.ok_btn.clicked.connect(self.write_ocv)

    def get_ocvlines(self):
        self.ocvlines = self.plainTextEdit.toPlainText()
        print(self.ocvlines)

    def set_fileDir(self):
        dir =QFileDialog.getExistingDirectory(None, 'Please select you file Dir', '/disk')
        self.fileDir_lineEdit.setText(dir)
        self.fileDir = dir

    def set_font(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.plainTextEdit.setFont(font)

    def write_ocv(self):
        if self.ocvlines == '':
            self.ocvlines = self.plainTextEdit.toPlainText()
        ocvFile = genocv.ocv(self.fileDir, self.ocvlines)
        ocvFile.write_ocv()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = ocv(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())