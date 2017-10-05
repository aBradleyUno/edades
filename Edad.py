class Edad():
    def __init__(self):
        self.resultado = ''

    def calculate_edad(self,num1):
		if type(num1) is str:
			self.resultado= "no valido"
		elif num1<0:
			self.resultado = "no existes"
		elif num1<13 and num1>=0:
			self.resultado = "eres nino"
		elif num1>=13 and num1<18:
			self.resultado = "eres adolecente"
		elif num1>=18 and num1<65:
			self.resultado = "eres adulto"
		elif num1>=65 and num1<120:
			self.resultado = "eres adulto mayor"
		else:
			self.resultado = "eres mumm-ra"
    def getResultado(self):
        return self.resultado
