class Ex5(object):
	"""Ex5: Criar um programa que efetue a soma dos numeros pares de 0 a 100"""
	def __init__(self, arg):
		super(Ex5, self).__init__()
		self.arg = arg

	def ParesSeq(self, arg):
		self.arg = 0
		for i in range(1,101):
			if i % 2 == 0:
				arg += i
		return arg

obj5 = Ex5(0)
print(f'{obj5.ParesSeq(0)}')
		