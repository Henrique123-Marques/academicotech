print("15. Escreva um programa que leia dois números e determine o maior múltiplo comum (MMC) entre eles.")

import math

class Ex15(object):
	"""docstring for Ex15"""
	def __init__(self):
		super(Ex15, self).__init__()
		self.n1 = int(input('Digite o primeiro numero: ')) 
		self.n2 = int(input('Digite o segundo numero: '))

	def MaiorMMC(self): #Corrigir condicionais
		mdc = math.gcd(self.n1, self.n2)
		mmc = abs(self.n1 * self.n2)
		return f'O MMC de {self.n1} e {self.n2} é {mmc}'

obj15 = Ex15()
print(f'{obj15.MaiorMMC()}')