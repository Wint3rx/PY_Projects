import tkinter as tk
import webbrowser
import sqlite3
from tkinter import *
from random import *
from tkinter import messagebox
from tkinter import ttk


def abrir_ventana2():
    ventanai.withdraw()  # Oculta la ventana de inicio

    # Código de la ventana de inventario
    ventana2 = Toplevel()
    ventana2.title("Inventario FASTFOOD")
    ventana2.geometry("700x450")
    ventana2.configure(bg='lightblue')

    miCodigo = StringVar()
    miProducto = StringVar()
    miComida = StringVar()
    miPreciouni = StringVar()
    miCantidad = StringVar()

    def conecBD():
        miConexion = sqlite3.connect("FOOD.db")
        miCursor = miConexion.cursor()

        try:
            miCursor.execute('''
                CREATE TABLE IF NOT EXISTS fastfood (
                    CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
                    PRODUCTO VARCHAR(50) NOT NULL,
                    COMIDA VARCHAR(50) NOT NULL,
                    CANTIDAD INT NOT NULL,
                    PRECIO INT NOT NULL
                )
            ''')

            messagebox.showinfo("CONEXION", "BASE DE DATOS CREADA")
        except:
            messagebox.showinfo("CONEXION", "Conexion realizada")

    def eliminarbd():
        miConexion = sqlite3.connect("FOOD.db")
        miCursor = miConexion.cursor()
        if messagebox.askyesno(message="Seguro que quieres borrar?", title="OJO"):
            miCursor.execute("DROP TABLE IF EXISTS fastfood")
            miConexion.commit()
        else:
            pass
        limpiar()
        mostrar()

    def fuera():
        valor = messagebox.askquestion("Salir", "¿Lista para irte?")
        if valor == "yes":
            ventana2.destroy()

    def limpiar():
        miCodigo.set("")
        miProducto.set("")
        miComida.set("")
        miPreciouni.set("")
        miCantidad.set("")

    def msg():
        acerca = '''
        Inventario nice
        VERSION BETA
        EN producción
        '''
        messagebox.showinfo("Acerca de", acerca)

    def nuevo():
        miConexion = sqlite3.connect("FOOD.db")  
        miCursor = miConexion.cursor() 
        try:
            datos = miProducto.get(), miComida.get(), miCantidad.get(), miPreciouni.get()
            miCursor.execute("INSERT INTO fastfood VALUES(NULL,?,?,?,?)", (datos))  
            miConexion.commit()
        except:
            messagebox.showwarning("CUIDADO", "HUBO UN ERROR, INVALIDO") 
            pass
        limpiar()
        mostrar()

    def mostrar():
        miConexion = sqlite3.connect("FOOD.db")  
        miCursor = miConexion.cursor() 
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            miCursor.execute("SELECT * FROM fastfood")
            for row in miCursor:
                tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4])) 
        except:
            pass

    tree = ttk.Treeview(height=12, columns=('#0', '#1', '#2', '#3'))
    tree.place(x=0, y=150)
    tree.column('#0', width=140)
    tree.heading('#0', text="CODIGO", anchor=CENTER) 
    tree.column('#1', width=140)
    tree.heading('#1', text="Producto", anchor=CENTER) 
    tree.column('#2', width=140)
    tree.heading('#2', text="Comida", anchor=CENTER) 
    tree.column('#3', width=140)
    tree.heading('#3', text="Cantidad", anchor=CENTER) 
    tree.column('#4', width=140)
    tree.heading('#4', text="Precio total", anchor=CENTER) 

    def seleccion(event):
        item = tree.focus()
        miCodigo.set(tree.item(item, "text"))
        miProducto.set(tree.item(item, "values")[0])
        miComida.set(tree.item(item, "values")[1])
        miCantidad.set(tree.item(item, "values")[2])
        miPreciouni.set(tree.item(item, "values")[3])
    tree.bind("<Double-1>", seleccion)

    def modificar():
        miConexion = sqlite3.connect("FOOD.db")
        miCursor = miConexion.cursor() 
        try:
            datos = miProducto.get(), miComida.get(), miCantidad.get(), miPreciouni.get()
            miCursor.execute("UPDATE fastfood SET PRODUCTO=?, COMIDA=?, CANTIDAD=?, PRECIO=? WHERE CODIGO="+miCodigo.get(), (datos))
            miConexion.commit()
        except:
            messagebox.showwarning("CUIDADO", "HUBO UN ERROR EN LA ACTUALIZACIÓN")
            pass

    def borrar():
        miConexion = sqlite3.connect("FOOD.db")
        miCursor = miConexion.cursor() 
        try:
            if messagebox.askyesno(message="Seguro que quieres borrar? no hay vuelta atras", title="OJO"):
                miCursor.execute("DELETE FROM fastfood WHERE CODIGO="+miCodigo.get())
                miConexion.commit() 
        except:
            messagebox.showwarning("CUIDADO", "HUBO UN ERROR EN LA ELIMINACIÓN")
            pass

    menubar=Menu(ventana2)
    menubasedat=Menu(menubar, tearoff=0)
    menubasedat.add_command(label="Crear o conectar BD", command=conecBD)
    menubasedat.add_command(label="ELIMINAR BD", command=eliminarbd)
    menubasedat.add_command(label="Salir?", command=fuera)
    menubar.add_cascade(label="Incio", menu=menubasedat)

    ayudamenu=Menu(menubar, tearoff=0)
    ayudamenu.add_command(label="Limpiar campos", command=limpiar)
    ayudamenu.add_command(label="INFO del sistema", command=msg)
    menubar.add_cascade(label="Ayuda",menu=ayudamenu)

    e1=Entry(ventana2, textvariable=miCodigo)

    l2=Label(ventana2, text="Producto", background=("green"))
    l2.place(x=30, y=10)
    e2=Entry(ventana2, textvariable=miProducto, width=28)
    e2.place(x=100, y=10)

    l6=Label(ventana2, text="Cantidad", background=("green"))
    l6.place(x=280, y=10)
    e6=Entry(ventana2, textvariable=miCantidad, width=15)
    e6.place(x=370, y=10)

    l3=Label(ventana2, text="Comida", background=("green"))
    l3.place(x=30, y=40)
    e3=Entry(ventana2, textvariable=miComida, width=20)
    e3.place(x=100, y=40)

    l4=Label(ventana2, text="Precio total",background=("green"))
    l4.place(x=280, y=40)
    e4=Entry(ventana2, textvariable=miPreciouni, width=15)
    e4.place(x=370, y=40)

    l5=Label(ventana2, text="Q", background="light blue")
    l5.place(x=450, y=40)

    l7=Label(ventana2, text="Que bueno verte de nuevo", background="light blue")
    l7.place(x=520, y=10)

    #botones
    b1=Button(ventana2, text="Crear registro", command=nuevo, background="yellow")
    b1.place(x=50, y=90)

    b2=Button(ventana2, text="Modificar registro", command=modificar, background="yellow")
    b2.place(x=180, y=90)

    b3=Button(ventana2, text="Mostrar productos", command=mostrar, background="yellow")
    b3.place(x=340, y=90)

    b4=Button(ventana2, text="Borrar Registro", command=borrar, background="red")
    b4.place(x=500, y=90)

    ventana2.config(menu=menubar)
    ventana2.mainloop()

def abrir_ventana3():
    ventanai.withdraw()
    anexo=sqlite3.connect('producto')
    cursor1= anexo.cursor()
    #------------------------------------------BD--------------------------------------
    def tablaexiste(nombret):
        cursor1.execute("SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE= 'table' AND name = '{}'".format(nombret))
        if cursor1.fetchone()[0]==1:
            return True
        else:
            cursor1.execute(f"CREATE TABLE MENU (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE TEXT, PRECIO REAL)")
            return False
    tablaexiste("MENU")

    def selecproduc(tabla):
        cursor1.execute(f'SELECT * FROM {tabla}')
        lista =[]
        for filaencontrada in cursor1.fetchall():
            lista.append(filaencontrada)
        return lista


    #------------------------------------------VENTANAS-----------------------------------------
    fuentetitulo=('Helvetica',20)
    fuenteboton=('Verdana',15)

    menuproduct = Tk()
    menuproduct.title("PRODUCTOS")
    menuproduct.geometry("700x450")
    menuproduct.configure(bg='white')

    S1=Label(menuproduct, text="BIENVENIDO AL APARTADO DE PRODUCTOS", font=fuentetitulo)
    S1.configure(bg='white')
    S1.pack()
    s2=Label(menuproduct,text="Porfavor digame que es lo que desea hacer")
    s2.configure(bg='white')
    s2.pack()
    s3=Label(menuproduct)
    s3.configure(bg='white')
    s3.pack()

    def producto1():
        producto1 = Toplevel()
        producto1.title("Ingreso de Nuevo Producto")
        producto1.geometry("250x200")
        producto1.configure(bg='light cyan')

        def insertar():
            nombre_producto = nombre_entry.get()
            precio_producto = float(precio_entry.get())
            cursor1.execute(f"INSERT INTO MENU (nombre, precio) VALUES (?, ?)", (nombre_producto, precio_producto))
            anexo.commit()
            correcto.config(text=f"\nEl nuevo producto ha sido agregado correctamente ^^")

        # Create and pack labels, entry fields, and a button
        sp1=Label(producto1)
        sp1.configure(bg='light cyan')
        sp1.pack()
        nombre=Label(producto1, text="Nombre del Producto:")
        nombre.configure(bg='light cyan')
        nombre.pack()
        nombre_entry = Entry(producto1)
        nombre_entry.pack()

        precio=Label(producto1, text="Precio del Producto:")
        precio.configure(bg='light cyan')
        precio.pack()
        precio_entry = Entry(producto1)
        precio_entry.pack()   
        
        sp2=Label(producto1)
        sp2.configure(bg='light cyan')
        sp2.pack()

        insert_button =Button(producto1, text="Insertar Producto", command=insertar)
        insert_button.pack()

        correcto = Label(producto1, text="")
        correcto.configure(bg='light cyan')
        correcto.pack()

    def producto2():
        global opcion
        producto2 = Toplevel()
        producto2.title("Modificar Producto")
        producto2.geometry("400x100")
        producto2.configure(bg='light cyan')

        produc=Label(producto2, text="Ingrese el codigo del producto que desea modificar:")
        produc.configure(bg='light cyan')
        produc.pack()
        cod = Entry(producto2)
        cod.pack()

        def actu():
            codigo=cod.get()
            def guardar_cambios():
                nuevo_nombre = entry_nombre.get()
                nuevo_precio = entry_precio.get()

                if nuevo_nombre or nuevo_precio:
                    if nuevo_nombre:
                        cursor1.execute(f"UPDATE MENU SET NOMBRE = ? WHERE CODIGO = ?", (nuevo_nombre, codigo))
                    if nuevo_precio:
                        cursor1.execute(f"UPDATE MENU SET PRECIO = ? WHERE CODIGO = ?", (nuevo_precio, codigo))

                    anexo.commit()
                    label_resultado.config(text=f"Registro con código {codigo} actualizado correctamente.")
                else:
                    label_resultado.config(text="No se realizaron cambios.")

            cursor1.execute(f'SELECT NOMBRE, PRECIO FROM MENU WHERE CODIGO == {codigo}')
            registro = cursor1.fetchone()
            if registro is None:
                label_resultado.config(text=f"No se encontró ningún registro con el código {codigo}.")
            else:
                nombre_actual, precio_actual = registro

                ventana = Toplevel()
                ventana.title(f"Actualización de Registro con Código {codigo}")

                label_nombre = Label(ventana, text="Nombre actual:")
                label_nombre.grid(row=0, column=0)
                label_precio = Label(ventana, text="Precio actual:")
                label_precio.grid(row=1, column=0)

                entry_nombre = Entry(ventana)
                entry_nombre.grid(row=0, column=1)
                entry_nombre.insert(0, nombre_actual)

                entry_precio = Entry(ventana)
                entry_precio.grid(row=1, column=1)
                entry_precio.insert(0, precio_actual)

                boton_guardar = Button(ventana, text="Guardar Cambios", command=guardar_cambios)
                boton_guardar.grid(row=2, column=0, columnspan=2)

                label_resultado = Label(ventana, text="")
                label_resultado.grid(row=3, column=0, columnspan=2)


        boton2=Button(producto2, text="Modificar producto", command=actu)
        boton2.pack()

    def producto3():
        producto3 = Toplevel()
        producto3.title("Eliminar Producto")
        producto3.geometry("400x150")
        producto3.configure(bg='light cyan')

        etiqueta = Label(producto3, text="Eliminar un producto")
        etiqueta.configure(bg='light cyan')
        etiqueta.pack()

        # Entrada para ingresar el código
        codi=Label(producto3, text="Ingrese el código del producto que desea eliminar:")
        codi.configure(bg='light cyan')
        codi.pack()
        codigo = Entry(producto3)
        codigo.pack()

        def confirmar_eliminacion():
            codigo_ingresado = codigo.get()
            
            if  codigo_ingresado:
                cursor1.execute(f'DELETE FROM MENU WHERE CODIGO = ?', (codigo_ingresado,))
                anexo.commit()
                label_resultado.config(text=f"Producto con código {codigo_ingresado} eliminado correctamente.")
            else:
                label_resultado.config(text="Por favor, complete todos los campos.")

        boton_eliminar = Button(producto3, text="Eliminar Producto", command=confirmar_eliminacion)
        boton_eliminar.pack()

        label_resultado = Label(producto3, text="")
        label_resultado.pack()

    def producto4():
        producto4 = Toplevel()
        producto4.title("Productos en el Menú ")
        producto4.geometry("400x500")
        producto4.configure(bg='light cyan')
        cursor1.execute(f'SELECT * FROM MENU')
        productos = cursor1.fetchall()

        if productos:
            for producto in productos:
                producto_texto = f"Código: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}"
                producto_label = Label(producto4, text=producto_texto)
                producto_label.configure(bg='light cyan')
                producto_label.pack()
        else:
            mensaje_vacio = Label(producto4, text="No hay productos en este menú.")
            mensaje_vacio.configure(bg='light cyan')
            mensaje_vacio.pack()

    ip=Button(menuproduct, text="1.Ingresar un producto nuevo",command=producto1, background="light goldenrod",font=fuenteboton).pack()
    sp1=Label(menuproduct)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(menuproduct, text="2.Modificar un producto existente",command=producto2, background="light goldenrod",font=fuenteboton).pack()
    sp1=Label(menuproduct)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(menuproduct, text="3.Eliminar un producto",command=producto3, background="light goldenrod",font=fuenteboton).pack()
    sp1=Label(menuproduct)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(menuproduct, text="4.Visualizar productos existente",command=producto4, background="light goldenrod",font=fuenteboton).pack()


    menuproduct.mainloop()

def abrir_ventana4():
    ventanai.withdraw()  # Oculta la ventana de inicio
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



def abrir_ventana5():
    def abrir_sitio_web(url):
        webbrowser.open_new(url)
        
    proveedores = {
    "Bimbo": {
        "Nombre": "Bimbo",
        "Dirección": "Bimbo De Centroamerica S.A.. 9 Calle 2-52 Zona 3 Mixco Colo EL Rosario Guatemala",
        "Teléfono": "1-800-8350193",
        "Email": "servicioalcliente@grupobimbo.com",
        "Sitio Web": "https://www.grupobimbo.com/",
    },
    "Maseca": {
        "Nombre": "Maseca",
        "Dirección": "Km. 32 1/2 Ruta Antigua Guatemala, Aldea LO de Coy",
        "Teléfono": "987-654-3210",
        "Email": "proveedor2@example.com",
        "Sitio Web": "https://www.gruma.com/es/nuestras-marcas/localiza-una-marca/maseca.aspx",
    },
    "Coca Cola": {
        "Nombre": "Coca cola",
        "Dirección": "26 Calle, Zona 11, Guatemala",
        "Teléfono": "1-800-743-6773",
        "Email": "consumidor@coca-cola.com",
        "Sitio Web": "https://journey.coca-cola.com/inicio-gt"
    },
    "Pepsi": {
        "Nombre": "Pepsi",
        "Dirección": "JF95+9P4, y, Calz. San Juan & Calle De San Juan Sacatepequez, Ciudad de Guatemala",
        "Teléfono": "1-800-743-6773",
        "Email": "consumidores.1800@pepsico.com",
        "Sitio Web": "https://www.pepsi.com/"
    }
}

    def abrir_sitio_web(url):
        webbrowser.open_new(url)

    def mostrar_proveedores(root):
        root.withdraw()
        
        proveedores_window = tk.Toplevel()
        proveedores_window.title("Proveedores")
        proveedores_window.geometry("400x400")
        
        for proveedor_nombre in proveedores:
            button = tk.Button(proveedores_window, text=proveedor_nombre, command=lambda name=proveedor_nombre: mostrar_informacion_proveedor(name, proveedores_window))
            button.pack(pady=10, padx=20)
        
        regresar_button = tk.Button(proveedores_window, text="Regresar al Menú Principal", command=lambda: volver_al_menu_principal(root, proveedores_window))
        regresar_button.pack()

    def mostrar_informacion_proveedor(proveedor_nombre, proveedores_window):
        proveedores_window.withdraw()
        
        info_window = tk.Toplevel()
        info_window.title("Información del Proveedor")
        info_window.geometry("800x400")

        proveedor_info = proveedores.get(proveedor_nombre, {})
        for key, value in proveedor_info.items():
            if key == "Sitio Web":
                label_sitio_web = tk.Label(info_window, text=f"{key}: {value}", fg="blue", cursor="hand2")
                label_sitio_web.bind("<Button-1>", lambda event, url=value: abrir_sitio_web(url))
                label_sitio_web.pack()
            else:
                label = tk.Label(info_window, text=f"{key}: {value}")
                label.pack()

        regresar_button = tk.Button(info_window, text="Regresar a la lista de Proveedores", command=lambda: volver_a_lista_proveedores(proveedores_window, info_window))
        regresar_button.pack()

    def volver_a_lista_proveedores(proveedores_window, info_window):
        info_window.destroy()
        proveedores_window.deiconify()

    def volver_al_menu_principal(root, proveedores_window):
        proveedores_window.destroy()
        root.deiconify()

def abrir_ventana6():
    ventanai.withdraw()  # Oculta la ventana de inicio

    # Código de la ventana de inventario
    ventana6 = Toplevel()
    ventana6.title("Inventario FASTFOOD")
    ventana6.geometry("700x450")
    ventana6.configure(bg='lightblue')

def Clientes():
    root = Tk()
    root.title("Clientes FASTFOOD")
    root.geometry("600x450")
    root.configure(bg='lightpink')

    codigo = StringVar()
    nombre = StringVar()
    nit = StringVar()
    telefono = StringVar()
    edad = StringVar()

    def conecClientes():
        conexion = sqlite3.connect("Clientes.db")
        cursorCL = conexion.cursor()
        try:
            cursorCL.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50) NOT NULL,
            NIT VARCHAR(50) NOT NULL,
            TELEFONO INT NOT NULL,
            EDAD INT NOT NULL
        )
    ''')
            messagebox.showinfo("CONEXIÓN", "BASE DE DATOS CREADA")
        except:
            messagebox.showinfo("CONEXIÓN", "Conexión realizada")

    def eliminarbd():
        conexion = sqlite3.connect("Clientes.db")
        cursorCL = conexion.cursor()
        if messagebox.askyesno(message="¿Está seguro que desea borrar?", title="ADVERTENCIA"):
            cursorCL.execute("DROP TABLE IF EXISTS Clientes")
            conexion.commit()
        else:
            pass
        limpiar()
        seleccionar()

    def exit():
        valor = messagebox.askquestion("Salir", "¿List@ para salir?")
        if valor == "yes":
            root.destroy()

    def limpiar():
        codigo.set("")
        nombre.set("")
        nit.set("")
        telefono.set("")
        edad.set("")

    def mensaje():
        mensaje = '''
        Los datos del cliente
        están siendo ingresados 
        '''
        messagebox.showinfo("Mensaje", mensaje)

    def insertar():
        conexion = sqlite3.connect("Clientes.db")
        cursorCL = conexion.cursor()
        try:
            datos = nombre.get(), nit.get(), telefono.get(), edad.get() 
            cursorCL.execute("INSERT INTO Clientes VALUES (NULL,?,?,?,?)", (datos))
            conexion.commit()
        except:
            messagebox.showwarning("Cuidado", "Blanky") 
            pass
        limpiar()
        seleccionar()

    def seleccionar():
        conexion = sqlite3.connect("Clientes.db")
        cursorCL = conexion.cursor()
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            cursorCL.execute("SELECT * FROM Clientes")
            for row in cursorCL:
                tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4]))
        except:
            pass

    tree = ttk.Treeview(height=12, columns=('#0', '#1', '#2', '#3'))
    tree.place(x=0, y=130)
    tree.column('#0', width=120)
    tree.heading('#0', text="CODIGO", anchor=CENTER)
    tree.column('#1', width=120)
    tree.heading('#1', text="Nombre", anchor=CENTER)
    tree.column('#2', width=120)
    tree.heading('#2', text="NIT", anchor=CENTER)
    tree.column('#3', width=120)
    tree.heading('#3', text="Telefono", anchor=CENTER)
    tree.column('#4', width=120)
    tree.heading('#4', text="Edad", anchor=CENTER)

    def seleccion(event):
        item = tree.focus()
        codigo.set(tree.item(item, "text"))
        nombre.set(tree.item(item, "values")[0])
        nit.set(tree.item(item, "values")[1])
        telefono.set(tree.item(item, "values")[2])
        edad.set(tree.item(item, "values")[3])
    tree.bind("<Double-1>", seleccion)

    def cambiar():
        conexion = sqlite3.connect("Clientes.db")
        cursorCL = conexion.cursor()
        try:
            datos = nombre.get(), nit.get(), telefono.get(), edad.get()
            cursorCL.execute("UPDATE Clientes SET NOMBRE=?, NIT=?, TELEFONO=?, EDAD=? WHERE CODIGO="+codigo.get(), (datos))
            conexion.commit()
        except:
            messagebox.showwarning("ALERTA", "SE ENCONTRO UN ERROR")
            pass
        limpiar()
        seleccionar()

    def borrar():
        conexion = sqlite3.connect("Clientes.db")
        cursorCL = conexion.cursor()
        try:
            if messagebox.askyesno(message="¿Está seguro que desea borrar?", title="ADVERTENCIA"):
                cursorCL.execute("DELETE FROM Clientes WHERE CODIGO="+codigo.get())
                conexion.commit()
        except:
            messagebox.showwarning("ALERTA", "SE ENCONTRO UN ERROR")
            pass
        limpiar()
        seleccionar()

    menucli = Menu(root)
    menubonito = Menu(menucli, tearoff=0)
    menubonito.add_command(label="Crear o conectar Base de Datos", command=conecClientes)
    menubonito.add_command(label="ELIMINAR BASE DE DATOS", command=eliminarbd)
    menubonito.add_command(label="Salir", command=exit)
    menucli.add_cascade(label="Inicio", menu=menubonito)

    e1 = Entry(root, textvariable=codigo)

    l2 = Label(root, text="Nombre", background="yellow")
    l2.place(x=50, y=10)
    e2 = Entry(root, textvariable=nombre, width=28)
    e2.place(x=100, y=10)

    l6 = Label(root, text="NIT", background="yellow")
    l6.place(x=30, y=40)
    e6 = Entry(root, textvariable=nit, width=15)
    e6.place(x=100, y=40)

    l4 = Label(root, text="Telefono", background="yellow")
    l4.place(x=280, y=10)
    e4 = Entry(root, textvariable=telefono, width=15)
    e4.place(x=370, y=10)

    l5 = Label(root, text="Edad", background="yellow")
    l5.place(x=280, y=40)
    e5 = Entry(root, textvariable=edad, width=15)
    e5.place(x=370, y=40)

    l7 = Label(root, text="Bienvenido a Clientes", background="light pink")
    l7.place(x=480, y=40)

    # botones
    b1 = Button(root, text="Crear Cliente", command=insertar, background="orange")
    b1.place(x=50, y=90)

    b2 = Button(root, text="Modificar Cliente", command=cambiar, background="orange")
    b2.place(x=180, y=90)

    b3 = Button(root, text="Mostrar Clientes", command=seleccionar, background="orange")
    b3.place(x=340, y=90)

    b4 = Button(root, text="Borrar", command=borrar, background="orange")
    b4.place(x=500, y=90)

    root.config(menu=menucli)

    root.mainloop()
#-----------------------------------------------------FIN CLIENTES-------------------------------------------------------


def abrir_ventana7():
    def reportep():
        anexo=sqlite3.connect('producto')
        cursor1= anexo.cursor()
        def mostrar():
            cursor1.execute("SELECT codigo, nombre FROM MENU WHERE categoria = ?", (categoria.get(),))
            productos = cursor1.fetchall()
            if productos:
                for producto in productos:
                    producto_texto = f"Código: {producto[0]}, Nombre: {producto[1]}"
                    producto_label = Label(reportep, text=producto_texto)
                    producto_label.configure(bg='light cyan')
                    producto_label.pack()
            else:
                mensaje_vacio = Label(reportep, text="No hay productos en esta categoria.")
                mensaje_vacio.configure(bg='light cyan')
                mensaje_vacio.pack()

        reportep = Toplevel()
        reportep.title("Productos en el Menú")
        reportep.geometry("400x500")
        reportep.configure(bg='light cyan')

        rep = Label(reportep, text="Ingrese Qué categoría desea Visualizar:\n\n1.Hamburguesa\n2.Pizza\n3.Pollo frito\n4.Ensaladas\n5.Bebidas\n6.Postres\n7.Acompañamientos\n8.Infantil\n")
        rep.configure(bg='light cyan')
        rep.pack()
        
        categoria = Entry(reportep)
        categoria.pack()

        rp = Button(reportep, text="VISUALIZAR", command=mostrar)
        rp.pack()
        
    def reportfact():
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

    ventanai.withdraw()
    fuentetitulo=('Helvetica',20)
    fuenteboton=('Verdana',10)

    reportes = Tk()
    reportes.title("REPORTES")
    reportes.geometry("700x450")
    reportes.configure(bg='white')

    S1=Label(reportes, text="BIENVENIDO AL APARTADO DE REPORTES", font=fuentetitulo)
    S1.configure(bg='white')
    S1.pack()
    s2=Label(reportes,text="Porfavor digame que es lo que desea ver")
    s2.configure(bg='white')
    s2.pack()
    s3=Label(reportes)
    s3.configure(bg='white')
    s3.pack()


    ip=Button(reportes, text="1.Listado de clientes", background="light goldenrod",font=fuenteboton).pack()
    sp1=Label(reportes)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(reportes, text="2.Listado de Proveedores",background="light goldenrod",font=fuenteboton).pack()
    sp1=Label(reportes)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(reportes, text="3.Listado de productos", background="light goldenrod",command=reportep,font=fuenteboton).pack()
    sp1=Label(reportes)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(reportes, text="4.Listado de Precios", background="light goldenrod",font=fuenteboton).pack()
    sp1=Label(reportes)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(reportes, text="Listado de Facturacion", background="light goldenrod",command=reportfact,font=fuenteboton).pack()
    sp1=Label(reportes)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(reportes, text="Impresion de factura", background="light goldenrod",font=fuenteboton).pack()
    sp1=Label(reportes)
    sp1.configure(bg='white')
    sp1.pack()
    ip=Button(reportes, text="Listado de Ingresos o ventas por dia", background="light goldenrod",font=fuenteboton).pack()

ventanai = Tk()
ventanai.geometry("550x550")
ventanai.title("INICIO")

Button(ventanai, text="Ir a inventario", width=50, command=abrir_ventana2).pack(pady=30)
Button(ventanai, text="Ir a produtos", width=50, command=abrir_ventana3).pack(pady=30)
Button(ventanai, text="Ir a facturación", width=50, command=abrir_ventana4).pack(pady=30)
Button(ventanai, text="Ir a proveedores", width=50, command=abrir_ventana5).pack(pady=30)
Button(ventanai, text="Ir a clientes", width=50, command=Clientes).pack(pady=30)
Button(ventanai, text="Ir a reportes", width=50, command=abrir_ventana7).pack(pady=30)

ventanai.mainloop()