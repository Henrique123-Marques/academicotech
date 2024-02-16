class Ex14(object):
    """Criar um programa que leia altura e sexo do usuário e apresente seu peso ideal. 
    Formulas :: Homensà(72,7 * h) – 58 <::> MULHERES à(62,1 * h) – 44,7."""
    def __init__(self, altura, sexo, homem, mulher):
        super(Ex14, self).__init__()
        self.altura = altura
        self.sexo = sexo
        self.homem = homem
        self.mulher = mulher

    def Peso_ideal(self, altura, sexo, homem, mulher):
        altura = float(input('Digite a altura do usuário: '))
        sexo = str(input('Digite M para Homem ou F para Mulher: '))
        if sexo == 'M' or sexo == 'm':
            homem = ((72.7 * altura) - 58)
            return f'O peso ideal do usuario homem é: {homem}'

        elif sexo == 'F' or sexo == 'f':
            mulher = ((62.1 * altura) - 44.7)
            return f'O peso ideal da usuaria mulher é: {mulher}'

obj14 = Ex14(0,"",0,0)
PesoIdeal_var = obj14.Peso_ideal(0,"",0,0)
print(PesoIdeal_var) 