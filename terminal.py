#qpy:2
#qpy:console

import os
while True:
    texto = input("$joao@linux> ")
    if 'cd' in texto:
        os.chdir(texto[3:])
        os.system(texto)
        texto = input("$joao@linux> "+texto[3:])
    else:
        os.system(texto)