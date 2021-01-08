
import os
import re

class setup:
    def __init__(self, projDir, libDir, corner):
       # self.path = libDir
        self.corner = corner
        self.all_file = set()
        self.file_path = set()
        self.lib_dir = set()
        self.lib_name = set()
        self.projDir = projDir
        self.libDir = libDir
        self.flag = 0


    def run_setup(self):
        self.__ergodic()
        self.over_setup()

    def __ergodic(self):
        # try:
        # if os.path.exists(self.projDir):
        #     pass
        # else:
        #     try:
        #         os.mkdir(self.projDir,755)
        #     except :
        #         print('path error')
        #         exit(0)
        for i in self.corner:
            self.getpath(i)
            self.itemize(i)
        # except:
        #     pass

    def getpath(self,key): #--> all_file , --> file_path
        """get all file and all path of file"""
        #for i in self.projDir:
        for root, dirs, files in os.walk(self.libDir,followlinks=False):
            if self.corner[key] in root:
                self.file_path.add(root)
                for i in files:
                    print(i)
                    self.all_file.add(root + '/' + i)

    def itemize(self,path_key): #--> lib_dir
        """ classify paths and files"""
        #path_key = self.corner[path_key]
        for i in self.all_file:
            if re.search(r'.*(%s)\/(.*db)' %self.corner[path_key],i):
                #print(i)
                tmp = re.search(r'(.*(%s))\/(.*db)' %self.corner[path_key],i)
                self.lib_dir.add(tmp.group(1))
                self.lib_name.add(tmp.group(3))
        self.creat_setup(path_key)


    def creat_setup(self,path_key):
        setup_file = self.projDir + '/setup.tcl'
        print(setup_file)
        self.f = open(setup_file, 'a+')
        if self.flag:
            self.f.write('} elseif {[regexp ' + '{} $corner'.format(path_key, self.corner[path_key]) + ']} {'+ '\n' + 'set lib_dir "{}"'.format(" ".join(self.lib_dir)) +'\n' + 'set lib_name "{}"'.format(" ".join(self.lib_name)))
            self.lib_name.clear()
            self.lib_dir.clear()
        else:
            self.flag = 1
            self.f.write('if [regexp {} $corner'.format(path_key, self.corner[path_key]) + ']} {' + '\n' + 'set lib_dir "{}"'.format(" ".join(self.lib_dir)) +'\n' + 'set lib_name "{}"'.format(" ".join(self.lib_name))+ '\n')
            self.lib_name.clear()
            self.lib_dir.clear()

    def over_setup(self):
        self.f.write('\n' + '}\n' + '\n' )
        self.f.write('if {$hier} {' + '\n' + '  foreach subm $subms {\n' + '    lappend lib_name "${subm_lib}/${subm}/${subm}_${mode}_${corner}.setup.prop_lib.db"' + '\n  }\n}\n')
        self.f.write('echo "$lib_dir"\n'+'\n')
        self.f.write('set search_path [concat $lib_dir]\n'+'\n')
        self.f.write('set link_library " * $lib_name "')

if __name__ == '__main__':
    libDir = "/disk/proj2/glista/current/lib/"   #It is a list of lib, please input you lib absolute path
    corner = {'wcl': 'MAXLT', 'wc': 'MAX', 'lt': 'MIN', 'ml': 'MINHT', 'tt': 'TYP'}  # please input you need corner
    projDir = "/home/wzq"  #please input you setup.tcl absolute path
    haha = setup(projDir, libDir, corner)
    haha.run_setup()
