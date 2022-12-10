from network import login, joinGame, train, action, actionTrain
from utils import createGraph, stepsToSomething, getTiles

training = True

if __name__ == "__main__":
    login()
    if training:
        connect = train
        act = actionTrain
        
    else:
        connect = joinGame
        act = action

    state, id = connect()
    tiles = getTiles(state)
    player = state[f'player{id}']
    G = createGraph(tiles)
    while True:
        shot = False
        for coords in [*[(state[f"player{i+1}"]['q'],state[f"player{i+1}"]['r']) for i in range(4)]]:
            steps = stepsToSomething(G, (player['q'],player['r']), coords)
            if len(steps) <= 4 and coords != (player['q'], player['r']):
                tile = coords
                state = act(f'attack,{tile[0]},{tile[1]}')
                shot = True
                break
        if not shot:
            steps = stepsToSomething(G, (player['q'],player['r']), (0,0))
            if len(steps) <= 5:
                tile = steps[-2]
                state = act(f'attack,{tile[0]},{tile[1]}')
            else:
                tile = steps[1]
                state = act(f'move,{tile[0]},{tile[1]}')
        tiles = getTiles(state)
        player = state[f'player{id}']
