import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io"      # https://dashboard.api-football.com/ web del dasboard

HEADERS = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY
}

LIGA_URUGUAY = 268  # ID Primera division - Apertura

def _get(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()["response"]


#for liga in _get("leagues", {"country": "Uruguay"}):
    nombre = liga["league"]["name"]
    id_liga = liga["league"]["id"]
    temporadas = [s["year"] for s in liga["seasons"]]
    print(f"{id_liga} - {nombre} - Temporadas disponibles: {temporadas} ")


def get_fixtures(season=2026, league=LIGA_URUGUAY):
    return _get("fixtures", {"league": league, "season": season})

def get_standings(season=2026, league=LIGA_URUGUAY):
    return _get("standings", {"league": league, "season": season})

def get_topscorers(season=2026, league=LIGA_URUGUAY):
    return _get("players/topscorers", {"league": league, "season": season})

def get_team_stats(team_id, season=2026, league=LIGA_URUGUAY):
    return _get("teams/statistics", {"league": league, "season": season, "team": team_id})