class Ex16(object):
    """Criar um programa que apresente a conversão de reais em dólar. - Cotacao jan/2024"""
    def __init__(self):
        super(Ex16, self).__init__()
        self.real = float(input('Insira o valor em reais pra conversão: '))

    def Conversor_Dolar(self):
        self.conversor = (self.real*4.30)
        return self.conversor

obj16 = Ex16()
dolar = obj16.Conversor_Dolar() 
print(f'O valor em real digitado equivale a {dolar} dolares')
        