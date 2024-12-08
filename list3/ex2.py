class Ex2(object):
	"""Ex2- Efetue a soma da sequencia de 0 a 100"""
	def __init__(self, soma):
		super(Ex2, self).__init__()
		self.soma = soma

	def SomaSeq(self, soma):
		self.soma = 0
		for i in range(1, 101):
			soma += i
		return soma

obj2 = Ex2(0)
print(f'{obj2.SomaSeq(0)}')
