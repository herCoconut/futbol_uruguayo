import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY
}

LIGA_URUGUAY = 201  #Confirmar el ID real????

def _get(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()["response"]

def get_fixtures(season=2026, league=LIGA_URUGUAY):
    return _get("fixtures", {"league": league, "season": season})

def get_standings(season=2026, league=LIGA_URUGUAY):
    return _get("standings", {"league": league, "season": season})

def get_topscorers(season=2026, league=LIGA_URUGUAY):
    return _get("players/topscorers", {"league": league, "season": season})

def get_team_stats(team_id, season=2026, league=LIGA_URUGUAY):
    return _get("teams/statistics", {"league": league, "season": season, "team": team_id})