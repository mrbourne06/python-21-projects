import requests
from pprint import PrettyPrinter

printer = PrettyPrinter()

def get_scoreboard():
    url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
    res = requests.get(url)
    data = res.json()

    games = data['scoreboard']['games']

    for game in games:
        home = game['homeTeam']
        away = game['awayTeam']
        clock = game['gameClock']
        period = game['period']
        
        print('-----------------------------')
        print(f"{home['teamTricode']} vs {away['teamTricode']}")
        print(f"{home['score']} - {away['score']}")
        print(f"{clock} - Q{period}")

get_scoreboard()
