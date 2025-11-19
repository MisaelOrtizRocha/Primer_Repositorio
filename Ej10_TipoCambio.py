import tkinter as tk
from tkinter import messagebox

ventana_p = tk.Tk()
ventana_p.title("DIVISAS  " )
ventana_p.geometry("600x400")
ventana_p.configure(bg="#e0ffff")
ventana_p.resizable(False, False)

etiqueta = tk.Label(ventana_p, text="Introduce la cantidad que deseas cambiar ")
etiqueta.pack(pady=5)

cantidad_pesos = tk.Entry(ventana_p, font=("Arial", 12))
cantidad_pesos.pack(pady=5)

def dolar():
    try:
        cantidad = float(cantidad_pesos.get())
        dolares = cantidad / 19.19
        etiqueta_result.config(text=f"Dolares: ${dolares:.2f}", font=("impact", 15))
    except ValueError:
        messagebox.showerror("Teclea una cantidad")

def euro():
    try:
        cantidad = float(cantidad_pesos.get())
        euro = cantidad / 21.45
        etiqueta_result.config(text=f"Euros: ${euro:2f}", font=("impact", 15))
    except ValueError:
        messagebox.showerror("Teclea una cantidad")

def libra():
    try:
        cantidad = float(cantidad_pesos.get())
        libras = cantidad / 24.68
        etiqueta_result.config(text=f"Libras: ${libras:.2f}", font=("impact", 15))
    except ValueError:
        messagebox.showerror("Teclea una cantidad")

def yen():
    try:
        cantidad = float(cantidad_pesos.get())
        yenes = cantidad / 0.12
        etiqueta_result.config(text=f"Yenes: ${yenes:.2f}", font=("impact", 15))
    except ValueError:
        messagebox.showerror("Teclea una cantidad")

boton_dolar = tk.Button(ventana_p, text="Dolares", font=("Arial", 12), command=dolar)
boton_dolar.pack(pady=10)

boton_euro = tk.Button(ventana_p, text="Euros", font=("Arial", 12), command=euro)
boton_euro.pack(pady=10)

boton_libra = tk.Button(ventana_p, text="Libras", font=("Arial", 12), command=libra)
boton_libra.pack(pady=10)

boton_yen = tk.Button(ventana_p, text="Yenes", font=("Arial", 12), command=yen)
boton_yen.pack(pady=10)

etiqueta_result = tk.Label(ventana_p)
etiqueta_result.pack(pady=10)

ventana_p.mainloop()