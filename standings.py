import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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

    colores_equipos = {
        "Penarol": "#fdca01",
        "Nacional": "#f80020",
        "Defensor sporting": "#450090",
        "Boston River": "#1f5428",
        "Progreso": "#de0204",
        "Cerro Largo": "#2b29d2",
        "Racing Montevideo": "#1c6823",
        "Liverpool Montevideo": "#003399",
        "Wanderers": "#1d120e",
        "Cerro": "#0193de",
        "Deportivo Maldonado": "#d00000",
        "Rampla Juniors": "#009a3e",
        "CA River Plate": "#c01b24",
        "Danubio": "#171613",
        "Fenix": "#6e3178",
        "Miramar": "#e5060b",
    }






if __name__ == "__main__":
    main()