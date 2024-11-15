print('19. Escreva um programa que leia uma lista de nomes e exiba os nomes em ordem alfabética.')

class Ex19(object):
	"""docstring for Ex19"""
	def __init__(self):
		super(Ex19, self).__init__()
		self.listanomes = []

	def Alfabetica(self):
		for i in range(1,5):
			nome = str(input('Digite um nome: '))
			self.listanomes.append(nome)
		return sorted(self.listanomes)

obj19 = Ex19()
print(f'Lista de nomes em ordem Alfabetica: {obj19.Alfabetica()}')
		