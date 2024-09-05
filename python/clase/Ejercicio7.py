segundos = int(input("Ingrese el tiempo en segundos: "))
horas = segundos // 3600  # Obtener las horas completas
segundos_restantes = segundos % 3600  # Calcular los segundos restantes
minutos = segundos_restantes // 60
segundos_restantes = segundos_restantes % 60
tiempo_en_horas = horas + minutos / 60 + segundos_restantes / 3600
print(f"El tiempo es de {tiempo_en_horas:.2f} horas")
