class Ex11(object):
    """11 Criar um programa que leia dois valores e apresente a diferença do maior pelo menor"""
    def __init__(self, arg1, arg2, diferenca):
        super(Ex11, self).__init__()
        self.arg1 = arg1
        self.arg2 = arg2
        self.diferenca = diferenca

    def Diferenca(self, arg1, arg2, diferenca):
        arg1 = float(input('Valor 1: '))
        arg2 = float(input('Valor 2: '))
        diferenca = arg1 - arg2
        return diferenca

obj11 = Ex11(0, 0, 0)
diferenca_var = obj11.Diferenca(0, 0, 0)
print(f'A diferenca do maior para o menor é: {diferenca_var}')
         
        