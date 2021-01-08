# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import input_configx2
import geninput
import os


class input(input_configx2.Ui_Dialog):
    def __init__(self, Dialog):
        super().setupUi(Dialog)
        self.sdc_files = []
        self.mode = []
        self.projDir = ''
        self.verilogPath = ''
        self.spefDir = ''
        self.designeName = ''
        self.dict_arg = {}
        self.sdcArg = {}
        self.sdcDir = ''
        self.ice = 2
        self.redhawk = 2
        self.initUI()
        self.flag = 0

    def initUI(self):
        self.proj_btn.clicked.connect(self.get_projDir)
        self.verilog_btn.clicked.connect(self.get_verilogPath)
        self.spef_btn.clicked.connect(self.get_spefDir)
        #self.designeName_lineEdit..connect(self.get_designeName)
        self.ice_spinBox.setValue(2)
        self.redhawk_spinBox.setValue(2)
        self.ice_spinBox.valueChanged.connect(self.get_ice)
        self.redhawk_spinBox.valueChanged.connect(self.get_redhawk)
        self.sdc_tableWidget.setRowCount(20)
        self.mode_tableWidget.setRowCount(20)
        self.sdc_tableWidget.setColumnCount(1)
        self.mode_tableWidget.setColumnCount(1)
        self.sdc_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mode_tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked)
        self.sdc_tableWidget.setHorizontalHeaderLabels(['sdc_file'])
        self.mode_tableWidget.setHorizontalHeaderLabels(['mode'])
        self.mode_tableWidget.setMaximumSize(100, 1000)
        # self.sdc_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # self.sdc_tableWidget.itemClicked()
        self.sdc_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mode_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sdc_btn.clicked.connect(self.get_sdc)
        self.mode_tableWidget.cellChanged.connect(self.get_mode)
        self.ok_btn.clicked.connect(self.create_input)
        self.cancel_btn.clicked.connect(self.exit)
    def get_projDir(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.ExistingFiles)
        self.projDir = dir.getExistingDirectory(
            None, "Select the path of lib", "/disk")
        self.proj_lineEdit.setText(self.projDir)

    def get_verilogPath(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.ExistingFile)
        dir.setDirectory('/disk')
        if dir.exec_():
            self.verilogPath = dir.selectedFiles()[0]
            self.verilog_lineEdit.setText(self.verilogPath)

    def get_spefDir(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.ExistingFiles)
        self.spefDir = dir.getExistingDirectory(
            None, "Select the path of lib", "/disk")
        self.spef_lineEdit.setText(self.spefDir)

    def get_ice(self):
        self.ice = self.ice_spinBox.value()

    def get_redhawk(self):
        self.redhawk = self.redhawk_spinBox.value()

    def get_designeName(self):
        self.designeName = self.designeName_lineEdit.text()
        print(self.designeName)

    def get_sdc(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.ExistingFiles)
        # dir.setDirectory('/disk')
        self.sdcDir = dir.getExistingDirectory(
            None, "Select the path of lib", "/disk")
        self.sdc_lineEdit.setText(self.sdcDir)
        for root, dirs, files in os.walk(self.sdcDir):
            for i in files:
                if 'sdc' in i:
                    i = root + '/' + i
                    if i not in self.sdc_files and i != '':
                        print(i)
                        self.sdc_files.append(i)
        print(self.sdc_files)
        for i in self.sdc_files:
            row = len(self.sdc_files)
            self.sdc_tableWidget.setRowCount(row)
            item = QTableWidgetItem(i)
            self.sdc_tableWidget.setItem(self.sdc_files.index(i), 0, item)

        # print(len(self.sdc_files))
        # print(self.sdc_files)

        # self.sdc_tableWidget.resizeColumnsToContents()
        # self.sdc_tableWidget.resizeRowsToContents()

    def get_mode(self):
        self.flag += 1
        row = len(self.sdc_files)
        self.mode_tableWidget.setRowCount(row)
        try:
            for i in range(len(self.sdc_files)):
                if self.mode_tableWidget.item(i, 0).text() not in self.mode:
                    self.mode.append(self.mode_tableWidget.item(i, 0).text())
        except BaseException:
            pass

    def create_input(self):
        self.designeName = self.designeName_lineEdit.text()
        if self.projDir == '' or self.spefDir == '' or self.mode == '' or self.sdc_files == '':
            print(self.projDir)
            print(self.spefDir)
            print(self.mode)
            print(self.sdc_files)
            print(self.designeName)
            QMessageBox.information(
                None, 'Tips', 'Please set all  args!', QMessageBox.Ok)
        elif len(self.mode) != len(self.sdc_files):
            print(self.mode)
            print(self.sdc_files)
            QMessageBox.information(
                None,
                'Tips',
                'Please input SDC corresponding mode!',
                QMessageBox.Ok)
        elif self.ice == 2 or self.redhawk == 2:
            QMessageBox.information(
                None,
                'Tips',
                'Please set generate_ice or generate_redhawk value!',
                QMessageBox.Ok)
        else:
            self.dict_arg['DESIGN'] = self.designeName
            self.dict_arg['generate_ice'] = self.ice
            self.dict_arg['generate_redhawk'] = self.redhawk
            self.dict_arg['verilog_file'] = self.verilogPath
            self.dict_arg['spefDir'] = self.spefDir
            self.dict_arg['sdcDir'] = self.sdcDir
            self.sdcArg = dict(zip(self.mode,self.sdc_files))
            self.sdc_arg = dict(zip(self.mode,self.sdc_files))
            input = geninput.input(proj_path = self.projDir, arg_dict = self.dict_arg,sdc_arg=self.sdc_arg)
            input.create_input()
            QCoreApplication.instance().quit()

    def exit(self):
        select = QMessageBox.information(
            None, 'Tips', 'Are you sure exit?!', QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if select == QMessageBox.Yes:
            QCoreApplication.instance().quit()

    # def rn_sdc_file(self, item, *haha):
    #     """ rm the path of lib that unwant """
    #     print(self.lib_path)
    #     select = QMessageBox.information(
    #         None,
    #         'Message',
    #         'Are you sure you want to rename the sdc file',
    #         QMessageBox.Yes | QMessageBox.No)
    #     if select == QMessageBox.Yes:
    #         self.lib_path = ''
    #         self.lib_dir_line.clear()
    #     print(self.lib_path)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = input(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
