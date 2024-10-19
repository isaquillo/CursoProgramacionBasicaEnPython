
# # Tarea 4

# # for i in range(10,20,2):
# #     print(i)


# num1 = 2
# num2 = 4

# # print(num1 + num2)

# palabra1 = "2"
# palabra2 = " Mundo"

# # print(palabra1 + palabra2)

# print(num1 + int(palabra1))


edades = [20, -3, -200, 7, 45, 1, 16, 432, 175, 60, 55, 8, 77, 28, 21, 45, 16]
"""
Recorrer la lista e imprimir de acuerdo con la edad
"Niño" si es menor o igual a 11
"Adolescente" si es mayor o igual a 12 y menor o igual que 16
"Joven" si es mayor o igual que 18 y menor o igual que 29
"Adulto" si es mayor o igual que 30 y menor o igual que 59
"Adulto mayor" si es mayor o igual que 60

Validar que la edad esté dentro del rango de 1 a 130
print("Edad fuera del rango válido)

"""
for edad in edades:
    print(str(edad) + " - ", end="")
    if edad >= 1 and edad <= 130:
        if edad <= 11:
            print ("Niño")
        elif edad >= 12 and edad <= 16:
            print ("Adolescente")
        elif edad >= 18 and edad <= 29:
            print ("Joven")
        elif edad >= 30 and edad <= 59:
            print ("Adulto")
        elif edad >= 60 and edad <= 130:
            print ("Adulto Mayor")
    else:
        print("Edad fuera del rango válido")