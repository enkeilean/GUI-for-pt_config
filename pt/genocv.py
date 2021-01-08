# -*- coding: utf-8 -*-
import sys
class ocv:
    def __init__(self, fileDir, ocv_lines):
        self.fileDir = fileDir
        self.filePath = fileDir + '/ocv.tcl'
        self.ocv_lines = ocv_lines


    def write_ocv(self):
        with open(self.filePath,'w+') as f:
            f.write(self.ocv_lines)
if __name__ == '__main__':
    a = ocv('/home/wzq/haha','fdkgjskdfgsfgsjkdfghsjkdfgsf')
    a.write_ocv()