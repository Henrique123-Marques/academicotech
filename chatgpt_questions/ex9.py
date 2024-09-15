class ContagemRegressiva:
    def __init__(self):
        self.enunciado = "Escreva um programa que faça uma contagem regressiva de 10 até 0 e imprima 'Fogo!' ao final."
    
    def resolver(self):
        for i in range(10, -1, -1):
        	print(i)
        return 'Fogo!'

obj9 = ContagemRegressiva()
print(obj9.resolver())
        