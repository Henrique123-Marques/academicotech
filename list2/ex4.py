import math

class Ex4(object):
    """04- Criar um programa que leia 10 valores e apresente o maior e o menor valor."""
    def __init__(self):
        super(Ex4, self).__init__()
    
    def MaiorMenor(self):
        lista = list()
        for i in range(10):
            self.arg = float(input('Digite um valor: '))
            lista.append(self.arg)
        return lista

obj4 = Ex4()
maior_menor = obj4.MaiorMenor()
print(f'Maior valor: {max(maior_menor)}; Menor valor: {min(maior_menor)}')

        