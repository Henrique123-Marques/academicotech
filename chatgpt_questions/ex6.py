class ContagemDeVogais:
    def __init__(self):
        self.enunciado = "Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário."
        self.texto = str(input('Digite uma palavra: '))
        self.lista = [] 

    def resolver(self):
        vogais = 'aeiouAEIOU'
        for letra in self.texto:
        	if letra in vogais:
        		self.lista.append(letra)
        return self.lista

obj6 = ContagemDeVogais()
print(obj6.resolver()) 