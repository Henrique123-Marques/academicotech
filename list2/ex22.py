class Ex22(object):
    """Crie um programa que receba 10 RMs e 10 notas de alunos e ao 
    final mostre o RA com a maior nota, o RM com a menor nota e a média das notas."""
    def __init__(self, rm, notas):
        super(Ex22, self).__init__()
        self.rm = rm
        self.notas = notas
        