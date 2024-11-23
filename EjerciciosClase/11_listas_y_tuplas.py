# Listas
# Colección ordenada de datos de cualquier tipo

lista = [1,5, "hola"]
lista.append(6)
print(lista)
lista[0] = 8
print(lista)

# Operaciones con listas
lista.clear()
print(lista)
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(1)
print(lista)

print(lista.count(1))

print(lista.index(1))

# copiar lista

otra_lista = lista

otra_lista = lista.copy()
otra_lista.clear()

print("Impresión de valores en las listas")
print(otra_lista)
print(lista)

# slicing
sublista = lista[:]

print("sublista: " + str(sublista))

# Tuplas
# Colección ordenada de datos de cualquier tipo que no puede ser modificada
tupla = (1,5, "hola")
tupla[0] = 8
print(tupla)


# Ejercicio con lista y tupla

lista_compras = []


# Menú interactivo

while True:
    print("----Lista de compras----")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Mostrar lista")
    print("4. Terminar compra")
    print("0. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        item = input("¿Qué quieres agregar?: ")
        lista_compras.append(item)
        print(f"'{item}' ha sido agregado")
    elif opcion == 2:
        item = input("¿Qué quieres eliminar?: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' ha sido eliminado")
        else:
            print(f"'{item}' no está en la lista")
    elif opcion == 3:
        print("Lista actual\n")
        for i, elemento in enumerate(lista_compras, start=1):
            print(f"{i}. {elemento}")
    elif opcion == 4:
        tupla = tuple(lista_compras)
        print("Lista de compras final\n")
        for i, elemento in enumerate(tupla, start=1):
            print(f"{i}. {elemento}")
        break
    elif opcion == 0:
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo")
