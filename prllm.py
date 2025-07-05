def quicksort(lista):
    # Caso base: listas vacías o de un solo elemento ya están ordenadas
    if len(lista) <= 1:
        return lista
    else:
        # Elegimos un pivote (aquí el primero)
        pivote = lista[0]

        # Creamos dos listas:
        # - menores: elementos menores o iguales al pivote
        # - mayores: elementos mayores al pivote
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]

        # Aplicamos QuickSort recursivamente y combinamos
        return quicksort(menores) + [pivote] + quicksort(mayores)


# Ejemplo de uso
numeros = [33, 10, 55, 71, 29, 3, 18]
print("Lista original:", numeros)

ordenados = quicksort(numeros)
print("Lista ordenada:", ordenados)
