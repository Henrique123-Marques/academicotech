class Ex13(object):
    """Ex13 Criar um programa que apresente o mês correspondente de acordo coma 
    entrada do usuário. Exemplo entra 1 e apresenta janeiro."""
    def __init__(self, mes):
        super(Ex13, self).__init__()
        self.mes = mes

    def MesFunc(self, mes):
        mes = float(input('Digite um numero para saber o mes: '))
        if mes == 1:
            return 'Janeiro'
        elif mes == 2:
            return 'Fevereiro'
        elif mes == 3:
            return 'Março'
        elif mes == 4:
            return 'Abril'
        elif mes == 5:
            return 'Maio'
        elif mes == 6:
            return 'Junho'
        elif mes == 7:
            return 'Julho'
        elif mes == 8:
            return 'Agosto'
        elif mes == 9:
            return 'Setembro'
        elif mes == 10:
            return 'Outubro'
        elif mes == 11:
            return 'Novembro'
        elif mes == 12:
            return 'Dezembro'

obj13 = Ex13(0)
Mes_var = obj13.MesFunc(0)
print(Mes_var)
        