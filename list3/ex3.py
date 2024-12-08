class Ex3(object):
	"""Ex3 - Desenvolver um programa que efetue a soma e a média de uma sequencia de 100 termos
	O programa deve pedir o primeiro termo da sequencia e realizar a soma dos 99 termos seguintes"""
	def __init__(self, arg, media):
		super(Ex3, self).__init__()
		self.arg = arg
		self.media = media

	def SomaSequencia(self, arg, media):
		self.arg = int(input('Digite um numero: '))
		for i in range(1, 101):
			self.arg += i  
			self.media = self.arg / 100
		return self.arg, self.media

	'''def MediaSeq(self, arg, media):
		self.arg = int(input('Digite o mesmo valor que o anterior: '))
		for i in range(1,101):
			self.arg += i
			
		return self.media	 '''

obj3 = Ex3(0,0)
print(f'Soma e Média da sequencia solicitada: {obj3.SomaSequencia(0,0)}')
#print(f'Media da sequencia solicitada: {obj3.MediaSeq(0,0)}')