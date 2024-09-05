numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 != 0:
    division = numero1 / numero2
    resto = numero1 % numero2
else:
    division = "No se puede dividir por cero"
    resto = "No se puede dividir por cero"
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Resto de la división:", resto)