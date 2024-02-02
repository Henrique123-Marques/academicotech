class Ex28(object):
    """Criar um programa que repita uma operação sem a utilização de uma função de looping (repetição)."""
    def __init__(self):
        super(Ex28, self).__init__()
        self.valor1 = float(input('Digite o primeiro valor: '))
        self.valor2 = float(input('Digite o segundo valor: '))

    def operacao(self):
        self.soma = self.valor1 + self.valor2
        return self.soma

obj28 = Ex28()
soma = obj28.operacao()
print(f'Soma da operacao: {soma}')
print(f'Soma da operacao: {soma}') 
        