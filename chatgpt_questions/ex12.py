print(f'12. Escreva um programa que leia um número e informe se ele é divisível por 3 e 5 simultaneamente.')

class Ex12Divisivel(object):
	def __init__(self):
		self.n = float(input('Digite um numero: '))

	def DivisivelFunc(self):
		if self.n % 3 == 0 and self.n % 5 == 0:
			return True
		else:
			return False

obj12 = Ex12Divisivel()
print(f'{obj12.DivisivelFunc()}')		