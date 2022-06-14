import requests
import json

urls = {
    "best_games": "https://games.gamepix.com/games?sid=P3T7T&order=q",
    "newest_games": "https://games.gamepix.com/games?sid=P3T7T&order=d",
    "categories": "https://games.gamepix.com/categories",
    "single_game_prefix": "https://games.gamepix.com/game?sid=P3T7T&gid=",
    "category_prefix": " https://games.gamepix.com/games?category="
}

class categoryData:
    def __init__(self, id, urlPrefixForGame):
        self.id = id
        self.urlPrefixForGame = urlPrefixForGame

    def createCategoryDataObj(self):
        obj = {
            "category_url": urls["category_prefix"] + self.id,
            "url_prefix_for_game": self.urlPrefixForGame
        }
        return obj


def load_games():
    url = urls["best_games"]
    r = requests.get(url)
    response = json.loads(r.text)
    games_obj = response["data"]
    return games_obj

def load_categories():
    url = urls["categories"]
    r = requests.get(url)
    response = json.loads(r.text)
    category_objs = response["data"]
    return category_objs

def get_best_games (games, limit, start):
    requested_games = []

    games_len = len(games)

    for i in range(start, games_len):
        if len(requested_games) == limit or len(requested_games) > limit:
            break

        requested_games.append(games[i])

    return requested_games

def get_best_mobile_games (games, limit, start):
    requested_games = []
    games_len = len(games)

    for i in range(start, games_len):
        cur_game = games[i]

        if len(requested_games) == limit or len(requested_games) > limit:
            break
        elif cur_game['touch'] == True:
            requested_games.append(cur_game)
        
    return requested_games

def get_game_by_id(gameid):
    url = urls["single_game_prefix"] + gameid
    
    r = requests.get(url)
    response = json.loads(r.text)

    return response