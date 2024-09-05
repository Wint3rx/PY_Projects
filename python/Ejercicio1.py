def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

rango_inicial = 1
rango_final = 100

print(f"Números primos en el rango del {rango_inicial} al {rango_final}:")
for numero in range(rango_inicial, rango_final + 1):
    if es_primo(numero):
        print(numero)