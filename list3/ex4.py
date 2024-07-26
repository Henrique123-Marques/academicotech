class Candidato:
	"""docstring for Eleicao"""
	def __init__(self, nome, numero):
		self.nome = nome
		self.numero = numero
		self.votos = 0
		
class Urna:
	""""""
	def __init__(self):
		self.candidatos = [
							Candidato('Pequi', 20), 
							Candidato('Trena', 30),
		 					Candidato('Nanco', 15), 
		 					Candidato('Mumbo', 26),
		 					Candidato('Bonco', 37)
		 				]
		self.votos_brancos = 0
		self.votos_nulos = 0
		self.votos_total = 0

	def registrar_voto(self, numero):
		if numero == -1:
			return False
		self.votos_total += 1

		if numero == 0:
			self.votos_brancos += 1
		else:
			for candidato in self.candidatos:
				if candidato.numero == numero:
					candidato.votos += 1
					return True
			self.votos_nulos += 1
		return True

	def calc_perc(self):
		percentuais = {}
		for candidato in self.candidatos:
			percentuais[candidato.nome] = (candidato.votos / self.votos_total) * 100
		
		percentuais["Brancos"] = (self.votos_brancos/ self.votos_total) * 100
		percentuais["Nulos"] = (self.votos_nulos / self.votos_total) * 100
		return percentuais

class Eleicao:
	"""docstring for Eleicao"""
	def __init__(self):
		self.urna = Urna()

	def iniciar(self):
		print('Digite o nº do candidato (ou 0 para Branco, -1 para encerrar): ')
		while True:
			try:
				voto = int(input())
				if not self.urna.registrar_voto(voto):
					break
			except ValueError:
				print('Entrada invalida. Digite um nº')

		percentuais = self.urna.calc_perc()
		for nome, percentual in percentuais.items():
			print(f'{nome}: {percentual:.2f}%')

#Para iniciar a eleicao
eleicao = Eleicao()
eleicao.iniciar()	