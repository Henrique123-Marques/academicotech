class Ex1(object):
	"""docstring for Ex1 Crie um programa que mostre uma sequencia de Fibonacci até o numero de termos
	escolhido pelo usuario"""
	def __init__(self):
		super(Ex1, self).__init__()

	def Fibonacci(self):
		if n <= 0:
			return []
		elif n == 1:
			return [0]
		elif n == 2:
			return [0,1]

		sequencia = [0,1]
		while len(sequencia) < n:
			sequencia.append(sequencia[-1] + sequencia[-2])
		return sequencia	

	def run(self):
		n = float(input('Digite um numero: '))
		seq_fibonacci = self.Fibonacci(n)
		print(f'Sequencia de Fibonacci: {seq_fibonacci}')

obj1 = Ex1()
obj1.run()