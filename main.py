import requests

team_id = 713659
gameweek_id = 33

player_data = {}
player_gameweeks = {}

static = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
static_json = static.json()
static_keys = static_json.keys()
#print(static_keys)
elements = static_json['elements']

for player in elements:
    id = player['id']
    player_data[id] = player


user_info = requests.get("https://fantasy.premierleague.com/api/entry/"+str(team_id)+"/")
user_info_json = user_info.json()
user_info_keys = user_info_json.keys()
print(user_info_json['name']+" Gameweek "+str(gameweek_id))
print("")

gameweek = requests.get("https://fantasy.premierleague.com/api/entry/"+str(team_id)+"/event/"+str(gameweek_id)+"/picks/")
gameweek_json = gameweek.json()
gameweek_keys = gameweek_json.keys()

#print(player_data[302])

for player_metadata in gameweek_json['picks']:
    player_id = player_metadata['element']
    player = player_data[player_id]
    is_captain = player_metadata['is_captain']
    is_vice = player_metadata['is_vice_captain']
    append = ""
    if is_captain:
        append = "(C)"
    elif is_vice:
        append = "(V)"

    print(player["first_name"]+" "+player["second_name"]+" "+append)


