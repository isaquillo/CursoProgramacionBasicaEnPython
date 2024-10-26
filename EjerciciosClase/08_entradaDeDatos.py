"""
La entrada de datos nos permite introducir información de parte del usuario
y, por lo tanto, nos permite desarrollar programas interactivos
"""
# -----------------INTRODUCIENDO TEXTO---------------

# nombre = ""
# nombre = input("Dame tu nombre: ")
# print("Hola " + nombre)

# -----------------INTRODUCIENDO NÚMEROS--------------

# numero = float(input("Dame un número decimal: "))
# print("El número es: " + numero)
# print(numero + 5)

# -----------------INTRODUCIENDO DATOS EN UNA LISTA------------
# Calcular el promedio de 3 calificaciones de un alumno

calificaciones = []
# 1) Introducir datos en la lista
# Una forma de hacerlo (con for i in range)
for i in range(3):
    calificaciones.append(float(input("Introduce la calificación #" + str(i+1) +": ")))

# Otra forma (con while)
# contador = 1
# while(contador <= 3):
#     calificaciones.append(float(input("Introduce la calificación #" + str(contador) +": ")))
#     contador += 1
# print(calificaciones)

# y otra forma (con while(True))
# contador = 0
# while(True):
#     if(contador==3):
#         break
#     calificaciones.append(float(input("Introduce la calificación #" + str(contador + 1) +": ")))
#     contador += 1

# 2) Sumar todas las calificaciones
# utilizando for (for-each "por cada uno")
suma = 0
for calificacion in calificaciones:
    suma += calificacion
    # suma = suma + calificacion

# 3) Promedio: Dividir la suma entre el número de calificaciones
promedio = suma / len(calificaciones)

# 4) Mostrar el resultado
print("El promedio es: " + str(promedio))
