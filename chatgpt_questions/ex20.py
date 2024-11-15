print(f'20. Escreva um programa que leia um número e exiba o quadrado e o cubo desse número.')

class Ex20(object):
	"""docstring for Ex20"""
	def __init__(self):
		super(Ex20, self).__init__()
		self.arg = float(input('Digite um numero: '))

	def Potencias(self):
		quadrado = self.arg**2
		cubo = self.arg**3
		return quadrado, cubo

obj20 = Ex20()
print(f'O quadrado e o cubo do numero digitado são {obj20.Potencias()} ') 		