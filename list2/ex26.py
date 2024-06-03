class Ex26(object):
	"""Ex 26: Faça um Programa que leia um número e exiba o dia correspondente da semana. 
	(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""
	def __init__(self, dia):
		self.dia = dia

	def func_Semana(self, dia):
		dia = float(input('Digite um numero: '))
		if dia == 1:
			return 'Domingo'
		elif dia == 2:
			return 'Segunda'
		elif dia == 3:
			return 'Terça'
		elif dia == 4:
			return 'Quarta'
		elif dia == 5:
			return 'Quinta'
		elif dia == 6:
			return 'Sexta'
		elif dia == 7:
			return 'Sabado'
		elif dia > 7 or dia < 1:
			return 'Invalido'

obj26 = Ex26(0)
semana_valor = obj26.func_Semana(0)
print(f'{semana_valor}')