nombre= (input("Ingrese su nombre: "))
antiguedad= int(input("Ingrese sus anios laborando en la empresa: "))
sueldo = int(input("Ingrese su sueldo: "))
bono= None
if antiguedad <= 6:
 bono= (sueldo *7) / 100
 print (f"su bono es: {bono}")
elif 6 < antiguedad < 12:
 bono= (sueldo * 10) / 100
 print (f"su bono es: {bono}")
elif antiguedad >= 12:
 bono= (sueldo * 15) / 100
 print (f"su bono es: {bono}")
sueldo_total= sueldo + bono
print (nombre)
print (f"su bono es: {bono}")
print (f"su sueldo mas el bono es: {sueldo_total}")