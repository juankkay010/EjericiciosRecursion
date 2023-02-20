# Defina una función recursiva para determinar la cantidad de elementos en una lista l

def count_elements(lista: list, c=0):
    if len(lista) == 0:
        return c
    else:
        c += 1
        return count_elements(lista[1:], c)


print(count_elements([1, 2, 3, True, "Hola"]))


