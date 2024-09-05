nombre= (input("Ingrese su nombre: ")) 
apellido= (input("Ingrese su apellido: "))
nit= int(input("Ingrese su nit: "))
direccion= (input("Ingrese su direccion: "))
num_telefonico= int(input("Ingrese su numero de telefono: "))
genero = None  

while genero not in [1, 2, 3, 4]:
    try:
        genero = int(input('''Genero:
                           1. Femenino
                           2. Masculino
                           3. Otros
                           4. Juan
                           Elija una opción: '''))
    except ValueError:
        print("Por favor, ingrese un número válido.")

if genero == 1:
    print("Femenino")
elif genero == 2:
    print("Masculino")
elif genero == 3:
    LGTV=(input("Definase entre los mas de 200,000 generos existentes: "))
elif genero == 4:
    print("Juan")
   


