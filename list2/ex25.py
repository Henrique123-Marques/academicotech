class Ex25(object):
	"""Ex25 Faça um Programa que pergunte em que turno você estuda. 
	Peça para digitar M-matutino ou V - Vespertino ou N - Noturno. 
	Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""
	def __init__(self, turno):
		self.turno = turno

	def func_Turno(self, turno):
		turno = str(input('Digite o turno que você estuda: M-matutino, V-Vesperetino ou N-Noturno: '))
		if turno == 'M' or turno == 'm':
			return 'Bom dia'
		elif turno == 'V' or turno == 'v':
			return 'Boa Tarde'
		elif turno == 'N' or turno == 'n':
			return 'Boa noite'

obj25 = Ex25('')
saudacao = obj25.func_Turno('')
print(f'{saudacao}')
		