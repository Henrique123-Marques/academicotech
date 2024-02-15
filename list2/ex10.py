import math, random

class Ex10(object):
    """10- Criar um programa que leia 5 valores e efetue a troca entre eles."""
    def __init__(self, lista):
        super(Ex10, self).__init__()
        self.lista = lista
    
    def Trocas(self, lista):
        lista = [1,2,3,4,5]
        lista[0], lista[1] = lista[1], lista[0]
        
        return lista

obj9 = Ex10([])
trocados = obj9.Trocas([])
print(trocados)

        