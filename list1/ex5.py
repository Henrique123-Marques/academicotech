"""5 : Criar um programa que leia nome e sobrenome e apresente o nome completo."""
class Ex5(object):
	def __init__(self):
		self.nome = str(input('Digite seu nome: '))
		self.sobrenome = str(input('Digite seu sobrenome: '))
		
	def NomeCompleto(self):
		return f'{self.nome} {self.sobrenome}'

objEx5 = Ex5()
nome_completo = objEx5.NomeCompleto()
print(f'Seu nome completo é: {nome_completo}')