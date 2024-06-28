class ClassName(object):
	"""Ex3: Desenvolva a soma e a média e uma sequencia de 100 termos. O programa deve pedir o primeiro numero e somar
	os 99 posteriores """
	def __init__(self, arg1):
		self.arg1 = arg1

	def SomaSeq(self, arg1):
		arg1 = int(input('Digite o primeiro numero: '))
		termos99 = 99
		soma = (termos99/2) * (arg1 + termos99)	
		return soma
		'''lista = list(range(arg + 1, arg + 100))
		return sum(lista)'''

obj3 = ClassName(0)
sequencial = obj3.SomaSeq(0)
print(f'A soma dos proximos 99 numeros é: {sequencial}')
		