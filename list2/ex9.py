class Ex9(object):
    """09- Criar um programa que calcule a quantidade de litros gastos de combustível em 
    uma viagem com um automóvel que faz 15 km por litro. 
    Fórmulas :: Distancia = Tempo * Velocidade e Litrosgastos = distancia/15"""
    def __init__(self):
        super(Ex9, self).__init__()
        self.tempo = float(input('Insira o tempo em horas da viagem: '))
        self.vel = float(input('Insira a velocidade do veiculo: '))

    def Distancia(self):
        self.distancia = self.tempo * self.vel
        return self.distancia

    def Litros(self):
        self.litros = self.distancia/15
        return self.litros

obj9 = Ex9()
distancia_var = obj9.Distancia()
litros = obj9.Litros()

print(f'A distancia da viagem foi de: {distancia_var}km.\n A quantidade de litros gastos foi de: {litros} Litros')