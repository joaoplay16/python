#-*-coding:utf8;-*-
#qpy:2
#qpy:console


class Animal(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def fazer_som(self):
        print ("???")

class Mamifero(Animal):
    def fazer_som(self):
        print ("Som de mamíferos")

    def som_de_mamifero(self):
      return super(Mamifero, self).fazer_som()
        

gato = Animal('Gato', 2)
print (gato.nome)
print (gato.idade)
gato.fazer_som()

mam = Mamifero('Man',54)
mam.fazer_som()
mam.som_de_mamifero()
