class InverterString:
    def __init__(self):
        self.enunciado = "Escreva um programa que inverta uma string fornecida pelo usuário."
        self.texto = str(input('Escreva uma palavra: '))

    def resolver(self):
        string_invertida = ''.join(reversed(self.texto))
        return string_invertida

obj7 = InverterString()
print(obj7.resolver())