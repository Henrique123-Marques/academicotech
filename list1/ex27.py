class Ex27(object):
    """27 : Criar um programa que leia um valor real e apresente o valor arredondado."""
    def __init__(self):
        super(Ex27, self).__init__()
        self.valor = float(input('Digite um valor real: '))

    def Arrendondamento(self):
        return f'{self.valor:.2f}' 

obj27 = Ex27()
valor_arredondado = obj27.Arrendondamento()
print(f'Valor arredondado: {valor_arredondado}')
        