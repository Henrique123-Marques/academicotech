class Ex10(object):
    """Criar um programa que calcule o volume de uma caixa retangular. Vol = altura*comprimento*largura."""
    def __init__(self):
        self.altura = float(input('Insira a altura da caixa: '))
        self.comprimento = float(input('Insira o comprimento da caixa: '))
        self.largura = float(input('Insira a largura da caixa: '))

    def volume(self):
        self.volume = (self.altura * self.comprimento * self.largura)
        return self.volume

obj10 = Ex10()
volume = obj10.volume()
print(f'O volume da caixa é: {volume}')
        