class Menu:
    def mostrar_menu(self):
        print("\n--- Cajero Automático ---")
        print("1. Consignar")
        print("2. Retirar")
        print("3. Consultar saldo")
        print("4. Salir")

    def obtener_opcion(self):
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion not in [1, 2, 3, 4]:
                raise ValueError("Opción no válida.")
            return opcion
        except ValueError as e:
            print(f"Error ingrese un dato valido")
            return None
