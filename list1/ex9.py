'''09 : Criar um programa que calcule a quantidade de litros gastos em uma viagem em que o automóvel faz 
12 KM por litro. Sendo as fórmulas. Distância = tempo gasto * valocidade média... 
Litros Gastos = distancia /12.'''

class ex9():
	def __init__(self):
		self.tempo_gasto = float(input('insira o tempo em horas: '))
		self.vel_media = float(input('Insira a valocidade media: '))
	
	def distancia(self):
		self.distancia = self.tempo_gasto * self.vel_media
		return self.distancia

	def Litros_Gastos(self):
		self.litros = (self.distancia)/12
		return self.litros 

obj9 = ex9()
distancia = obj9.distancia()
litros = obj9.Litros_Gastos()

print(f'A Distancia percorrida foi de: {distancia} km e a quantidade de litros gastos na viagem foi: {litros:.2f} litros')