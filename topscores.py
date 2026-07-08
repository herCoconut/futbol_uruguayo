import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from api import get_topscorers


def main():
    for season in (2026, 2025, 2024, 2023, 2022, 2021, 2020):   # Temporadas habilitadas: 2024, 2023 y 2022
        topscorers = get_topscorers(season=season)
        if topscorers:
            
            # Se crean listas
            player_list = []    # Lista de jugadores para cada temporada
            goals_list = []     # Lista de goles para cada temporada
            minutes_per_goal_list = []  # Lista de minutos por gol para cada temporada

            print(f"Temporada {season}:")
            # topscorers es una lista de diccionarios, por eso no se puede hacer topscorers["player"]
            for scorer in topscorers:
                # Maximos goleadores
                player_name = scorer["player"]["name"]
                player_list.append(player_name)
                # Equipos donde juegan
                team_name = scorer["statistics"][0]["team"]["name"]
                # Goles convertidos
                goals = scorer["statistics"][0]["goals"]["total"]
                goals_list.append(goals)
                # Posicion en la que juega
                position = scorer["statistics"][0]["games"]["position"]
                # Partidos jugados
                appearances = scorer["statistics"][0]["games"]["appearences"]
                # Minutos jugados
                minutes_played = scorer["statistics"][0]["games"]["minutes"]
                # Calculo de minutos por gol
                minutes_per_goal = minutes_played / goals if goals > 0 else None
                minutes_per_goal_list.append(minutes_per_goal)

                # Se muestra la informacion de cada jugador
                print(f"{player_name} - {team_name} - Goles: {goals} - Posición: {position} - Apariciones: {appearances} - Minutos por gol: {int(minutes_per_goal)}")
            print("\n")

            plt.figure(figsize=(10, 6))
            plt.bar(player_list, goals_list, color='blue')
            plt.xlabel('Jugadores')
            plt.ylabel('Goles')
            plt.title(f'Máximos Goleadores Temporada {season}')
            plt.xticks(rotation=45)
            plt.savefig('Maximos_Goleadores.png')

    else:
        print("No se encontraron datos de máximos goleadores.")


if __name__ == "__main__":
    main()

