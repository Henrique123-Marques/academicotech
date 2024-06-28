class Ex2(object):
	"""Ex 2: Soma de 0 a 100"""
	def __init__(self, n):
		self.n = n

	def Soma0a100(self, n):
		n = list(range(101))
		return sum(n)

obj2 = Ex2(0)
soma_seq = obj2.Soma0a100(0)
print(f'Soma da sequencia de 0 a 100: {soma_seq}')