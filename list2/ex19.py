class Ex19(object):
    """Ex19: Criar um programa que classifique de acordo com a leitura do ano de nascimento::
a.    Criança de 0 a 10 anos
b.    Jovem de 11 a 19 anos
c.     Adulto de 20 a 59 anos
d.    Idoso acima de 60 anos"""
    def __init__(self, idade):
        super(Ex19, self).__init__()
        self.idade = idade

    def Classificacao(self, idade):
        idade = float(input('Insira sua idade: '))
        if idade < 0:
            return 'Não existe essa idade'
        elif idade >= 0 and idade <= 10:
            return 'Criança'
        elif idade >= 11 and idade <= 19:
            return 'Jovem'
        elif idade >= 20 and idade <= 59:
            return 'Adulto'
        elif idade >= 60:
            return 'Idoso'

obj19 = Ex19(0)
Classificacao_idade = obj19.Classificacao(0)
print(Classificacao_idade)

        