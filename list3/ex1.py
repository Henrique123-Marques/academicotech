class Ex1(object):
	"""docstring for Ex1 Crie um programa que mostre uma sequencia de Fibonacci até o numero de termos
	escolhido pelo usuario"""
	def __init__(self):
		super(Ex1, self).__init__()

	def Fibonacci(self):
		n = float(input('Digite um numero: '))
		if n <= 1:
			return n
		else:
			return Fibonacci(n-1) + Fibonacci(n-2)

obj1 = Ex1()
seq_fibonacci = obj1.Fibonacci()
print(f'Sequencia de Fibonacci: {seq_fibonacci}')
		
		