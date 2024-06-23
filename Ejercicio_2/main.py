def ordenar_con_criterios(entry, criteria):
    """
    Ordena los elementos de la lista 'entry' según los criterios especificados en 'criteria'.

    Primero filtra los elementos que cumplen con todos los criterios dados en 'criteria',
    luego ordena estos elementos filtrados por la propiedad 'priority' en orden descendente.
    Finalmente, coloca los elementos que no cumplen con los criterios al final del resultado,
    manteniendo su orden original.

    Args:
    entry (list): Lista de diccionarios representando los elementos a ordenar.
    criteria (list): Lista de tuplas que especifican los criterios de filtrado. Cada tupla tiene
                     tres elementos: (propiedad, operador, valor).

    Returns:
    list: Lista de diccionarios ordenada según los criterios especificados.
    """
    # Filtrar los elementos que cumplen con los criterios especificados
    filtered = []
    for elem in entry:
        cumple_criterios = True
        for crit in criteria:
            prop = crit[0]
            operador = crit[1]
            valor = crit[2]
            if operador == '=':
                cumple_criterios = cumple_criterios and elem[prop] == valor
            elif operador == '>=':
                cumple_criterios = cumple_criterios and elem[prop] >= valor
            elif operador == '<=':
                cumple_criterios = cumple_criterios and elem[prop] <= valor
            else:
                # Manejar otros operadores según sea necesario
                pass
        
        if cumple_criterios:
            filtered.append(elem)
    
    # Ordenar manualmente los elementos filtrados por la propiedad 'priority' en modo descendente
    filtered_sorted = ordenamiento_manual(filtered, 'priority', reverse=True)
    
    # Mantener los elementos que no cumplen con los criterios en su posición original
    non_filtered = [elem for elem in entry if elem not in filtered]
    
    # Combinar los resultados: elementos filtrados ordenados al principio y elementos no filtrados al final
    result = filtered_sorted + non_filtered
    
    return result

def ordenamiento_manual(arr, key, reverse=False):
    """
    Implementación de ordenamiento manual por una clave 'key' en una lista de diccionarios 'arr'.
    
    Args:
    arr (list): Lista de diccionarios que se desea ordenar.
    key (str): Clave por la cual ordenar cada diccionario en 'arr'.
    reverse (bool, optional): Indica si el ordenamiento debe ser descendente (True) o ascendente (False). Default es False.
    
    Returns:
    list: Lista de diccionarios ordenados según la clave especificada.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (not reverse and arr[j][key] > arr[j + 1][key]) or (reverse and arr[j][key] < arr[j + 1][key]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
     # Ejemplo de entrada: lista de elementos con propiedades
    entry = [
        {'id': 12340, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 125, 'priority': 2},
        {'id': 12341, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 127, 'priority': 4},
        {'id': 12342, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 129, 'priority': 6},
        {'id': 12343, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 131, 'priority': 0},
        {'id': 12344, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 133, 'priority': 0},
        {'id': 12345, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 135, 'priority': 0},
        {'id': 12346, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 137, 'priority': -1},
        {'id': 12347, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 139, 'priority': 0},
        {'id': 12348, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 141, 'priority': 2},
        {'id': 12349, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 143, 'priority': 0},
        {'id': 12350, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost': 145, 'priority': 0},
        {'id': 12351, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost': 147, 'priority': 10},
        {'id': 12352, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost': 149, 'priority': 0},
        {'id': 12353, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost': 151, 'priority': 0},
        {'id': 12354, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost': 153, 'priority': 0},
        {'id': 12355, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost': 155, 'priority': 0},
        {'id': 12356, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost': 157, 'priority': 0},
        {'id': 12357, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost': 159, 'priority': 0},
        {'id': 12358, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost': 161, 'priority': 0},
        {'id': 12359, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost': 135, 'priority': 0},
        {'id': 12360, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 137, 'priority': 0},
        {'id': 12361, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 139, 'priority': 0},
        {'id': 12362, 'weight': 3, 'width': 3, 'height': 1, 'length': 10, 'cost': 141, 'priority': -2},
        {'id': 12363, 'weight': 3, 'width': 3, 'height': 1, 'length': 10, 'cost': 153, 'priority': -2},
        {'id': 12364, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 145, 'priority': -6},
        {'id': 12366, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 147, 'priority': 0},
        {'id': 12367, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 149, 'priority': 0},
        {'id': 12365, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 151, 'priority': 2},
        {'id': 12368, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 181, 'priority': 2},
        {'id': 12369, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 183, 'priority': 0},
    ]
    
    # Criterio de filtrado
    criteria2 = [
        ('weight', '=', 3),
        ('width', '=', 3),
    ]
    
    # Llamar a la función para ordenar según los criterios especificados
    resultado = ordenar_con_criterios(entry, criteria2)
    
    # Mostrar el resultado
    print("Resultado después de ordenar con criterios:")
    for elem in resultado:
        print(elem)

if __name__ == "__main__":
    main()