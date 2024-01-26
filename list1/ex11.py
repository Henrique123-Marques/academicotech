class Ex11(object):
    """ Criar um programa que leia 4 notas e apresente a media e a soma das notas."""
    def __init__(self):
        self.nota1 = float(input('Insira a primeira nota: '))
        self.nota2 = float(input('Insira a segunda nota: '))
        self.nota3 = float(input('Insira a terceira nota: '))
        self.nota4 = float(input('Insira a quarta nota: '))

    def media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3 + self.nota3)/4
        return self.media 

    def soma(self):
        self.soma = self.nota1 + self.nota2 + self.nota3 + self.nota4
        return self.soma

obj11 = Ex11()
media = obj11.media()
soma = obj11.soma()
print(f'A média das notas é {media}; a soma das notas é {soma   }')
    
