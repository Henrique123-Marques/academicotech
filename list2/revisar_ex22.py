class Ex22(object):
    """Crie um programa que receba 10 RMs e 10 notas de alunos e ao 
    final mostre o RM com a maior nota, o RM com a menor nota e a média das notas."""
    def __init__(self, rm, notas, maior, menor, media, lista_rm, list_notas):
        super(Ex22, self).__init__()
        self.rm = rm
        self.notas = notas
        self.menor = menor
        self.maior = maior
        self.media = media
        self.list_rm = [] 
        self.list_notas = []

    def analysis_rm_nota(self, rm, notas, maior, menor, media, lista_rm, list_notas):
        for i in range(10):
            self.rm = float(input('Insira o RM: '))
            self.notas = float(input('Insira a nota: '))
            self.list_rm.append(self.rm)
            self.list_notas.append(self.notas)

    def Maior(self, rm, notas, maior, menor, media, lista_rm, list_notas):
        for self.notas in self.list_notas:
            self.maior = max(self.list_notas)
        return self.maior

    def Menor(self, rm, notas, maior, menor, media, lista_rm, list_notas):
        for self.notas in self.list_notas:
            self.menor = min(self.list_notas)
        return self.menor

    def Media_Notas(self, rm, notas, maior, menor, media, lista_rm, list_notas):
        self.media = sum(self.list_notas)/len(self.list_notas)
        return self.media

obj22 = Ex22(0,0,0,0,0,[],[])
analise = obj22.analysis_rm_nota(0,0,0,0,0,[],[])
maior_nota = obj22.Maior(0,0,0,0,0,[],[])
menor_nota = obj22.Menor(0,0,0,0,0,[],[])
media_notas = obj22.Media_Notas(0,0,0,0,0,[],[])
print(f'Maior nota e Menor Nota: {maior_nota} e {menor_nota}; Media das notas: {media_notas}')