class Ex1(object):
	"""Ex1 Crie um programa que apresente uma seq de Fibonacci até o numero escolhido pelo usuario"""
	def __init__(self):
		super(Ex1, self).__init__()

	def Fibonacci(length):
		a = 1
		b = 1
		
		for i in range(length):
			print(a, end=" ")
			a,b=b,a+b

	n = int(input('Quantos numeros? '))
	while(n < 0):
		n = int(input('Digite um numero positivo: '))
	Fibonacci(n)
		