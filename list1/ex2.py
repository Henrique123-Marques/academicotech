'''Exercício 02 : Criar um programa que apresente a tabuada do valor digitado pelo usuário. '''
class Ex2():
	def __init__(self):
		self.tabuada = float(input('Digite um valor para saber sua tabuada: '))

	def resultado2(self):
		for i in range(1, 11):
			print(f'Resultado EX2: {self.tabuada} x {i} = {self.tabuada * i}')

obj2 = Ex2()
obj2.resultado2()