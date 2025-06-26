import tkinter as tk
from tkinter import messagebox
from calculadora_logica import Calculadora

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.calculadora = Calculadora()

        # Create input fields
        self.label_num1 = tk.Label(master, text="Número 1:")
        self.label_num1.grid(row=0, column=0, padx=5, pady=5)
        self.entry_num1 = tk.Entry(master, width=30)
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)

        self.label_num2 = tk.Label(master, text="Número 2:")
        self.label_num2.grid(row=1, column=0, padx=5, pady=5)
        self.entry_num2 = tk.Entry(master, width=30)
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)

        # Create result display
        self.label_resultado = tk.Label(master, text="Resultado:")
        self.label_resultado.grid(row=2, column=0, padx=5, pady=5)
        self.resultado_var = tk.StringVar()
        self.display_resultado = tk.Label(master, textvariable=self.resultado_var, width=28, anchor="w", relief="sunken", bd=1)
        self.display_resultado.grid(row=2, column=1, padx=5, pady=5)

        # Create buttons for operations
        self.btn_sumar = tk.Button(master, text="Sumar", command=self.perform_sumar, width=10)
        self.btn_sumar.grid(row=3, column=0, padx=5, pady=5)

        self.btn_restar = tk.Button(master, text="Restar", command=self.perform_restar, width=10)
        self.btn_restar.grid(row=3, column=1, padx=5, pady=5)

        self.btn_multiplicar = tk.Button(master, text="Multiplicar", command=self.perform_multiplicar, width=10)
        self.btn_multiplicar.grid(row=4, column=0, padx=5, pady=5)

        self.btn_dividir = tk.Button(master, text="Dividir", command=self.perform_dividir, width=10)
        self.btn_dividir.grid(row=4, column=1, padx=5, pady=5)

        self.btn_modulo = tk.Button(master, text="Módulo", command=self.perform_modulo, width=10)
        self.btn_modulo.grid(row=5, column=0, padx=5, pady=5)

        self.btn_limpiar = tk.Button(master, text="Limpiar", command=self.clear_fields, width=10)
        self.btn_limpiar.grid(row=5, column=1, padx=5, pady=5)

    def get_numbers(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese números válidos en ambos campos.")
            return None, None

    def display_result(self, result):
        self.resultado_var.set(str(result))

    def perform_sumar(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.calculadora.sumar(num1, num2)
            self.display_result(result)

    def perform_restar(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.calculadora.restar(num1, num2)
            self.display_result(result)

    def perform_multiplicar(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.calculadora.multiplicar(num1, num2)
            self.display_result(result)

    def perform_dividir(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.calculadora.dividir(num1, num2)
            self.display_result(result)

    def perform_modulo(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.calculadora.modulo(num1, num2)
            self.display_result(result)

    def clear_fields(self):
        self.entry_num1.delete(0, tk.END)
        self.entry_num2.delete(0, tk.END)
        self.resultado_var.set("")

def main():
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()