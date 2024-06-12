class Ex30(object):
	"""docstring for Ex30  Criar um programa que calcule a área de um triangulo"""
	def __init__(self):
		super(Ex30, self).__init__()
	
	def AreaTriangulo(self):
		base = float(input('Digite o valor da base: '))
		altura = float(input('Digite o valor da altura: '))
		area = (base*altura)/2 
		return area

obj30 = Ex30()
triangulo_area = obj30.AreaTriangulo()
print(f'A área do triangulo é: {triangulo_area}')