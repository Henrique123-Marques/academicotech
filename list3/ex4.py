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
	def __init__(self):
		super(Ex4, self).__init__()
		self.candidatos = {
		20: {'nome': 'Pequi', 'votos': 0},
		30: {'nome': 'Trena', 'votos': 0},
		15: {'nome': 'Nanco', 'votos': 0},
		26: {'nome': 'Mumbo', 'votos': 0},
		37: {'nome': 'Bonco', 'votos': 0},
		}
		self.brancos = 0
		self.nulos = 0
		self.total_votos = 0

	def registro_votos(self, voto):
		if voto == 0:
			self.brancos += 1
		elif voto in self.candidatos:
			self.candidatos[voto]['votos'] += 1
		else:
			self.nulos += 1
		self.total_votos += 1

	def percentuais_calc(self):
		percentuais = {}
		for numero, dados in self.candidatos.items():
			percentuais[dados['nome']] = (dados['votos'] / self.total_votos) * 100
		percentuais['Branco'] = (self.brancos / self.total_votos) * 100
		percentuais['Nulos'] = (self.nulos / self.total_votos) * 100
		return percentuais

	def resultados(self):
		print('\nResultados Finais')
		for numero, dados in self.candidatos.items():
			print(f'{dados['nome']}: {dados['votos']} votos')
		print(f' Votos em Branco: {self.brancos}')
		print(f'Votos Nulos: {self.nulos}')

		print('\nPercentuais: ')
		percentuais = self.percentuais_calc()
		for categoria, percentual in percentuais.items():
			print(f'{categoria}: {percentual:.2f}%')

	def iniciar_pesquisa(self):
		print('Digite o numero do candidato (0 para Branco, -1 para encerrar): ')
		while True:
			try:
				voto = int(input('Digite seu voto: '))
				if voto == -1:
					break
				self.registro_votos(voto)
			except ValueError:
				print('Entrada invalida. Por favor, tente novamente')

		self.resultados()

pesquisa = Ex4()
pesquisa.iniciar_pesquisa()	
