class Ex6(object):
    """06- Criar um programa que leia um valor e informe se o mesmo está fora ou dentro da faixa de 10 a 50."""
    def __init__(self):
        super(Ex6, self).__init__()
        self.arg = float(input('Digite um valor: '))

    def Faixa(self):
        if self.arg >= 10 and self.arg <= 50:
            return True
        else:
            return False

obj6 = Ex6()
faixa_valor = obj6.Faixa()
print(faixa_valor)
        