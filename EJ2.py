# Defina una función recursiva que reciba una lista para determinar cuántos numeros pares hay en ella

def how_many_pair(lista, c=0):
    if len(lista) == 0:
        return c
    else:
        if (lista[0] % 2) == 0:
            c += 1
            return how_many_pair(lista[1:], c)
        else:
            return how_many_pair(lista[1:], c)


print(how_many_pair([1, 22, 3, 41, 5, 6, 7, 8, 9, 105, 25067854632]))
