import math

class Ex29(object):
	"""docstring for Ex29 Criar um programa que leia 10 valores e apresente:
a.    Maior valor
b.    Menor valor
c.     Media dos valores pares
d.    Media dos valores impares
e.     Media dos valores"""
	def __init__(self):
		super(Ex29, self).__init__()
		self.lista1 = []

	def Apresentacao(self):
		for i in range(10):
			n = float(input('Digite um valor: '))
			self.lista1.append(n)
		return max(self.lista1), min(self.lista1), sum(self.lista1)/len(self.lista1)

obj29 = Ex29()
apresentacao_var = obj29.Apresentacao()
print(f'Maior valor, Menor valor e Média dos 10 valores respectivamente: {apresentacao_var}')

