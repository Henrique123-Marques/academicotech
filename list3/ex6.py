class Ex6(object):
	"""Ex6: Apresente o resultado da tabuada de qualquer valor: O numero sera a opcao do usuario"""
	def __init__(self, arg):
		super(Ex6, self).__init__()
		self.arg = int(input('Digite um numero: '))

	def Tabuada(self, arg):
		for i in range(1,11):
			print(f'Resultado: {self.arg} x {i} = {self.arg * i}')

obj6 = Ex6(0)
obj6.Tabuada(0)