import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from api import get_topscorers


def main():
    for season in (2026, 2025, 2024):
        topscorers = get_topscorers(season=season)
        if topscorers:
            print(f"Temporada {season}:")
            print(topscorers[:5])
            break
    else:
        print("No se encontraron datos de máximos goleadores.")


if __name__ == "__main__":
    main()

