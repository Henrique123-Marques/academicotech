class Ex28(object):
	"""28- Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
·         • "Telefonou para a vítima?"
·         • "Esteve no local do crime?"
·         • "Mora perto da vítima?"
·         • "Devia para a vítima?"
·         • "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
 entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".."""
	def __init__(self):
		self.lista = []

	def Pesquisa(self):
		arg1 = input('Telefonou para a vítima? 1 para Sim, 0 para Não: ')
		if arg1 == '1':
			self.lista.append(arg1)
		else:
			pass

		arg2 = input('Esteve no local do crime? 1 para Sim, 0 para Não: ')
		if arg2 == '1':
			self.lista.append(arg2)
		else:
			pass

		arg3 = input('Mora perto da vítima? 1 para Sim, 0 para Não: ')
		if arg3 == '1':
			self.lista.append(arg3)
		else:
			pass

		arg4 = input('Devia para a vítima? 1 para Sim, 0 para Não: ')
		if arg4 == '1':
			self.lista.append(arg4)
		else:
			pass

		arg5 = input('Já trabalhou com a vítima? 1 para Sim, 0 para Não:')
		if arg5 == '1':
			self.lista.append(arg5)
		else:
			pass
		
		if len(self.lista) == 2:
			return 'Suspeita'
		elif len(self.lista) == 3 or len(self.lista) == 4:
			return 'Cumplice'
		elif len(self.lista) == 5:
			return 'Assasino'
		else:
			return 'Inocente'


obj28 = Ex28()
analise = obj28.Pesquisa()
print(f'Tamanho da lista de respostas positivas: {analise}') 
