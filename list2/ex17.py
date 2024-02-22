class Ex17(object):
    """Criar um programa que leia dois valores reais e apresente o resultado da operação de acordo
     com a escolha do usuário::
a.    +  adição
b.    -  subtração
c.     /  divisão
d.     *  multiplicação"""
    def __init__(self, n1, n2, opcao):
        super(Ex17, self).__init__()
        self.n1 = n1
        self.n2 = n2
        self.opcao = opcao

    def Operacoes(self, n1, n2, opcao):
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        opcao = str(input('Digite A para adição; B para subtração; C para divisão ou D para multiplicação: '))
        if opcao == 'A' or opcao == 'a':
            return n1 + n2
        elif opcao == 'B' or opcao == 'b':
            return n1 - n2
        elif opcao == 'C' or opcao == 'c':
            return n1 / n2
        elif opcao == 'D' or opcao == 'd':
            return n1 * n2

obj17 = Ex17(0,0,0)
operacoes_var = obj17.Operacoes(0,0,0)
print(operacoes_var)



        