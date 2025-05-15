class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: División por cero no permitida."

    def modulo(self, a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return "Error: División por cero no permitida."

mi_calculadora = Calculadora()
print(mi_calculadora.sumar(5,7))
print(mi_calculadora.restar(45,11))
print(mi_calculadora.multiplicar(3,2))
print(mi_calculadora.dividir(10,0))
print(mi_calculadora.modulo(10,0))