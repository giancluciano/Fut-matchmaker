# Fut matchmaker

Com este projeto, é possível classificar as habilidades de futebol de seus amigos e, em seguida, usar as pontuações dos jogadores para criar um time equilibrado para sua próxima partida. O objetivo era criar um processo simples para classificar cada jogador e usá-lo como entrada para gerar dois times.

Entrada uma lista de jogadores com uma pontuação de ataque e defesa:

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

e receba algumas sugestões de times para sua partida:
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

## Classificações dos Jogadores

Aqui, vou compartilhar o que meu grupo de amigos fez que funcionou, sinta-se à vontade para fazer isso do seu jeito. Aqui teremos que fazer algum trabalho manual para obter as pontuações.
### Criando uma enquete online
criamos uma enquete online em que todos classificam todos, classificando de 1 a 5 nas seguintes habilidades:

1. Marcação
2. Dominância física
3. Resistência
4. Drible
5. Passe
6. Chute a gol

E depois que todos terminarem de votar, cada jogador terá uma pontuação como esta:

| Player | Marcação | Dominância física | Resistência | Drible | Passe | Chute a gol |
|---|---|---|---|---|---|---|
| James |2,80 | 3,07 |	4,07 | 	2,27 | 	2,73 | 	1,93 | 

Para transformar tudo isso em pontuações de Ataque e Defesa, decidimos que:
 - Defesa - média das notas de Marcação, Dominância física e Resistência
 - Attack - média do Drible, Passe e Chute a gol

E então basta preencher `players.json` com todas as pontuações e você está pronto para rodar o script.


## Como rodar

1. crie um arquivo player.json usando player-sample.jsom como exemplo 
2. verifique o arquivo main.py e altere as variáveis next_game_players e TEAM_SIZE para corresponder ao jogo que você vai jogar
3. execute `python3 -m main`