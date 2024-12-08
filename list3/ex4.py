class Ex4(object):
	"""Ex4 - Capture os resultados validos para uma pesquisa com o objetivo de
	conhecer o primeiro colocado nas pesquisas eleitorais. Sendo que o programa
	nao reconhece o numero exato de pessoas. O programa deve computar ate a entrada
	do valoe -1 (condicao de parada) Sendo:
	Nome do candidato /nº
	Pequi / 20
	Trena / 30
	Nanco / 15
	Mumbo / 26
	Bonco / 37

	O programa deve apresentar o percentual de cada candidato, brancos e nulos
	Considerar um numero diferente do numero dos candidatos como NULO
	Dispor de um registro para o voto em BRANCO"""
	def __init__(self, arg):
		super(Ex4, self).__init__()
		self.arg = arg
		