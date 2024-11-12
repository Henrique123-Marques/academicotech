print('13. Escreva um programa que leia uma lista de números inteiros e retorne o maior número da lista.')

class Ex13MaxList(object):
	"""docstring for Ex13MaxList"""
	def __init__(self):
		super(Ex13MaxList, self).__init__()
		self.lista = []


	def MaximoLista(self):
		for i in range(1,11):
			n = int(input('Digite um numero para a lista: '))
			self.lista.append(n)
		return max(self.lista)

obj13 = Ex13MaxList()
print(f'Lista: {obj13.MaximoLista()}')