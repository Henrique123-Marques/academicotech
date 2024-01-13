class Ex3():
	"""03 : Criar um programa para ler um valor e apresentar seu quadrado."""
	def __init__(self):
		self.n = float(input('Digite um numero para saber seu quadrado: '))

	def quadrado(self):
		self.n *= self.n
		return self.n

obj3 = Ex3()
n = obj3.quadrado()
print(f'O quadrado do numero digitado é: {n}')	