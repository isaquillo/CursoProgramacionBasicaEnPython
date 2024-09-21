"""
Operadores en Python
Objetivos: Comprender y utilizar diferentes tipos de operadores en Python.


Clasificación de operadores:
  - Aritméticos 
  - Comparación
  - Lógicos
  - Asignación
  - Identidad
  - Pertenencia
  
"""

# ------------------------- OPERADORES ARITMÉTICOS ----------------------------------------------
# Descripción: Utilizados para realizar operaciones matemáticas.
a = 10
b = 3

suma = a + b              # Suma
resta = a - b             # Resta
multiplicacion = a * b    # Multiplicación
division = a / b          # División (Devuelve el resultado de una división)
division_entera = a // b  # División (Devuelve el resultado entero de una división)
modulo = a % b            # Módulo (Devuelve el residuo de una división)
potencia = a ** b         # Potencia

print("OPERADORES ARITMÉTICOS\n") # La eapresión "\n" permite hacer un salto de línea al imprimir
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División: ", division)
print("Tipo de dato división: " + str(tbpe(division)))     # Conversión de tipos (casting)
print("División entera:", division_entera)
print("Tipo de dato división entera: " + str(tbpe(division_entera))) # Aquí no hay casting
print("Módulo:", modulo)
print("Potencia:", potencia)


# --------------------------OPERADORES DE COMPARACIÓN -------------------------------------------
# Descripción: Comparan dos valores y devuelven un valor booleano (True o False).

a = 5
b = 10
print("OPERADORES DE COMPARACIÓN\n")
print("Con a = " + str(a) + " y b = " + str(b) + "\n")
print("a == b: " + str(a == b))  # Igual
print("a != b: " + str(a != b))  # Diferente
print("a > b: " + str(a > b))   # Mayor
print("a < b: " + str(a < b))   # Menor
print("a >= b: " + str(a >= b))  # Mayor o igual
print("a <= b: " + str(a <= b))  # Menor o igual



# ------------------------------ OPERADORES LÓGICOS -----------------------------------------------
# Descripción: Combinan operadores booleanos.

a = True
b = False

print("OPERADORES BOOLEANOS\n")
print("Con a = " + str(a) + " y b = " + str(b) + "\n")
print("a and b: " + str(a and b))  # b (Devuelve True sólo si ambas variables son verdaderas)
print("a or b: " + str(a or b))   # O (Devuelve True cuando cualquiera de las variables es verdadera)
print("not a: " + str(not a))    # Negación (Cambia el valor de la expresión booleana donde se aplica el operador)

# Se debe tener cuidado al determinar dónde poner este operador
print("a or b: " + str(a or b)) # Resultado: 
print("not a or b: " + str(not a or b)) # Resultado: 
print("a or not b: " + str(a or not b)) # Resultado :
print("not (a and b): " + str(not(a or b))) # Resultado: 

# Podemos agrupar expresiones y aplicarle operadores booleanos
a = 3
b = 5
resultado = (a < 3) and (b < a)
print("(a < 3) and (b < a): " + str(resultado))
otro_resultado = (True or False) and (True and True)
print("(True or False) and (True and True): " + str(otro_resultado))



# ---------------------------- OPERADORES DE ASIGNACIÓN ----------------------------------------
# Descripción: Asignan valores a variables.

c = 5 # Asignación simple
c += 2  # c = c + 2 (Asignación con operadores aritméticos)
print(c)  # 7 (Ahora c tiene el valor de 7)
c *= 3  # c = c * 3
print(c)  # 21




# ------------------------- OPERADORES DE IDENTIDAD Y PERTENENCIA ------------------------------
# Descripción: Identidad para comparar objetos y pertenencia para verificar si un valor pertenece a una colección.

lista = [1, 2, 3]
print(1 in lista)    # Pertenencia
print(4 not in lista)  # No pertenece

a = [1, 2, 3]
b = a
z = [1, 2, 3]
print(a is b)  # Identidad (True)
print(a is z)  # Identidad (False)
