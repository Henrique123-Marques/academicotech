"""08 : Criar um programa que leia 4 valores e apresente em distributiva os valores somados e multiplicados. """

from functools import reduce
import math, statistics, operator

class Ex8(object):
	def __init__(self):
		super(Ex8, self).__init__()
		self.n1 = float(input('Digite o primeiro valor: '))
		self.n2 = float(input('Digite o segundo valor: '))
		self.n3 = float(input('Digite o terceiro valor: '))
		self.n4 = float(input('Digite o quarto valor: '))
		self.numeros = [self.n1, self.n2, self.n3, self.n4]

	def Distributiva(self):
		self.somaDistri = sum(self.numeros)
		self.produtoDistri = reduce(operator.mul, self.numeros)
		return f'{self.somaDistri}; {self.produtoDistri}'

obj8 = Ex8()
dsitribuicao = obj8.Distributiva()

print(f'Resultado: {dsitribuicao}')