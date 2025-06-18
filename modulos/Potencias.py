def primeras_potencias(n, cantidad=10):
    """
    Devuelve una lista con las primeras 'cantidad' potencias de n.
    Ejemplo: n=2 → [1,2,4,8,...,512]
    """
    return [n ** i for i in range(cantidad)]
