"""
Las funciones son bloques de código reutilizable
Permiten modularizar un programa
Permiten usar la técnica "divide y vencerás" al enfrentar un problema
"""
# Definición de la función
# def sumar(num1, num2):
#     print(num1 + num2)

# # Invocar la función (llamar)
# sumar(5, 10)

# Valores por defecto en una función
# Cuando se llama a la función sin argumentos, la función tomará
# los valores por defecto que se hayan definido
def multiplicar(num1 = 4, num2 = 5):
    print(num1 * num2)

multiplicar(10, 10)

# ----------EJERCICIO----------
# Calcular el promedio de calificaciones de un alumno

# Introducir datos en una lista
def introducir_calificaciones(num):
    calificaciones = []
    for i in range(num):
        calificaciones.append(float(input("Introduce la calificación #" + str(i+1) +": ")))
    return calificaciones


# Sumar todas las calificaciones
def sumar_calificaciones(calificaciones):
    suma = 0 # Generalmente comienza en 0
    for calificacion in calificaciones:
        suma += calificacion
    return suma

# Calcular el promedio
def calcular_promedio(suma, num_elementos):
    promedio = suma / num_elementos
    return promedio
    

# Mostrar el resultado en pantalla
def imprimir_resultado(resultado):
    print("El resultado es: " + str(resultado))


# Invocar las funciones
calificaciones = introducir_calificaciones(3)
suma = sumar_calificaciones(calificaciones)
promedio = calcular_promedio(suma, len(calificaciones))
imprimir_resultado(promedio)


