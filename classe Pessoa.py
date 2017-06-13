#-*-coding:utf8;-*-
#qpy:2
#qpy:console


class Pessoa (object):
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def Identidade(self):
        print ('%s ,%s' % self.nome,self.idade)
 
p = Pessoa("joao",21,"m")

p.Identidade()      