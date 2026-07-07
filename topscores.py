import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from api import get_topscorers


def main():
    for season in (2026, 2025, 2024, 2023, 2022, 2021, 2020):   # Temporadas habilitadas: 2024, 2023 y 2022
        topscorers = get_topscorers(season=season)
        if topscorers:
            # print(topscorers[0])
            print(f"Temporada {season}:")
            # topscorers es una lista de diccionarios, por eso no se puede hacer topscorers["player"]
            for scorer in topscorers:
                player_name = scorer["player"]["name"]
                team_name = scorer["statistics"][0]["team"]["name"]
                goals = scorer["statistics"][0]["goals"]["total"]
                position = scorer["statistics"][0]["games"]["position"]
                appearances = scorer["statistics"][0]["games"]["appearences"]
                minutes_played = scorer["statistics"][0]["games"]["minutes"]
                minutes_per_goal = minutes_played / goals if goals > 0 else None
                print(f"{player_name} - {team_name} - Goles: {goals} - Posición: {position} - Apariciones: {appearances} - Minutos por gol: {int(minutes_per_goal)}")
            print("\n")
    else:
        print("No se encontraron datos de máximos goleadores.")


if __name__ == "__main__":
    main()

