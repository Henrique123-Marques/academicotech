class VerificaçãoDeAnoBissexto:
    def __init__(self):
        self.enunciado = "Escreva um programa que solicite um ano do usuário e determine se esse ano é bissexto."
        self.ano = int(input('Digite um ano: '))
    
    def resolver(self):
    	if self.ano % 4 == 0:
    		return 'Ano bissexto'
    	else:
    		return 'Não é ano bissexto'

obj4 = VerificaçãoDeAnoBissexto()
print(obj4.resolver()) 
        
