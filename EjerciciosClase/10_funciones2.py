"""
Las funciones que reciben parámetros lo hacen por valor o referencia

Paso por valor: Reciben únicamente el valor de la variable
Esto significa que las modificaciones que se hagan en esa variable
no se reflejarán en la variable original

Paso por referencia: Reciben la ubicación en memoria de la variable
Esto significa que los cambios que se hagan en la variable
se reflejarán en la variable original

"""


# Paso de parámetros por valor
a = 3
b = 4

def suma(a,b):
    a = a + b
    print("Valor de a en la función: " + str(a))

suma(a,b) # Paso de variables por valor
print("Valor de a fuera de la función: " + str(a))


#  Paso de parámetros por referencia
calificaciones = [100, 90, 80] # Los objetos siempre se pasan por referencia

def modificar_calificaciones(calificaciones):
    # calificaciones.append(100)
    otras_calificaciones = calificaciones.copy()
    otras_calificaciones.append(100)
    print("Calificaciones dentro de la función: " + str(otras_calificaciones))

modificar_calificaciones(calificaciones)
print("Calificaciones fuera de la función: " + str(calificaciones))



# Funciones definidas por el usuario y funciones predefinidas
# Funciones que nosotros definimos
# Funciones predefinidas son las que vienen incluidas en el lenguaje



