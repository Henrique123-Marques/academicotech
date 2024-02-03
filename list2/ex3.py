import random, math
 
class Ex3(object):
    """Ex3: Criar um programa que leia 3 valores. Apresente o resultado completo da equação de 2º grau."""
    def __init__(self):
        super(Ex3, self).__init__()
        self.a = float(input('Digite o valor de a: '))
        self.b = float(input('Digite o valor de b: '))
        self.c = float(input('Digite o valor de c: '))

    def Func2Grau(self):
        if self.a < 0 and self.b < 0 and self.c < 0:
            return f'Erro, use apenas valores positivos: '
        else:    
            discriminant = self.b**2 - (4 * self.a * self.c)
            if discriminant >= 0:
                aux = math.sqrt(discriminant)
                return self.b + aux
            else:
                return 'Não há solução, pois o discriminante é negativo'

obj3 = Ex3()
eq_2grau = obj3.Func2Grau()
print(f'Uma possivel solucao para essa equacao é: {eq_2grau}')
