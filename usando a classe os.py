#qpy:2
#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import os

os.chdir ('/mnt/extSdCard/shell/')

files = os.listdir('/mnt/extSdCard/shell/')

for i,item in enumerate (files):
    if '.bak' in item:
        os.remove(item)
        files.remove(item)
        
    print (i+1, files[i])