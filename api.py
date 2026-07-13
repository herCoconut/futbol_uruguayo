import requests
import os
import json
import hashlib
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io"      # https://dashboard.api-football.com/ web del dasboard

HEADERS = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY,
}

LIGA_URUGUAY = 268  # ID Primera division - Apertura


def _cache_path_for(endpoint, params):
    key = json.dumps({"endpoint": endpoint, "params": params}, sort_keys=True)
    h = hashlib.sha1(key.encode("utf-8")).hexdigest()
    cache_dir = os.path.join(".cache", "api")
    os.makedirs(cache_dir, exist_ok=True)
    return os.path.join(cache_dir, f"{h}.json")


def _get(endpoint, params=None, cache_ttl=3600, force=False):
    """Llama a la API y cachea la respuesta en `.cache/api/`.

    - `cache_ttl`: segundos que mantiene la caché válida.
    - `force`: si True fuerza refrescar y no usa la caché.
    """
    if params is None:
        params = {}

    cache_file = _cache_path_for(endpoint, params)
    if not force and os.path.exists(cache_file):
        mtime = os.path.getmtime(cache_file)
        if (time.time() - mtime) < cache_ttl:
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                # si hay error leyendo la caché, continuar y refrescar
                pass

    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    resp = response.json().get("response")

    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(resp, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    return resp

for season in range(2000, 2026):
    print(f'Temporadas disponibles: {season} - {get_standings(season=season, cache_ttl=3600, force=False)}')

# Ejemplos de llamadas con caché centralizada
def get_fixtures(season=2024, league=LIGA_URUGUAY, cache_ttl=3600, force=False):
    return _get("fixtures", {"league": league, "season": season}, cache_ttl=cache_ttl, force=force)


def get_standings(season=2024, league=LIGA_URUGUAY, cache_ttl=3600, force=False):
    return _get("standings", {"league": league, "season": season}, cache_ttl=cache_ttl, force=force)


def get_topscorers(season=2024, league=LIGA_URUGUAY, cache_ttl=3600, force=False):
    return _get("players/topscorers", {"league": league, "season": season}, cache_ttl=cache_ttl, force=force)


def get_team_stats(team_id, season=2024, league=LIGA_URUGUAY, cache_ttl=3600, force=False):
    return _get("teams/statistics", {"league": league, "season": season, "team": team_id}, cache_ttl=cache_ttl, force=force)