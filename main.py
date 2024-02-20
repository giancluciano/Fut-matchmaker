import json
from itertools import combinations

### Add here all players that will play in the next match

next_game_players = [
    "James",
    "Lucas",
    "Daniel",
    "Jack",
    "Leo",
    "John",
    "David",
    "Julian",
    "Dylan",
    "Charles"
]

## change here with the team size you use to play
TEAM_SIZE = 5

# get best combination with a pre-made team
PRE_MADE_TEAM = None
# PRE_MADE_TEAM = ["James", "Lucas"] # if you wish that two or more people stay in the same team change use this option

## Note, if you play 7 a side soccer with a fixed goalkeeper, add a team size of 6 and do not add him to the player list

if __name__ == "__main__":
    players = []
    with open('players.json') as f:
        players = json.load(f)

    players = list(filter(lambda item: item["name"] in next_game_players, players))

    team_combinations = list(combinations(players, TEAM_SIZE))

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

    def print_teams(_match):
        print("TEAM 1")
        print(f'attack: {round(sum(map(lambda item: item["attack"], _match[1])),2)}, defense: {round(sum(map(lambda item: item["defense"], _match[1])),2)} team: {tuple(map(lambda item: item["name"], _match[1]))}')
        print("TEAM 2")
        print(f'attack: {round(sum(map(lambda item: item["attack"], _match[2])),2)}, defense: {round(sum(map(lambda item: item["defense"], _match[2])),2)} team: {tuple(map(lambda item: item["name"], _match[2]))}')
        print()
        print()
    
    # get three most balanced teams 
    matchs.sort(key=lambda item: item[0])
    if not PRE_MADE_TEAM:
        for i in range(0, 3):
            print_teams(matchs[i])
    else:
    # get best combination with a pre-made team
        for _match in matchs:
            if len(list(filter(lambda item: item["name"] in PRE_MADE_TEAM, _match[1]))) == len(PRE_MADE_TEAM) or len(list(filter(lambda item: item["name"] in PRE_MADE_TEAM, _match[2]))) == len(PRE_MADE_TEAM):
                print_teams(_match)
                break
