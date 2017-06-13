#qpy:2
#-*-coding:utf8;-*-
#qpy:2
#qpy:console

#ler arquivo
'''
f = open("/mnt/extSdCard/shell/Arquivo.txt",'r', encoding = 'utf-8')
print(f.read())
'''
#escrever no arquivo


on = True
while on:
    texto = input('>_ ')
    leitor = open("/mnt/extSdCard/shell/Arquivo.txt",'r', encoding = 'utf-8')
    escritor = open("/mnt/extSdCard/shell/Arquivo.txt",'a', encoding = 'utf-8')
    
    if texto == 'quit()':
       break
    elif texto == 'ver()':
        
        print(leitor.read())
    else:
        escritor.write(texto + '\n')
    
    