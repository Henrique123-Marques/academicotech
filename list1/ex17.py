class Ex17(object):
    """Criar um programa apresente a conversão de dólar para reais. """
    def __init__(self):
        super(Ex17, self).__init__()
        self.dolar = float(input('Digite o valor em dolares: '))

    def Conversor_Real(self):
        self.real = (self.dolar/4.3)
        return self.real

obj17 = Ex17()
valor_real = obj17.Conversor_Real()
print(f'O valor em dolar digitado equivale a {valor_real} reais') 
        