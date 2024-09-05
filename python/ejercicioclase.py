def calcula_media_desviacion(*args):
    total = 0
    for i in args:
        total += i
    media = total / len(args)
    
    total = 0 
    for i in args:
        total += (i - media) ** 2 
    
    desviacion = (total / len(args)) ** 0.5
    
    return media, desviacion

a, b, c, d = 3, 5, 10, 12
media, desviacion_tipica = calcula_media_desviacion(a, b, c, d)
print(f"Datos: {a}, {b}, {c}, {d}")
print(f"Media: {media}")
print(f"Desviacion tipica: {desviacion_tipica}")
print("Programa terminado")