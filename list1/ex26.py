class Ex26(object):
    """26 : Criar um programa que apresente o caractere digitado pelo usuário"""
    def __init__(self):
        super(Ex26, self).__init__()
        self.caractere = str(input('Insira o caractere: ')) 

    def Caractere(self):
        self.caractere_digitado = self.caractere[0]
        return self.caractere_digitado

obj26 = Ex26()
caractere_variavel = obj26.Caractere()
print(f'Caracter digitado pelo usuario: {caractere_variavel}')