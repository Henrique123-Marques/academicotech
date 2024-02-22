class Ex15(object):
    """15- Criar um programa que leia o ano de nascimento de uma pessoa e apresente sua idade e se pode votar ou não"""
    def __init__(self, nascimento, apto):
        super(Ex15, self).__init__()
        self.nascimento = nascimento
        self.apto = apto

    def Votacao(self, nascimento, apto):
        nascimento = float(input('Digite o seu ano de nascimento: '))
        apto = 2024 - nascimento
        if apto < 18:
            return False
        elif apto >= 18:
            return True

obj15 = Ex15(0,0)
votacao_apto = obj15.Votacao(0,0)
print(f'Se True, pode votar, caso contrario False, sua condição é: {votacao_apto}')
        
        