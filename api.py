import requests
import pandas as pd

def get_driver_standings(driver_id, start_year, end_year):
    results = []
    for year in range(start_year, end_year + 1):
        url = f"https://ergast.com/api/f1/{year}/drivers/{driver_id}/driverStandings.json"
        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()

            standings_list = data.get('MRData', {}).get('StandingsTable', {}).get('StandingsLists', [])
            if standings_list:
                standings = standings_list[0]['DriverStandings'][0]
                results.append({
                    "year": year,
                    "points": float(standings.get("points", 0)),
                    "wins": int(standings.get("wins", 0)),
                    "position": int(standings.get("position", 0))
                })
        except (requests.exceptions.RequestException, IndexError):
            continue

    return pd.DataFrame(results)

def get_driver_results(driver_id, start_year, end_year):
    data = []
    for year in range(start_year, end_year + 1):
        url = f"https://ergast.com/api/f1/{year}/drivers/{driver_id}/results.json?limit=1000"
        try:
            res = requests.get(url)
            res.raise_for_status()
            data_json = res.json()

            races = data_json.get("MRData", {}).get("RaceTable", {}).get("Races", [])
            for race in races:
                result = race["Results"][0]
                data.append({
                    "year": year,
                    "position": result.get("position", ""),
                    "grid": result.get("grid", ""),
                    "status": result.get("status", "")
                })
        except requests.exceptions.RequestException:
            continue

    return pd.DataFrame(data)
