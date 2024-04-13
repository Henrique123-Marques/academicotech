class Ex20(object):
    """20- Criar um programa que apresente a tabuada de uma valor digitado pelo usuário.0"""
    def __init__(self, arg):
        super(Ex20, self).__init__()
        self.arg = arg

    def Tabuada(self, arg):
        arg = float(input('Digite um valor: '))
        for i in range(1, 11):
            print(f'{arg * i}')

obj20 = Ex20(0)
resultado_tabuada = obj20.Tabuada(0)

        