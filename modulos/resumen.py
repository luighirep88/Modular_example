import pandas as pd

def consolidar_dataframe(multiplos, potencias, suma):
    """
    Crea un DataFrame consolidado con los resultados.
    """
    df = pd.DataFrame({
        'multiplos': multiplos,
        'potencias': potencias,
        'suma': suma
    })
    return df

def estadisticas_basicas(df):
    """
    Imprime estadísticas básicas de cada columna del DataFrame.
    """
    print("Estadísticas descriptivas:")
    print(df.describe())