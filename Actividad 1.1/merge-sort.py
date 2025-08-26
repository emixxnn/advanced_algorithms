# Emiliano Nuñez Félix A01645413
# Sergio Santiago Sánchez Salazar A01645255

def merge_sort(lista):
    # si la lista tiene 1 elemento o menos, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    
    # ordenar ambas mitades recursivamente
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)
    
    # combinar las dos mitades ordenadas
    return merge(izquierda_ordenada, derecha_ordenada)


def merge(lista1, lista2):
    # combinar dos listas ordenadas en una sola lista ordenada
    resultado = []
    while lista1 and lista2:
        # comparar los primeros elementos de ambas listas y agregar el menor a la lista resultado
        if lista1[0] <= lista2[0]:
            resultado.append(lista1[0])
            lista1.pop(0)
        # si el primer elemento de lista2 es menor, agregarlo a la lista resultado
        else:
            resultado.append(lista2[0])
            lista2.pop(0)
        
    # agregar los elementos restantes de lista1 o lista2
    resultado.extend(lista1)    
    resultado.extend(lista2)

    return resultado


