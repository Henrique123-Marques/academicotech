#Ex1 Escreva um programa que imprima todos os números pares de 1 a 50.

class Ex1_gpt:
	def __init__(self, arg):
		self.arg = []

	def ParesFunc(self):
		for i in range(1,50):
			if i % 2 == 0:
				self.arg.append(i)
		return self.arg


n_pares = Ex1_gpt([])
print(f'{n_pares.ParesFunc()}')		
		