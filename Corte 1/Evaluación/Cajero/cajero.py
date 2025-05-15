class Cajero:
    def __init__(self):
        self.saldo = 0.0

    def consignar(self, cantidad):
        try:
            if cantidad <= 0:
                return "La cantidad debe ser mayor que cero."
            self.saldo += cantidad
            return f"Saldo actualizado: {self.saldo:.2f}"
        except Exception as e:
            return f"Error al consignar ingrese un dato valido"

    def retirar(self, cantidad):
        try:
            if cantidad <= 0:
                return "La cantidad debe ser mayor que cero."
            if cantidad > self.saldo:
                return "Fondos insuficientes."
            self.saldo -= cantidad
            return f"Saldo actualizado: {self.saldo:.2f}"
        except Exception as e:
            return f"Error al retirar ingrese un dato valido"

    def consultar(self):
        return f"Saldo actual: {self.saldo:.2f}"

