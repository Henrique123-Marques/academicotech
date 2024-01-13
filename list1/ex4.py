"""04 : Criar um programa para ler dois valores e apresentar a soma."""
class Ex4(object):
	def __init__(self):
		self.n1 = float(input('Digite o primeiro valor: '))
		self.n2 = float(input('Digite o segundo valor: '))
	
	def Soma(self):
		self.soma = self.n1 + self.n2
		return self.soma

obj4 = Ex4()
soma = obj4.Soma()
print(f'A soma do primeiro e segundo numeros digitados é: {soma}')