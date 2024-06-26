def convertir_a_minusculas(texto):
    """
    Convierte una cadena de texto a minúsculas.
    
    Args:
    texto (str): La cadena de texto que se desea convertir.
    
    Returns:
    str: La cadena de texto convertida a minúsculas.
    """
    minusculas = ""
    for caracter in texto:
        # Convertir caracteres de 'A' a 'Z' a sus equivalentes en minúsculas
        if 'A' <= caracter <= 'Z':
            minusculas += chr(ord(caracter) + 32)
        else:
            minusculas += caracter
    return minusculas

def es_alfanumerico(caracter):
    """
    Verifica si un carácter es alfanumérico.
    
    Args:
    caracter (str): El carácter que se desea verificar.
    
    Returns:
    bool: True si el carácter es alfanumérico, False en caso contrario.
    """
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z') or ('0' <= caracter <= '9')


def contar_palabra(palabra, parrafo):
    """
    Cuenta el número de veces que una palabra aparece en un párrafo.

    Args:
    palabra (str): La palabra que se desea contar.
    parrafo (str): El párrafo en el que se desea contar la palabra.

    Returns:
    int: El número de veces que la palabra aparece en el párrafo.
    """
    # Convertir todo el texto a minúsculas para una búsqueda no sensible a mayúsculas/minúsculas
    palabra = convertir_a_minusculas(palabra)
    parrafo = convertir_a_minusculas(parrafo)

    # Inicializar el contador
    contador = 0
    palabra_len = len(palabra)
    parrafo_len = len(parrafo)
    index = 0

    while index <= parrafo_len - palabra_len:
        # Verificar si el fragmento actual del párrafo coincide con la palabra
        if parrafo[index:index + palabra_len] == palabra:
            # Verificar si la coincidencia es una palabra completa
            if (index == 0 or not es_alfanumerico(parrafo[index - 1])) and (index + palabra_len == parrafo_len or not es_alfanumerico(parrafo[index + palabra_len])):
                contador += 1
            index += palabra_len
        else:
            index += 1

    return contador


def main():
    """
    Función principal que usa el párrafo de ejemplo y la palabra a buscar para contar sus ocurrencias.
    """
    # Párrafo de ejemplo
    parrafo = """
    La logística Digital es un concepto que surge de la integración entre la logística tradicional y
    la era digital. Con el auge del correo electrónico y las descargas digitales reemplazando
    productos físicos, podríamos estar hablando de un golpe devastador para la industria de la
    logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la logística ha
    introducido las innovaciones digitales."""
    
    # Palabra que queremos contar
    palabra_buscada = "logística"

    # Obtener el número de veces que aparece la palabra en el párrafo
    veces = contar_palabra(palabra_buscada, parrafo)
    print(f" {veces} ocurrencias encontradas")

# Ejemplo de uso
if __name__ == "__main__":
    main()

