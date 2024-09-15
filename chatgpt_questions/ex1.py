class NúmerosPares:
    def __init__(self):
        self.enunciado = "Escreva um programa que imprima todos os números pares de 1 a 50."
        self.pares = []
    	
    def resolver(self):
    	for i in range(1,51):
    		if i % 2 == 0:
    			self.pares.append(i)
    	return self.pares

obj1 = NúmerosPares()
print(f'Ex1: Números pares de 1 a 50: {obj1.resolver()}\n')