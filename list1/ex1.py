'''Exercício 01 : Criar um programa que apresente o resultado da média, sendo R <-- (A + B + ( C * 2 )) / 4.'''

class Ex1():
    """docstring for Ex1"""
    def __init__(self):
        self.a = float(input('Digite o valor de a: '))
        self.b = float(input('Digite o valor de b: '))
        self.c = float(input('Digite o valor de c: '))
        
    def resultado(self):    
        self.r = (self.a + self.b + (self.c*2))/4
        return self.r

obj = Ex1() 
r = obj.resultado()
print(f'Valor de r: {r}')
