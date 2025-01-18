class Ex7(object):
	"""Ex7 Criar um programa que apresente todos os numeros impares na faixa de 0 a 500 - CORRIGA"""
	def __init__(self, arg):
		super(Ex7, self).__init__()
		self.arg = []

	def Impares(self, arg):
		for i in range(1, 501):
			if i % 2 == 0:
				break
			else:
				self.arg.append(i)
		return self.arg

objeto7 = Ex7(0)
print(f'Numeros impares de 0 a 500: {objeto7.Impares(0)}')
		