class Ex11GPT(object):
	"""1. Escreva um programa que solicite um número ao usuário e informe se ele é positivo, negativo ou zero.
"""
	def __init__(self):
		self.numero = float(input('Digite um numero: '))
		
	def PositivoNegativofunc(self):
		if self.numero > 0:
			return 'Positivo'
		else:
			return 'Negativo'

obj11 = Ex11GPT()
print(f'O número é {obj11.PositivoNegativofunc()}')
		