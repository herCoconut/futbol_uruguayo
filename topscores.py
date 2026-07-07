import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from api import get_topscorers


def main():
    for season in (2026, 2025, 2024):
        topscorers = get_topscorers(season=season)
        if topscorers:
            print(f"Temporada {season}:")
            # topscorers es una lista de diccionarios, por eso no se puede hacer topscorers["player"]
            for scorer in topscorers:
                player_name = scorer["player"]["name"]
                team_name = scorer["statistics"][0]["team"]["name"]
                goals = scorer["statistics"][0]["goals"]["total"]
                print(f"{player_name} - {team_name} - Goles: {goals}")
            break
    else:
        print("No se encontraron datos de máximos goleadores.")


if __name__ == "__main__":
    main()

