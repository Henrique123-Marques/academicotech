class Ex21(object):
    """21- Faça um programa que leia uma quantidade de tempo em minutos e
     apresente no formato de horas.  Exemplo:: 80 min à 1:20 hs."""
    def __init__(self, minutos):
        super(Ex21, self).__init__()
        self.minutos = minutos

    def ConverterMin_Horas(self, minutos):
        minutos = float(input('Digite o valor em minutos: '))
        minutos = minutos/60
        return minutos

obj21 = Ex21(0)
conversor_min_horas = obj21.ConverterMin_Horas(0)
print(f'O valor em minutos convertido em horas: {conversor_min_horas} horas')

        