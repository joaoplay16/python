#-*-coding:utf8;-*-
#qpy:2
#qpy:console

def reverso(s):
    rev =""
    for letra in s:
        rev = letra + rev
    return rev

print reverso("joao")