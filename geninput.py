# -*- coding: utf-8 -*-
import os

class input:
    def __init__(self, proj_path, arg_dict, sdc_arg):
        self.arg_dict = arg_dict
       # self.verilog_path = verilog_path
       #  self.sdc_path = sdc_path
        self.proj_path = proj_path
        self.sdc_arg = sdc_arg
        self.arg = ['DESIGN','generate_ice','generate_redhawk','verilog_file','spefDir','sdcDir']
        self.flag = 1

    def spef(self):              #return -->str
        '''get spef lines'''

        with open('./spef.init','r') as f:
            lines = f.read()
            # print(lines)
            return lines
        
    def sdc(self):          #return -->str
        ''' set sdc lines '''
        for i in self.sdc_arg:
            if self.flag == 1:
                lines = 'if {[regexp func $mode]} {\nset sdc_file $func_sdcDir/FunDft_flattensdc.tcl\n'
                self.flag = 0
            else:
                lines = lines + '} elseif {[regexp %s $mode]} {\n    set sdc_file %s\n'%(i,self.sdc_arg[i])
            #    lines = lines + '} elseif {[regexp %s $mode]} {\n    set sdc_file $func_sdcDir%s\n'%(i,self.sdc_arg[i])

        return lines + '\n' + '}'

    def write_input(self):
        setup_path = self.proj_path + '/input.tcl'
        with open(setup_path,'w') as f:
            print(type(self.arg[0]))
            print(type(self.arg_dict[self.arg[0]]))
            f.write('set ' + self.arg[0] + ' ' + str(self.arg_dict[self.arg[0]]) + '\n'*3)
            f.write('set ' + self.arg[1] + ' ' + str(self.arg_dict[self.arg[1]]) + '\n')
            f.write('set ' + self.arg[2] + ' ' + str(self.arg_dict[self.arg[2]]) + '\n'*3)
            f.write('set ' + self.arg[3] + ' ' + str(self.arg_dict[self.arg[3]]) + '\n'*3)
            f.write('set ' + self.arg[4] + ' ' + str(self.arg_dict[self.arg[4]]) + '\n')
            f.write(self.spef() + '\n'*3)
            f.write('set ' + self.arg[5] + ' ' + str(self.arg_dict[self.arg[5]]) + '\n')
            f.write(self.sdc())

            
if __name__ == '__main__':
    gg = 2
    bb =3
    haha = {'DESIGN':1,'generate_ice':2,'generate_redhawk':3,'verilog_file':4,'spefDir':5,'sdcDir':6}
    hehe = {'a':1,'b':2,'c':3}
    a = input(proj_path = '/home/wzq/haha', arg_dict = haha,sdc_arg=hehe)
    a.write_input()
