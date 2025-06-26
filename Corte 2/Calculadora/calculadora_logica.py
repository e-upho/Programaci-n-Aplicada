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