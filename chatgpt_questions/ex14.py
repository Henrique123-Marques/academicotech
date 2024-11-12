"Escreva um programa que leia uma palavra e exiba quantas letras essa palavra contém."

class Letras(object):
	"""docstring for Letras"""
	def __init__(self):
		super(Letras, self).__init__()
		self.arg = str(input('Digite uma palavra: '))

	def NumeroLetras(self):
		return len(self.arg)

obj14 = Letras()
print(f'O numero de letras que essa palavra tem são: {obj14.NumeroLetras()}')

