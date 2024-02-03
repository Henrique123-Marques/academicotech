import math, random

class Ex10(object):
    """10- Criar um programa que leia 5 valores e efetue a troca entre eles."""
    def __init__(self):
        super(Ex10, self).__init__()

    def Trocas(self):
        lista = list()
        for i in range(5):
            self.arg1 = float(input('Digite o primeiro valor: '))
            lista.append(self.arg1)

        return lista

obj9 = Ex10()
trocados = obj9.Trocas()
print(trocados)

        