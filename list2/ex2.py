class Ex2(object):
    """02- Criar um programa que leia 3 variáveis. Apresente as variáveis em ordem crescente"""
    def __init__(self):
        super(Ex2, self).__init__()
        self.arg1 = float(input('EXERCICIO 2: Insira o primeiro valor: '))
        self.arg2 = float(input('EXERCICIO 2: Insira o segundo valor: '))
        self.arg3 = float(input('EXERCICIO 2: Insira o terceiro valor: '))

    def Ordem(self):
        self.ordem = [self.arg1, self.arg2, self.arg3]
        return f'{sorted(self.ordem)}' 
        '''if self.arg1 > self.arg2 and self.arg1 > self.arg3 and self.arg2 < self.arg3:
            return f'{self.arg2}, {self.arg3}, {self.arg1}'
        
        elif self.arg1 < self.arg2 and self.arg1 < self.arg3 and self.arg2 < self.arg3:
            return f'{self.arg1}, {self.arg2}, {self.arg3}'''

obj2 = Ex2()
crescente = obj2.Ordem()
print(f'A lista em ordem crescente é: {crescente}\n')
