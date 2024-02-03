
class Ex1(object):
    """01- Criar um programa que leia 4 notas de um aluno. Apresente o resultado de acordo com a média das notas:
a.    APROVADO - se média maior ou igual a 8,5;
b.    EXAME - se média menor que 8,5 e maior que 6;
c.     RETIDO -  se média menor ou igual a 6;"""
    def __init__(self):
        super(Ex1, self).__init__()
        self.nota1 = float(input('EXERCICIO 1: Digite a primeira nota: '))
        self.nota2 = float(input('Digite a segunda nota: '))
        self.nota3 = float(input('Digite a terceira nota: ')) 
        self.nota4 = float(input('Digite a quarta nota: '))

    def Media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3 + self.nota4)/4

        if self.media >= 8.5:
            return f'Aprovado, pois sua media é: {self.media}'
        elif self.media < 8.5 and self.media > 6:
            return f'Exame, pois sua media é: {self.media}'
        elif self.media <= 6:
            return f'Retido, pois sua media é: {self.media}'

obj1 = Ex1()
media_ex1 = obj1.Media()
print(f'Resultado: {media_ex1}\n')





        