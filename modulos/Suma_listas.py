def suma_elementos(lista1, lista2):
    """
    Suma posición a posición dos listas del mismo largo.
    Ejemplo: [1,2,3], [4,5,6] → [5,7,9]
    """
    return [a + b for a, b in zip(lista1, lista2)]