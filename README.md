# Fut matchmaker

With this project, it's possible to rank your friends soccer skills, and then use the players scores to create a balanced team for your next match.
the objective was to make a simple process to rank each player and use it as input to generate two teams.

imput a list of players with an attack and defense score:

``` json
[
    {"name":"James", "attack": 2.27, "defense": 3.07},
    {"name":"Lucas", "attack": 2.40, "defense": 4.07},
    {"name":"Daniel", "attack": 4.00, "defense": 2.93},
    {"name":"Jack", "attack": 3.47, "defense": 3.60},
    {"name":"Leo", "attack": 3.40, "defense": 2.60},
    {"name":"John", "attack": 2.60, "defense": 3.13},
    {"name":"David", "attack": 2.93, "defense": 2.00},
    {"name":"Julian", "attack": 3.80, "defense": 3.33},
    {"name":"Dylan", "attack": 3.93, "defense": 4.20},
    {"name":"Charles", "attack": 4.20, "defense": 2.47}
]
```

and receive some team suggestions for your match:
```
TEAM 1
attack: 16.6, defense: 15.8 team: ('James', 'Daniel', 'Jack', 'David', 'Dylan')
TEAM 2
attack: 16.4, defense: 15.6 team: ('Lucas', 'Leo', 'John', 'Julian', 'Charles')


TEAM 1
attack: 16.34, defense: 15.6 team: ('James', 'Jack', 'John', 'Julian', 'Charles')
TEAM 2
attack: 16.66, defense: 15.8 team: ('Lucas', 'Daniel', 'Leo', 'David', 'Dylan')


TEAM 1
attack: 16.4, defense: 15.47 team: ('James', 'Leo', 'John', 'Dylan', 'Charles')
TEAM 2
attack: 16.6, defense: 15.93 team: ('Lucas', 'Daniel', 'Jack', 'David', 'Julian')
```

## Players ranks

In here, I'm going to share what my group of friends did that worked, feel free to make this your way. Here we will have to do some manual work to get the scores.
### creating an online poll
we created an online poll that everyone ranks everyone, ranking from 1 to 5 in the following traits:

1. Man-to-man marking
2. Physical dominance
3. Stamina\Endurance
4. Dribble
5. Pass
6. Goal Shot

And after everyone finish vote, each player will have a score like this:

| Player | Man-to-man marking | Physical dominance | Stamina\Endurance | Dribble | Pass | Goal Shot |
|---|---|---|---|---|---|---|
| James |2,80 | 3,07 |	4,07 | 	2,27 | 	2,73 | 	1,93 | 

To transform all of this to Attack and Defense scores, we decided that:
 - Defense - mean of Man-to-man marking, Physical dominance and Stamina\Endurance
 - Attack - mean of Dribble, Pass and Goal Shot
  
And then just fill `players.json` with all scores and you are ready to run the script.


## How to run

1. create a player.json file using player-sample.jsom as an example 
2. check main.py file and change the next_game_players and TEAM_SIZE variables to match the game you are going to play
3. run `python3 -m main`