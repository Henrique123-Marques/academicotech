class ex13(object):
    """13 : Criar um programa que leia o nome completo e apresente uma saudação e o nome completo."""
    def __init__(self):
        super(ex13, self).__init__()
        self.nome = str(input('Insire seu nome completo: '))

    def saudacao(self):
        self.saudacao = str(f'Saudação {self.nome}')
        return self.saudacao

obj13 = ex13()
Saudacao = obj13.saudacao()
print(Saudacao)        