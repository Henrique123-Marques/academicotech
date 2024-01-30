class Ex20(object):
    """Ex20  Criar um programa para ler a temperatura em em Celsius e apresentar a temperatura convertida  em fahrenheit. F=(9*C+160)/5. """
    def __init__(self):
        super(Ex20, self).__init__()
        self.celsius = float(input("Insira a temperatura em celsius: "))

    def Fahrenheit(self):
        self.fahrenheit = ((9*self.celsius+160)/5)
        return self.fahrenheit

obj20 = Ex20()
temp_fahrenheit = obj20.Fahrenheit()
print(f'A temperatura digitada em celsius convertida em fahrenheit é: {temp_fahrenheit}ºF')    