class Ex8(object):
    """08- Criar um programa que leia F ou M para o sexo do usuário e apresente homem ou mulher como resposta."""
    def __init__(self):
        super(Ex8, self).__init__()
        self.genero = str(input('Insira seu genero: M ou F?: '))

    def Genero(self):
        if self.genero == "M" or self.genero == 'm':
            return 'Homem'
        elif self.genero == "F" or self.genero == 'f':
            return 'Mulher'
        else:
            return False

obj8 = Ex8()
Genero_var = obj8.Genero()
print(Genero_var)

        