import tkinter as tk

def calcular_margen():
    x = float(entry_x.get())
    y = float(entry_y.get())
    descuento = float(entry_descuento.get())

    margen_ganancia = y - x
    descuento_aplicado = y * (descuento / 100)
    y_con_descuento = y - descuento_aplicado
    ganancia_en_CLP = margen_ganancia * 850
    y_con_descuento_en_CLP = y_con_descuento * 850
    descuento_en_CLP = descuento_aplicado * 850

    resultado_margen.config(text=f"Margen de ganancia: {margen_ganancia:.2f} USD ({ganancia_en_CLP:.2f} CLP)")
    resultado_descuento.config(text=f"Valor de venta con descuento: {y_con_descuento:.2f} USD ({y_con_descuento_en_CLP:.2f} CLP)\nDescuento aplicado: {descuento_aplicado:.2f} USD ({descuento_en_CLP:.2f} CLP)")


# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Calculador de margen de ganancia y descuentos")

# Fijar el tamaño de la ventana
ventana.geometry("600x220")  # Fijar tamaño de la ventana
ventana.resizable(False, False)  # Hacer que la ventana no sea redimensionable

# Crear los campos de entrada de datos
label_x = tk.Label(ventana, text="Coste del producto en USD:")
label_x.grid(column=0, row=0)

entry_x = tk.Entry(ventana)
entry_x.grid(column=1, row=0)

label_y = tk.Label(ventana, text="Valor de venta del producto en USD:")
label_y.grid(column=0, row=1)

entry_y = tk.Entry(ventana)
entry_y.grid(column=1, row=1)

label_descuento = tk.Label(ventana, text="Descuento (%):")
label_descuento.grid(column=0, row=2)

entry_descuento = tk.Entry(ventana)
entry_descuento.grid(column=1, row=2)

# Crear el botón de cálculo
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_margen)
boton_calcular.grid(column=1, row=3)

# Crear las etiquetas para mostrar los resultados
resultado_margen = tk.Label(ventana, text="")
resultado_margen.grid(column=0, row=4)

resultado_descuento = tk.Label(ventana, text="")
resultado_descuento.grid(column=1, row=4)

# Iniciar la aplicación
ventana.mainloop()
