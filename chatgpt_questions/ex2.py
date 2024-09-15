       
class Tabuada:
    def __init__(self):
    	self.enunciado = "Escreva um programa que solicite um número do usuário e exiba a tabuada desse número de 1 a 10."
    	self.num = float(input('Digite um numero: '))

    def resolver(self):
       for i in range(1,11):
       		print(f'Resultado: {self.num} x {i} = {self.num * i}')
obj2 = Tabuada()
print(f'Ex2: {obj2.resolver()}\n')