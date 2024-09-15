class ParOuImpar:
    def __init__(self):
        self.enunciado = "Escreva um programa que solicite um número do usuário e informe se ele é par ou ímpar."
        self.a= float(input('Digite um número: '))

    def resolver(self):
        if self.a % 2 == 0:
        	return 'Par'
        else:
        	return 'Impar'

obj10 = ParOuImpar()
print(f'O número digitado é {obj10.resolver()}')
