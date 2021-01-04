# -*- coding: utf-8 -*-
import os

class input:
    def __init__(self,verilog_path,sdc_path,**other):
        self.other = other
        self.verilog_path = verilog_path
        self.sdc_path = sdc_path
        self.arg = ['DESIGN','generate_ice','generate_redhawk','verilog_file','spefDir','sdcDir']


    def spef(self):

        with open('./spef.init','r') as f:
            lines = f.readlines()
            print(lines)

            return lines


a = input(1,2)
a.spef()