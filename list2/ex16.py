class Ex16(object):
    """16- Criar um programa que dada a idade da pessoa classifique em uma categoria:
a.    5 ~ 7 anos à infantil A
b.    8 ~ 10 anos à infantil B
c.     11 ~ 17 à infantil C
d.    Maior de 18 à adulto"""
    def __init__(self, arg):
        super(Ex16, self).__init__()
        self.arg = arg

    def Categoria(self, arg):
        arg = float(input('Digite sua idade: '))
        if arg < 5:
            return 'infantil anterior ao A ou bebe' 
        elif arg >= 5 and arg <= 7:
            return 'Infantil A'
        elif arg >= 8 and arg <= 10:
            return 'Infantil B'
        elif arg >= 11 and arg <= 17:
            return 'Infantil C'
        elif arg >= 18:
            return 'Maior de 18, adulto'

obj16 = Ex16(0)
idade_categoria = obj16.Categoria(0)
print(idade_categoria)
        