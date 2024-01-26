import math

class ex14(object):
    """14 : Criar um programa que leia 3 valores e apresente a soma dos seus quadrados."""
    def __init__(self):
        super(ex14, self).__init__()
        self.v1 = float(input('Insira o primeiro valor: '))
        self.v2 = float(input('Insira o segundo valor: '))
        self.v3 = float(input('Insira o terceiro valor: '))

    def quadrado(self):
        self.v1 = self.v1**2
        self.v2 = self.v2**2
        self.v3 = self.v3**2
        self.quad = (self.v1 + self.v2 + self.v3)
        return self.quad

obj14 = ex14()
NumerosQuadrados = obj14.quadrado()
print(f'Os valores digitados ao quadrado somados é: {NumerosQuadrados}')