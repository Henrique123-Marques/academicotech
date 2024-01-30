class Ex18(object):
    """Criar um programa apresente a media do bimestre sabendo que a segunda prova tem peso 2 e a media é por 3."""
    def __init__(self):
        super(Ex18, self).__init__()
        self.nota1 = float(input('Digite a nota1: '))
        self.nota2 = float(input('Digite a nota2: '))
        self.nota3 = float(input('Digite a nota3: ')) 
        
    def media_bimestre(self):
        self.media = ((self.nota1) + (self.nota2*2) + (self.nota3))/3
        return self.media

obj18 = Ex18()
media_do_bimestre = obj18.media_bimestre()
print(f'A média do bimestre é: {media_do_bimestre}')