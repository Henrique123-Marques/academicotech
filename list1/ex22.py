import random

class Ex22(object):
    """22 : Criar um programa para ler dois valores e efetuar a troca entre eles. Apresente os valores trocados."""
    def __init__(self):
        super(Ex22, self).__init__()
        self.valores = random.sample(range(1, 10),2)

    def TrocaFunc(self):
        self.aux = self.valores[0]
        self.valores[0] = self.valores[1]
        self.valores[1] = self.aux
        return f'Valores sorteados: {self.valores}; Valores trocados: {self.valores[1]}; {self.valores[0]}'

obj22 = Ex22()
trocas = obj22.TrocaFunc()
print(f'{trocas}')
