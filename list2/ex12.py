class Ex12(object):
    """12 Criar um programa que converta temperatura de acordo com a vontade do usuário de Celsius para 
    fahrenheit ou de fahrenheit para Celsius."""
    def __init__(self, opcao, celsius, fahrenheit):
        super(Ex12, self).__init__()
        self.opcao = opcao
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def Conversao(self, opcao, celsius, fahrenheit):
        opcao = float(input('Digite 1 para converter Celsius para fahrenheit ou 2 para converter fahrenheit para Celsius: '))
        if opcao == 1:
            celsius = float(input('Insira a temperatura em celsius: '))
            fahrenheit = ((9 * celsius + 160)/5)
            return f'A temperatura digitada em celsius equivale a {fahrenheit} Fº'

        elif opcao == 2:
            fahrenheit = float(input('Insira a temperatura em fahrenheit: '))
            celsius = ((fahrenheit-32)*(5/9))
            return f'A temperatura digitada em fahrenheit equivale a {celsius} Cº'

obj12 = Ex12(0,0,0)
conversor_temperatura = obj12.Conversao(0,0,0)
print(conversor_temperatura)


        