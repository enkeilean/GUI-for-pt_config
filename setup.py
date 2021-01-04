# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import setup_config
import gensetup

class demo(setup_config.Ui_Dialog):
    def __init__(self, Dialog):
        self.lib_path = ''
        super().setupUi(Dialog)
        self.initUI()
        self.corner = {}
        self.proj_path = ''


    def initUI(self):
        self.proj_btn.clicked.connect(self.bindbtn)
        self.lib_dir_btn.clicked.connect(self.bindlist)
       # self.lib_dir_line..connect(self.rm_lib_path)
        self.all.stateChanged.connect(self.set_allcorner)
        self.wcl.stateChanged.connect(self.set_wcl_corner)
        self.wc.stateChanged.connect(self.set_wc_corner)
        self.lt.stateChanged.connect(self.set_lt_corner)
        self.ml.stateChanged.connect(self.set_ml_corner)
        self.tt.stateChanged.connect(self.set_tt_corner)
        self.tt125c.stateChanged.connect(self.set_tt125c_corner)
        self.ok_btn.clicked.connect(self.creat_input)


    def bindlist(self):
        """ Select the path of lib """
        dir = QFileDialog.getExistingDirectory(
            None, "Select the  path of lib", "/etc")
        self.lib_dir_line.setText(dir)
        self.lib_path = dir

    def bindbtn(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.AnyFile)
        file_dir = dir.getExistingDirectory(
            None, "Select the path of lib", "/etc")
        self.proj_lineEdit.setText(file_dir)
        self.proj_path = file_dir
    def rm_lib_path(self, item, *haha):
        """ rm the path of lib that unwant """
        print(self.lib_path)
        select = QMessageBox.information(
            None,
            'Message',
            'Are you sure you want to delete the path or file',
            QMessageBox.Yes | QMessageBox.No)
        if select == QMessageBox.Yes:
            self.lib_path = ''
            self.lib_dir_line.clear()
        print(self.lib_path)

    def set_allcorner(self):
        '''set the corner that run'''
        if self.all.isChecked():
            self.wcl.setChecked(True)
            self.wc.setChecked(True)
            self.lt.setChecked(True)
            self.ml.setChecked(True)
            self.tt.setChecked(True)
            self.tt125c.setChecked(True)
            corner = {'wcl': 'MAXLT', 'wc': 'MAX', 'lt': 'MIN', 'ml': 'MINHT', 'tt': 'TYP','tt125c':'tt125c'}
            self.corner.update(corner)

            print(self.corner)
        else:
            self.wcl.setChecked(False)
            self.wc.setChecked(False)
            self.lt.setChecked(False)
            self.ml.setChecked(False)
            self.tt.setChecked(False)
            self.tt125c.setChecked(False)

            self.corner.clear()
            print(self.corner)

    def set_wcl_corner(self):     # To be optimized
        '''set the corner that run'''
        try:
            if self.wcl.isChecked():
                wcl = {'wcl': 'MAXLT'}
                self.corner.update(wcl)
                print(self.corner)
            else:
                self.corner.pop('wcl')
                print(self.corner)
        except KeyError:
            pass

    def set_wc_corner(self):  # To be optimized

        try:
            if self.wc.isChecked():
                wc = {'wc': 'MAX'}
                self.corner.update(wc)
                print(self.corner)
            else:
                self.corner.pop('wc')
                print(self.corner)
        except KeyError:
            pass

    def set_ml_corner(self):  # To be optimized

        try:
            if self.ml.isChecked():
                ml = {'ml': 'MINHT'}
                self.corner.update(ml)
                print(self.corner)
            else:
                self.corner.pop('ml')
                print(self.corner)
        except KeyError:
            pass

    def set_lt_corner(self):  # To be optimized

        try:
            if self.lt.isChecked():
                lt = {'lt': 'MIN'}
                self.corner.update(lt)
                print(self.corner)
            else:
                self.corner.pop('lt')
                print(self.corner)
        except KeyError:
            pass

    def set_tt_corner(self):  # To be optimized

        try:
            if self.tt.isChecked():
                tt = {'tt': 'TYP'}
                self.corner.update(tt)
                print(self.corner)
            else:
                self.corner.pop('tt')
                print(self.corner)
        except KeyError:
            pass

    def set_tt125c_corner(self):  # To be optimized

        try:
            if self.tt125c.isChecked():
                tt125c = {'tt125c':'tt125c'}
                self.corner.update(tt125c)
                print(self.corner)
            else:
                self.corner.pop('tt125c')
                print(self.corner)
        except KeyError:
            pass

    def creat_input(self):
        #print(self.proj_path +'\n' + self.lib_path + '\n' + self.corner)
        # lib_path = "/disk/proj2/glista/current/lib/"  # It is a list of lib, please input you lib absolute path
        # corner = {'wcl': 'MAXLT', 'wc': 'MAX', 'lt': 'MIN', 'ml': 'MINHT', 'tt': 'TYP'}  # please input you need corner
        # proj_path = "/home/wzq"  # please input you setup.tcl absolute path
        # print(type(self.proj_path))
        # print(type(self.corner))
        # print(type(self.lib_path))
        setup_file = gensetup.setup(self.proj_path, self.lib_path, self.corner)
        setup_file.run_setup()
        # QCoreApplication.instance().quit()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = demo(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
