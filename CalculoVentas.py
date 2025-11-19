import tkinter as tk
from tkinter import messagebox

ventana_p = tk.Tk()
ventana_p.title("CALCULO DE VENTAS")
ventana_p.geometry("700x500")
ventana_p.configure(bg="#d3ffff")
ventana_p.resizable(False,False)

etiqueta = tk.Label(ventana_p,text="Introduce  la cantidad de productos",font=("Impact",15))
etiqueta.pack(pady=15)
entrada_ar = tk.Entry(ventana_p, font=("Arial", 12))
entrada_ar.pack(pady=10)

etiqueta2 = tk.Label(ventana_p,text="Introduce el precio del producto",font=("Impact",15))
etiqueta2.pack(pady=15)
entrada_pr = tk.Entry(ventana_p,font=("Arial", 12))
entrada_pr.pack(pady=10)




def Multi():
    try:
        num1 = float(entrada_ar.get())
        num2 = float(entrada_pr.get())
        Multi = num1*num2
        resultado.config(text=f"SubTotal = {Multi}$")
    except ValueError:
        resultado.config(text="Introduce un caracter valido")
        
def IVA():
    try:
        num1 = float(entrada_ar.get())
        num2 = float(entrada_pr.get())
        IVA = (num1*num2*0.16)
        resultado.config(text=f"IVA = {IVA}$")
    except ValueError:
        resultado.config(text="Introduce un caracter valido") 
        
def Total ():
    try:
        num1 = float(entrada_ar.get())
        num2 = float(entrada_pr.get())
        Total= (num1*num1)+(num1*num2*0.16)
        resultado.config(text=f"TOTAL = : {Total}$")
    except ValueError:
        resultado.config(text="Introduce un caracter valido")
        
btn_subtotal = tk.Button(ventana_p,text="Subtotal", font=("Arial", 12), command=Multi)
btn_subtotal.pack(pady=10)

btn_IVA = tk.Button(ventana_p,text="IVA", font=("Arial", 12), command=IVA)
btn_IVA.pack(pady=10)

btn_Tot = tk.Button(ventana_p,text="Total", font=("Arial", 12), command=Total)
btn_Tot.pack(pady=10)
        
        
resultado = tk.Label(ventana_p,text="")
resultado.pack(pady=10)





ventana_p.mainloop()
