#-*-coding:utf8;-*-
#qpy:2
#qpy:console


class Pessoa(object):
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def Identidade(self):
        return self.nome,\
        self.idade,\
        self.sexo
 
p = Pessoa("joao",21,"m")

print (p.Identidade())     