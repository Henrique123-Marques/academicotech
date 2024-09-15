import math

class Fatorial:
    def __init__(self):
        self.enunciado = "Escreva um programa que calcule o fatorial de um número fornecido pelo usuário."
        self.num = int(input('Digite um número: '))
    
    def resolver(self):
    	fatorial = math.factorial(self.num)
    	return fatorial

obj8 = Fatorial()
print(obj8.resolver())
