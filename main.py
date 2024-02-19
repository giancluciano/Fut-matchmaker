import json
from itertools import combinations

def print_teams(_match):
    print("TIME 1")
    print(f'ataque: {round(sum(map(lambda item: item["attack"], _match[1])),2)}, defesa: {round(sum(map(lambda item: item["defense"], _match[1])),2)} time: {tuple(map(lambda item: item["name"], _match[1]))}')
    print("TIME 2")
    print(f'ataque: {round(sum(map(lambda item: item["attack"], _match[2])),2)}, defesa: {round(sum(map(lambda item: item["defense"], _match[2])),2)} time: {tuple(map(lambda item: item["name"], _match[2]))}')
    print()
    print()

next_game_players = [
    "Gian",
    "Pedro",
    "Feyh",
    "Ramos",
    "Leo",
    "Freitas",
    "Dudes",
    "Xixa",
    "Neto",
    "Marley",
    "Giox",
#    "Pereca",
    "Wandeco",
    "Miguel",
    "BK",
#    "Marcelo",
]


if __name__ == "__main__":
    players = []
    with open('players.json') as f:
        players = json.load(f)

    players = list(filter(lambda item: item["name"] in next_game_players, players))

    team_combinations = list(combinations(players,7))

    team_1_index = 0
    team_2_index = len(team_combinations) -1

    matchs = []

    while team_1_index < team_2_index:
        team_1_attack = sum(map(lambda item: item["attack"], team_combinations[team_1_index]))
        team_1_defense = sum(map(lambda item: item["defense"], team_combinations[team_1_index]))
        team_2_attack = sum(map(lambda item: item["attack"], team_combinations[team_2_index]))
        team_2_defense = sum(map(lambda item: item["defense"], team_combinations[team_2_index]))

        score_difference = abs(team_1_attack - team_2_attack) + abs(team_1_defense - team_2_defense)
        matchs.append((score_difference, team_combinations[team_1_index], team_combinations[team_2_index]))
        team_1_index += 1
        team_2_index -= 1

    # get three most balanced teams 
    matchs.sort(key=lambda item: item[0])
    for i in range(0, 3):
        print_teams(matchs[i])


    # get best combination with a pre-made team
    names = ["Neto", "Marley"]
    print(names)
    for _match in matchs:
        if len(list(filter(lambda item: item["name"] in names, _match[1]))) == len(names) or len(list(filter(lambda item: item["name"] in names, _match[2]))) == len(names):
            print_teams(_match)
            break

