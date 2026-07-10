import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import json
import time
from api import get_standings


def main():
    # Introducir las funcion que se crean
    ranking()

# Crear las funciones que se utilizaran en el codigo

def ranking(season=2024, league=None, cache_ttl=3600, force=False):
    # Obtener los datos (la caché ahora está centralizada en `api.py`)
    if league is None:
        data = get_standings(season=season, cache_ttl=cache_ttl, force=force)
    else:
        data = get_standings(season=season, league=league, cache_ttl=cache_ttl, force=force)

    # Convertir los datos a un DataFrame de pandas
    df = pd.json_normalize(
        data[0]["league"]["standings"][0],
        sep="_",
    )

    # Mostrar info resumida
    print(f"\033[103mColumnas del DataFrame: \033[0m{df.columns.tolist()}")
    print(f"\033[103mSe muestra los nombres de los equipos: \033[0m{df['team_name'].tolist()}")






if __name__ == "__main__":
    main()