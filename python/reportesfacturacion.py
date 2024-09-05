from tkinter import *

raiz = Tk()
raiz.title("Reportes de Facturación")
nueva_ventana=None

def impresion():
    global nueva_ventana
    nueva_ventana = Toplevel(raiz) 
    nueva_ventana.title("Impresion de datos")
    nueva_ventana.geometry("440x300")
    
    boton_obtener_datos = Button(nueva_ventana, text="Obtener Datos", command=obtener_valores)
    boton_obtener_datos.pack()

def obtener_valores():
        valor_cuadro_texto1 = cuadrotexto1.get()
        valor_cuadro_texto2 = cuadrotexto2.get()
        valor_cuadro_texto3 = cuadrotexto3.get()
        
        etiqueta_datos = Label(nueva_ventana, text=f"NIT: {valor_cuadro_texto1}\nNúmero de Autorización: {valor_cuadro_texto2}\nNúmero de Serie: {valor_cuadro_texto3}", font=fuente)
        etiqueta_datos.pack()
        miLabel5=Label(nueva_ventana, text="¡¡¡ Gracias por su reporte !!!", font=fuente)
        miLabel5.pack()
        
        boton_obtener_datos = Button(nueva_ventana, text="Obtener Datos", command=obtener_valores)
        boton_obtener_datos.pack()
        boton_obtener_datos.destroy()

miFrame = Frame(raiz, width=440, height=300)
miFrame.pack_propagate(0)
miFrame.pack()
fuente = ('Times New Roman', 16)

miLabel = Label(miFrame, text="Reportes de Facturación", font=fuente)
miLabel.pack()
miLabel1 = Label(miFrame, text="Anulación de DTE", font=fuente)
miLabel1.pack()
miLabel2 = Label(miFrame, text="Ingrese su NIT", font=fuente)
miLabel2.pack()
cuadrotexto1 = Entry(miFrame)
cuadrotexto1.pack()
miLabel3 = Label(miFrame, text="Ingrese el número de Autorización", font=fuente)
miLabel3.pack()
cuadrotexto2 = Entry(miFrame)
cuadrotexto2.pack()
miLabel4 = Label(miFrame, text="Ingrese el número de serie de la factura", font=fuente)
miLabel4.pack()
cuadrotexto3 = Entry(miFrame)
cuadrotexto3.pack()

boton_nueva_ventana = Button(miFrame, text="Impresion del reporte", command=impresion)
boton_nueva_ventana.pack()

raiz.mainloop()