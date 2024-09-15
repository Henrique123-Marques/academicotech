class SomaDeNúmeros:
    def __init__(self):
        self.enunciado = "Escreva um programa que leia dois números do usuário e exiba a soma deles."
        self.n1 = float(input('Digite um numero: '))
        self.n2 = float(input('Digite outro numero: '))
    
    def resolver(self):
      	soma = self.n1 + self.n2
      	return soma

obj3 = SomaDeNúmeros()
print(f'A soma dos numeros é: {obj3.resolver()}')