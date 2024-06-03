class Ex23(object):
	""""Ex23 Criar um programa que leia um valor e apresente se ele é positivo ou negativo."""
	def __init__(self, arg):
		super(Ex23, self).__init__()
		self.arg = arg

	def Func1(self, arg):
		arg = float(input('Digite um valor: '))
		if arg > 0:
			return 'Positivo'
		elif arg < 0:
			return 'Negativo'

obj23 = Ex23(0)
positivo_negativo = obj23.Func1(0)
print(f'O valor é: {positivo_negativo}')		