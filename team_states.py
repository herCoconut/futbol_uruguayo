import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from api import get_team_stats


def main():
    # Introducir las funcion que se crean
    temporadas_habilitadas()

# Crear las funciones que se utilizaran en el codigo

def temporadas_habilitadas():
    team_id = 3
    teams = get_team_stats(team_id=team_id)
    if teams:
        print(f'El team_id {team_id} es valido.')
        print(f'Tamano de teams: {len(teams)}.')
        print(f'Tipo de datos de teams: {type(teams)}.')
        print(f'Datos que contiene: {teams}.')
    else:
        print(f'El team_id {team_id} no es valido.')

if __name__ == "__main__":
    main()