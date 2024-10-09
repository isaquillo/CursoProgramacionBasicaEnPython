"""
Clase: 05 Control de Flujo
Fecha: 04 de Octubre 2024
"""


# Condicionales

edad = 20

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")
else:
    print("Eres menor de edad")
    print("Ni modo!")
    


calificacion = 80.0

if calificacion >= 90:
    print("Muy bien")
elif calificacion >= 80:
    print("Bien")
elif calificacion >= 70:
    print("Regular")
elif calificacion >= 60:
    print("De panzazo")
else:
    print("Reprobado")


# Ciclos (for y while)

# Utilizaremos una lista
# Una lista es una colección de elementos de cualquier tipo
# El for se utiliza especialmente cuando ya sabemos cuántas veces
# deberá repetirse el ciclo

animales = ["perro", "gato", "rata", "gallo"]
# numeros = [1,2,3]
calificaciones = [80, 90, 100, 50]

suma = 0
for calificacion in calificaciones:
    suma += calificacion

promedio = suma / len(calificaciones)
print(promedio)

# Ciclo for para iterar (recorrer) sobre una colección de elementos

mensaje = " es mi animal favorito"
for animal in animales:
    print("El " + animal + mensaje)

# Ciclo for para iterar sobre un rango de números
for i in range(5,101,5):
    print(i)


# Ciclo while
# Se utiliza para repetir intrucciones mientras se cumpla una condición
# Se usa cuando no se sabe de antemano cuántas veces se ejecutará el ciclo
# Es importante evitar los bucles infinitos

edad = 14

while edad >= 12 and edad <=17:
    print(f"Tienes {edad}. Eres un adolescente")





