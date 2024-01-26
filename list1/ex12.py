class Ex12(object):
    """12 : Criar um programa calculo de salário sendo. 
    Salário bruto = horas trab*valor hr...  total de descontos = (perc de desc/100)*sal bruto... 
    salário liq=sal bruto-total de desc."""
    def __init__(self):
        self.horas_trab = float(input('Insira o numero de horas trabalhadas: '))
        self.valor_hr = float(input('Insira o valor por hora de trabalho: '))

    def SalarioBruto(self):
        self.salario_bruto = (self.horas_trab * self.valor_hr)
        return self.salario_bruto

    def Descontos(self):
        self.perc = float(input('Insira o percentual de desconto: '))
        self.perc_desconto = (self.perc/100) * self.salario_bruto
        return self.perc_desconto

    def SalarioLiquido(self):
        self.salario_liq = self.salario_bruto - self.perc_desconto
        return self.salario_liq

obj12 = Ex12()
salario_bruto = obj12.SalarioBruto()
descontos = obj12.Descontos()
salario_liquido = obj12.SalarioLiquido()

print(f'O salario bruto é {salario_bruto} reais; o percentual de desconto é {descontos}% e o salario liquido é {salario_liquido} reais.')
        