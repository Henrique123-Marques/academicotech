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

        
class Tabuada:
    def __init__(self):
    	self.enunciado = "Escreva um programa que solicite um número do usuário e exiba a tabuada desse número de 1 a 10."
    	self.num = float(input('Digite um numero: '))

    def resolver(self):
       for i in range(1,11):
       		print(f'Resultado: {self.num} x {i} = {self.num * i}')
obj2 = Tabuada()
print(f'Ex2: {obj2.resolver()}\n')

class SomaDeNúmeros:
    def __init__(self):
        self.enunciado = "Escreva um programa que leia dois números do usuário e exiba a soma deles."
    
    def resolver(self):
        # Adicione a solução aqui
        pass

class ConversãoDeTemperatura:
    def __init__(self):
        self.enunciado = "Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit. A fórmula é: F = C * 9/5 + 32."
    
    def resolver(self):
        # Adicione a solução aqui
        pass

class VerificaçãoDeAnoBissexto:
    def __init__(self):
        self.enunciado = "Escreva um programa que solicite um ano do usuário e determine se esse ano é bissexto."
    
    def resolver(self):
        # Adicione a solução aqui
        pass

class ContagemDeVogais:
    def __init__(self):
        self.enunciado = "Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário."
    
    def resolver(self):
        # Adicione a solução aqui
        pass

class InverterString:
    def __init__(self):
        self.enunciado = "Escreva um programa que inverta uma string fornecida pelo usuário."
    
    def resolver(self):
        # Adicione a solução aqui
        pass

class Fatorial:
    def __init__(self):
        self.enunciado = "Escreva um programa que calcule o fatorial de um número fornecido pelo usuário."
    
    def resolver(self):
        # Adicione a solução aqui
        pass

class ContagemRegressiva:
    def __init__(self):
        self.enunciado = "Escreva um programa que faça uma contagem regressiva de 10 até 0 e imprima 'Fogo!' ao final."
    
    def resolver(self):
        # Adicione a solução aqui
        pass

class ParOuImpar:
    def __init__(self):
        self.enunciado = "Escreva um programa que solicite um número do usuário e informe se ele é par ou ímpar."
    
    def resolver(self):
        # Adicione a solução aqui
        pass
