class Ex15(object):
    """15 : Criar um programa que leia 3 valores e apresente o quadrado de sua soma."""
    def __init__(self):
        super(Ex15, self).__init__()
        self.arg1 = float(input('Digite o primeiro numero: '))
        self.arg2 = float(input('Digite o segundo numero: '))
        self.arg3 = float(input('Digite o terceiro numero: '))

    def QuadradoSoma(self):
        self.quad_soma = (self.arg1 + self.arg2 + self.arg3)**2
        return self.quad_soma

obj15 = Ex15()
quadrado_soma = obj15.QuadradoSoma()
print(f'O quadrado da soma é: {quadrado_soma}')