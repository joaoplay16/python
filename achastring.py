#qpy:2
#qpy:console

import os
extsd = ('/mnt/extSdCard/')
e = ".txt"
on = True
while on:
    lista = os.listdir(extsd)
    for item in lista:
        if item.endswith(e):
           arq = open(extsd+item)
           print (item.upper()+':\n',arq.read()+'\n')
        elif not '.' in item:
           extsd= os.getcwd()+item   
            
        