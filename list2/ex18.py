import math

class Ex18(object):
    """ Elabore um programa em que receba dez valores reais, 
    calcule a média desses valores, e ao final indique quantos 
    valores estão acima da média."""
    def __init__(self, valores, lista, media, valores_acima):
        super(Ex18, self).__init__()
        self.valores = valores
        self.lista = []
        self.media = media
        self.valores_acima =[]

    def SomaValores(self, valores, lista, media, valores_acima):
        for i in range(10):
            self.valores = float(input('Digite um valor: '))
            self.lista.append(self.valores)
        return sum(self.lista)

    def Media(self, valores, lista, media, valores_acima):
        self.media = sum(self.lista)/len(self.lista)
        return self.media

    def ValoreAcima(self, valores, lista, media, valores_acima):
        for self.valores in self.lista:
            if self.valores > self.media:
                self.valores_acima.append(self.valores)
        return self.valores_acima

obj18 = Ex18(0,[],0,[])
valores_acima_media = obj18.SomaValores(0,[],0,[])
media_valores = obj18.Media(0,[],0,[])
valores_acima_var = obj18.ValoreAcima(0,[],0,[])
print(f'Soma dos valores: {valores_acima_media}; Média dos valores: {media_valores}; Os valores acima da media são: {valores_acima_var}')    