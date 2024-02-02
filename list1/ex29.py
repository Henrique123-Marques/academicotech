class Ex29(object):
    """29 : Criar um programa que calcule o peso ideal para uma mulher. Fórmula de peso ideal = 62.1 * altura - 44.7"""
    def __init__(self):
        super(Ex29, self).__init__()
        self.altura = float(input('Insira a altura da mulher: '))

    def PesoIdeal(self):
        self.peso_ideal = 62.1 * self.altura - 44.7
        return self.peso_ideal

obj29 = Ex29()
peso = obj29.PesoIdeal()
print(f'O peso ideal de acordo com a altura digitada é: {peso}') 
            