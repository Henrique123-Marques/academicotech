class Ex27(object):
	"""27 .Faça um programa que leia as duas notas parciais obtidas por um aluno em um componente
	 curricular ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à 
	 tabela abaixo::
Média de Aproveitamento Conceito
·           Entre 9.0 e 10.0       A
·           Entre 7.5 e 9.0         B
·           Entre 6.0 e 7.5         C
·           Entre 4.0 e 6.0         D
·           Entre 4.0 e zero        E
O programa deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""
	def __init__(self, nota1, nota2, soma, media):
		self.nota1 = nota1
		self.nota2 = nota2
		self.soma = soma
		self.media = media

	def Soma(self, nota1, nota2, soma, media):
		nota1  = float(input('Digite a primeira nota: '))
		nota2 = float(input('Digite a segunda nota: '))
		soma = nota1 + nota2
		media = soma/2
		if media >= 9 and media <= 10:
			return soma, media, 'Aprovado'
		elif media >= 7.5 and media <= 9:
			return soma, media, 'Aprovado'
		elif media >= 6 and media <= 7.5:
			return soma, media, 'Aprovado'	
		elif media >= 4 and media < 6:
			return soma, media, 'Reprovado'
		elif media >= 0 and media < 4:
			return soma, media, 'Reprovado'

obj27 = Ex27(0,0,0,0)
notas_soma = obj27.Soma(0,0,0,0)
print(f'As notas são:  Soma, média das notas e situação: {notas_soma}')	