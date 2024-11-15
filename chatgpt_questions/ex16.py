print(f'16. Escreva um programa que solicite ao usuário um número e exiba a sequência de Fibonacci até esse número.')

from sympy import *

class Ex16Fibonacc(object):
	"""docstring for Ex16Fibonacc"""
	def __init__(self):
		self.arg = float(input('Digite um numero: '))

	def Fibonacci(self):
		seq_fibonacci = fibonacci(self.arg)
		return seq_fibonacci

obj16 = Ex16Fibonacc()
print(f'A sequencia fibonacci do numero digitado é: {obj16.Fibonacci()}')


