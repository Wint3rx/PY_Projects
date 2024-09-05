from tkinter import *
from random import *

letras = "ABCDEFGHIJKLMNOPKRSTUVWXYZ"
numeros = "0123456789"
unir = f"{letras}{numeros}"
longitud = 32
extension = ''.join(sample(letras + numeros, 8)) + '-' + ''.join(sample(letras + numeros, 4)) + '-' + ''.join(sample(letras + numeros, 4)) + '-' + ''.join(sample(letras + numeros, 4)) + '-' + ''.join(sample(letras + numeros, 12))
dte = randint(10000000, 999999999)

raiz = Tk()

miFrame = Frame(raiz, width=440, height=860)
miFrame.pack()

miLabel = Label(miFrame, text="COMIDILLA RIQUILLA")
miLabel.place(x=165)
miLabel0 = Label(miFrame, text="NIT: 89302910")
miLabel0.place(x=190, y=20)
miLabel1 = Label(miFrame, text="DOCUMENTO TRIBUTARIO ELECTRONICO")
miLabel1.place(x=120, y=60)
miLabel2 = Label(miFrame, text="FACTURA")
miLabel2.place(x=200, y=80)
miLabel3 = Label(miFrame, text="AUTORIZACION No.")
miLabel3.place(x=170, y=100)
miLabel4 = Label(miFrame, text=extension)
miLabel4.place(x=108, y=120)
miLabel5 = Label(miFrame, text="Numero de DTE: " + str(dte))
miLabel5.place(x=155, y=140)

miLabel6 = Label(miFrame, text="NIT del cliente: ")
miLabel6.place(x=190, y=180)
ct1 = Entry(miFrame)    
ct1.place(x=170, y=200)
miLabel7 = Label(miFrame, text="Datos de compra")
miLabel7.place(x=180, y=220)
ct2 = Entry(miFrame)
ct2.place(x=170, y=240)
miLabel8 = Label(miFrame, text="Cantidad de productos")
miLabel8.place(x=170, y=260)
ct3 = Entry(miFrame)
ct3.place(x=170, y=280)
miLabel9 = Label(miFrame, text="Productos comprados")
miLabel9.place(x=170, y=300)
ct4 = Entry(miFrame)
ct4.place(x=170, y=320)

miLabel10 = Label(miFrame, text="Gracias por su compra <3", font=("Comic Sans MS", 18))
miLabel10.place(x=90, y=800)

def crear_nueva_ventana():
    nueva_ventana = Toplevel(raiz)  # Crea una nueva ventana
    nueva_ventana.geometry("440x860")  # Establece las dimensiones de la nueva ventana

    miFrameNueva = Frame(nueva_ventana, width=440, height=860)
    miFrameNueva.pack()

    # Copia los elementos y sus configuraciones a la nueva ventana
    Label(miFrameNueva, text="COMIDILLA RIQUILLA").place(x=165)
    Label(miFrameNueva, text="NIT: 89302910").place(x=190, y=20)
    Label(miFrameNueva, text="DOCUMENTO TRIBUTARIO ELECTRONICO").place(x=120, y=60)
    Label(miFrameNueva, text="FACTURA").place(x=200, y=80)
    Label(miFrameNueva, text="AUTORIZACION No.").place(x=170, y=100)
    Label(miFrameNueva, text=extension).place(x=108, y=120)
    Label(miFrameNueva, text="Numero de DTE: " + str(dte)).place(x=155, y=140)

    Label(miFrameNueva, text="NIT del cliente: ").place(x=190, y=180)
    ct1_nueva = Entry(miFrameNueva)
    ct1_nueva.insert(0, ct1.get())  # Copia el contenido de ct1
    ct1_nueva.place(x=170, y=200)

    Label(miFrameNueva, text="Datos de compra").place(x=180, y=220)
    ct2_nueva = Entry(miFrameNueva)
    ct2_nueva.insert(0, ct2.get())  # Copia el contenido de ct2
    ct2_nueva.place(x=170, y=240)

    Label(miFrameNueva, text="Cantidad de productos").place(x=170, y=260)
    ct3_nueva = Entry(miFrameNueva)
    ct3_nueva.insert(0, ct3.get())  # Copia el contenido de ct3
    ct3_nueva.place(x=170, y=280)

    Label(miFrameNueva, text="Productos comprados").place(x=170, y=300)
    ct4_nueva = Entry(miFrameNueva)
    ct4_nueva.insert(0, ct4.get())  # Copia el contenido de ct4
    ct4_nueva.place(x=170, y=320)

    Label(miFrameNueva, text="Gracias por su compra <3", font=("Comic Sans MS", 18)).place(x=90, y=800)

# Crear un botón para abrir una nueva ventana con los datos
boton_nueva_ventana = Button(miFrame, text="Impresion", command=crear_nueva_ventana)
boton_nueva_ventana.place(x=200, y=350)

raiz.mainloop()
