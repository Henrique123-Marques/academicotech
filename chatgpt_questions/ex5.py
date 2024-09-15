class ConversãoDeTemperatura:
	def __init__(self):
		self.enunciado = "Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit. A fórmula é: F = C * 9/5 + 32."
		self.celsius = float(input('Digite uma temperatura em celsius: '))

	def resolver(self):
		fahrenheit = ((self.celsius * 9/5) + 32)
		return fahrenheit

obj5 = ConversãoDeTemperatura()
print(f'{obj5.resolver()} Fahrenheit')
    
