#-*-coding:utf8;-*-
#qpy:2
#qpy:console

lista = [x for x in range(1,101) if x % 2 == 0]
a = filter(lambda x: x % 3==0, lista)
print (a)