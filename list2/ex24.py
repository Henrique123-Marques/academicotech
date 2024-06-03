class Ex24(object):
	"""Ex24 Criar um programa que leia 5 valores e apresente a soma dos dois maiores valores."""
	def __init__(self):
		self.list = []

	def Ler_Valores(self):
		for i in range(5):
			n1 = float(input('Digite um valor: '))
			self.list.append(n1)

	def Soma_Maiores(self):
		if len(self.list) < 2:
			return None

		valores_ordenados = sorted(self.list, reverse=True)
		return valores_ordenados[0] + valores_ordenados[1]


obj24 = Ex24()
obj24.Ler_Valores()
soma_dois_maiores = obj24.Soma_Maiores()
print(f'Soma dos dois maiores valores: {soma_dois_maiores}')
		