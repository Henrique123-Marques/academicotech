class Ex19(object):
    """19 : Criar um programa ler um valor e apresente o dobro o triplo e o quádruplo."""
    def __init__(self):
        super(Ex19, self).__init__()
        self.valor = float(input('Digite um valor: '))

    def Dobro(self):
        self.dobro = self.valor ** 2
        return self.dobro

    def Triplo(self):
        self.triplo = self.valor ** 3
        return self.triplo

    def Quadruplo(self):
        self.quadruplo = self.valor ** 4
        return self.quadruplo


obj19 = Ex19()
valor_dobro = obj19.Dobro()
valor_triplo = obj19.Triplo()
valor_quadruplo = obj19.Quadruplo()

print(f'Seu dobro: {valor_dobro}; Seu triplo: {valor_triplo}; Seu quadruplo: {valor_quadruplo}') 
        