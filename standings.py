import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from api import get_standings


def main():
    # Introducir las funcion que se crean
    ranking()

# Crear las funciones que se utilizaran en el codigo

def ranking():
    # Obtener los datos de la API
    data = get_standings()

    # Convertir los datos a un DataFrame de pandas
    df = pd.json_normalize(data[0])

    print(df.info())
    # print(df.head())



if __name__ == "__main__":
    main()