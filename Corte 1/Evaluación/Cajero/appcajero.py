from cajero import Cajero
from menu import Menu

class AppCajero:
    def __init__(self):
        self.cajero = Cajero()
        self.menu = Menu()

    def ejecutar(self):
        while True:
            self.menu.mostrar_menu()
            opcion = self.menu.obtener_opcion()

            if opcion is None:
                continue

            if opcion == 1:
                try:
                    cantidad = float(input("Ingrese la cantidad a consignar: "))
                    print(self.cajero.consignar(cantidad))
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")
            elif opcion == 2:
                try:
                    cantidad = float(input("Ingrese la cantidad a retirar: "))
                    print(self.cajero.retirar(cantidad))
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")
            elif opcion == 3:
                print(self.cajero.consultar())
            elif opcion == 4:
                print("Gracias por usar el cajero. ¡Hasta pronto!")
                break

if __name__ == "__main__":
    app = AppCajero()
    app.ejecutar()