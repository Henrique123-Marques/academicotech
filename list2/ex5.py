class Ex5(object):
    """05- Criar um programa que leia 10 valores e apresente o maior valor par e o menor valor impar."""
    def __init__(self):
        super(Ex5, self).__init__()
    
    def Listas(self):
        listaPar = list()
        listaImpar = list()
        for i in range(10):
            self.arg = float(input('Digite um valor: '))
            if self.arg % 2 == 0:
                listaPar.append(self.arg)
            elif self.arg % 2 == 1:
                listaImpar.append(self.arg)


        maiorPar = max(listaPar)
        menorImpar = min(listaImpar)

        return f'Lista de valores pares: {listaPar}; Lista de valores impares: {listaImpar}\nMaior valor par: {maiorPar}; Menor valor impar: {menorImpar}'

obj5 = Ex5()
listas_par_impar = obj5.Listas()
print(f' {listas_par_impar}')
    
        