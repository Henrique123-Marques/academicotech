"""Criar um programa que calcule a area de uma circunferência. Sendo: área=PI*Raio2."""

import math, statistics

class Ex7(object):
	def __init__(self):
		super(Ex7, self).__init__()
		self.raio = float(input('Digite o raio da circunferência: ')) 
	
	def area_circunferencia(self):
		self.area = math.pi * (self.raio**2)
		return self.area

obj7 = Ex7()
circunferencia = obj7.area_circunferencia()
print(f'A area da circunferência é aproximadamente: {circunferencia:.2f}')