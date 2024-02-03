import math

class Ex7(object):
    """docstring for Ex7"""
    def __init__(self):
        super(Ex7, self).__init__()
        self.arg = float(input('Digite um valor: '))

    def ValoresAcima(self):
        self.arg_cima1 = self.arg + 1
        self.arg_cima2 = self.arg + 2
        self.arg_cima3 = self.arg + 3

        return f'Os 3 Valores acima são: {self.arg_cima1}; {self.arg_cima2}; {self.arg_cima3}'

    def ValoresBaixo(self):
        self.arg_baixo1 = self.arg - 1
        self.arg_baixo2 = self.arg - 2
        self.arg_baixo3 = self.arg - 3
        self.arg_baixo4 = self.arg - 4
        self.arg_baixo5 = self.arg - 5

        return f'Os 5 Valores abaixo são: {self.arg_baixo1}; {self.arg_baixo2}; {self.arg_baixo3}; {self.arg_baixo4}; {self.arg_baixo5}'

obj7 = Ex7()
valores_cima = obj7.ValoresAcima()
valores_baixo = obj7.ValoresBaixo()
print(f'{valores_cima}\n {valores_baixo}') 


        