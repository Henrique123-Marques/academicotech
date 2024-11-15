print(f'17. Escreva um programa que leia uma lista de números e exiba o menor e o maior valor dessa lista.')

class Ex17(object):
	def __init__(self):
		self.lista1 = []

	def MaiorMenorLista(self):
		for i in range(1,11):
			n = float(input('Digite um numero: '))
			self.lista1.append(n)
		return max(self.lista1)

	def MaiorMenorLista2(self):
		return min(self.lista1)

obj17 = Ex17()
print(f'O maior valor da lista é {obj17.MaiorMenorLista()} e menor é: {obj17.MaiorMenorLista2()}')
