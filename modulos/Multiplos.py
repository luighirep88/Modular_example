def primeros_multiplos(n, cantidad=10):
    """
    Devuelve una lista con los primeros 'cantidad' múltiplos de n.
    Ejemplo: n=3 → [3,6,9,...,30]
    """
    return [n * i for i in range(1, cantidad+1)]
