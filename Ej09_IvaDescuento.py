import tkinter as tk
from tkinter import messagebox
ventana_p = tk.Tk ()
ventana_p.title ("Tiendita Y VA")
ventana_p.geometry("600x400")
ventana_p.resizable(False, False)

etiqueta = tk.Label(ventana_p,text="Introduce  la cantidad de productos",font=("Impact",15))
etiqueta.pack(pady=15)
entrada_pr  = tk.Entry(ventana_p, font=("Arial",12))
entrada_pr.pack(pady=5)
eti_resul = tk.Label(ventana_p)
eti_resul.pack (pady=5)

def IVA () :
    try:
        cantidad=float(entrada_pr.get())
        iva1=cantidad*0.16
        eti_resul.config(text=f"IVA: ${iva1:.2f}")
    except ValueError:
        messagebox.showerror("Error, ingrese una cantidad valida")

def desc():
    try:
        cantidad = float(entrada_pr.get())
        descuento = cantidad * 0.10
        eti_resul.config(text=f"Descuento: ${descuento:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese una cantidad válida")

# Función para calcular Total
def total():
    try:
        cantidad = float(entrada_pr.get())
        iva2 = cantidad * 0.16
        desc2 = cantidad * 0.10
        total = cantidad + iva2 - desc2
        eti_resul.config(text=f"TOTAL A PAGAR: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese una cantidad válida")

# Botón para calcular IVA
boton_iva = tk.Button(ventana_p, text="Calcular IVA", font=("Arial", 12),
                      command=IVA, fg="#00EEFF", bg="#000000")
boton_iva.pack(pady=10)

# Botón para calcular Descuento
boton_desc = tk.Button(ventana_p, text="Aplicar Descuento 10%", font=("Arial", 12),
command=desc, fg="#FFFFFF", bg="#DE6AE9")
boton_desc.pack(pady=15)

# Botón para calcular Total
boton_total = tk.Button(ventana_p, text="Pagar Total", font=("Arial", 12),
command=total, fg="#FAFAFA", bg="#90FF99")
boton_total.pack(pady=15)

# Ejecutar la aplicación
ventana_p.mainloop()