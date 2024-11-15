print('18. Escreva um programa que leia a idade de uma pessoa e informe se ela é maior de idade (18 anos ou mais).')

class Ex18(object):
	"""docstring for Ex18"""
	def __init__(self):
		super(Ex18, self).__init__()
		self.idade = int(input('Digite a sua idade: '))

	def FuncIdade(self):
		if self.idade < 18:
			return False
		elif self.idade >= 18:
			return True

obj18 = Ex18()
print(f'Você é maior de idade? Resposta: {obj18.FuncIdade()}')
		