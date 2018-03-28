import json


class Player(object):
    def __init__(self, id = None, nickname = None, gold = None, map_position = None, json_data = None):
        self.id = id
        self.nickname = nickname
        self.gold = gold
        self.map_position  = map_position

        if json_data is not None:
            self.__dict__ = json_data
    
    def get_json_format(self):
        return self.__dict__


def Save(lista_graczy):
    with open('players.json', 'w') as outfile:
        json_to_save = {}
        for player in lista_graczy:
            json_to_save[player.id] = player.get_json_format()
        outfile.write(json.dumps(json_to_save, indent=4))

new_players  = []
def Load(plik):
    with open(str(plik), 'r') as outfile:
        loaded_json = json.load(outfile)
        for id, player_json in loaded_json.items():
            print("Loaded player: " + str(player_json))
            new_players.append(Player(json_data = player_json))

Load("players.json")

