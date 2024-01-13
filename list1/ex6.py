"""06 : Criar um programa que leia 5 valores inteiros e apresente a média aritmética dos valores"""
import statistics

class Ex6(object):
	def __init__(self):
		self.n1 = float(input('Digite o primeiro numero: '))
		self.n2 = float(input('Digite o segundo numero: '))
		self.n3 = float(input('Digite o terceiro numero: '))
		self.n4 = float(input('Digite o quarto numero: '))
		self.n5 = float(input('Digite o quinto numero: '))
		self.numeros = [self.n1, self.n2, self.n3, self.n4, self.n5]

	def Media(self):
		self.media = statistics.mean(self.numeros)
		return self.media
		

objEx6 = Ex6()
media = objEx6.Media()
print(f'A media aritmética dos valores é: {media}')
