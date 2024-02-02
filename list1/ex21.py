class Ex21(object):
    """Criar um programa para ler uma temperatura em fahrenheit e apresentar a temperatura convertida em Celsius.
C=(f-32)*(5/9)"""
    def __init__(self):
        super(Ex21, self).__init__()
        self.fahrenheit = float(input('Insira a temperatura em fahrenheit: ')) 
        
    def ConverterFahrenheit(self):
        self.celsius = ((self.fahrenheit-32)*(5/9))
        return self.celsius

obj21 = Ex21()
celsius = obj21.ConverterFahrenheit()
print(f'A temperatura digitada equivale a {celsius:.2f} Celsius')