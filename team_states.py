import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from api import get_team_stats


def main():
    # Introducir las funcion que se crean
    temporadas_habilitadas()

# Crear las funciones que se utilizaran en el codigo

def temporadas_habilitadas():
    for season in (2026, 2025, 2024, 2023, 2022, 2021, 2020):
        teams = get_team_stats(season=season)
        if teams:
            print(f'Tamano de teams: {len(teams)}')
            print(f'Tipo de datos de teams: {type(teams)}')
            print(f'Datos que contiene: {teams}')


if __name__ == "__main__":
    main()