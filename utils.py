import json
import networkx as nx

def getGameState(state):
    try:
        return json.loads(json.loads(state)['gameState'])
    except:
        print(state)

def getTiles(state):
    return state['map']['tiles']

def removeEdge(G: nx.Graph, tile1, tile2):
    try:
        G.remove_edge(tile1, tile2)
        G.remove_node(tile2)
    except:
        pass

def tileWeight(entity):
    if entity == "BLACKHOLE" or entity == "ASTEROID":
        return 100000
    return 1

def edgeWeight(G: nx.Graph, coords):
    try:
        return G.nodes[coords]['weight']
    except:
        return 1

def addEdges(G: nx.Graph, tile):
    G.add_edge((tile['q'], tile['r']),(tile['q'], tile['r']+1), weight=edgeWeight(G, (tile['q'], tile['r']+1))) 
    G.add_edge((tile['q'], tile['r']),(tile['q'], tile['r']-1), weight=edgeWeight(G, (tile['q'], tile['r']-1)))
    G.add_edge((tile['q'], tile['r']),(tile['q']-1, tile['r']), weight=edgeWeight(G, (tile['q']-1, tile['r'])))
    G.add_edge((tile['q'], tile['r']),(tile['q']+1, tile['r']), weight=edgeWeight(G, (tile['q']+1, tile['r']))) 
    G.add_edge((tile['q'], tile['r']),(tile['q']-1, tile['r']+1), weight=edgeWeight(G, (tile['q']-1, tile['r']+1)))
    G.add_edge((tile['q'], tile['r']),(tile['q']+1, tile['r']-1), weight=edgeWeight(G, (tile['q']+1, tile['r']-1)))
    if tile['r'] == -14:
        removeEdge(G,(tile['q'], tile['r']),(tile['q'], tile['r']-1))
        removeEdge(G,(tile['q'], tile['r']),(tile['q']+1, tile['r']-1)) 
    if tile['q'] == 14:
        removeEdge(G,(tile['q'], tile['r']),(tile['q']+1, tile['r']-1)) 
        removeEdge(G,(tile['q'], tile['r']),(tile['q']+1, tile['r'])) 
    if tile['q'] + tile['r'] == 14:
        removeEdge(G,(tile['q'], tile['r']),(tile['q']+1, tile['r'])) 
        removeEdge(G,(tile['q'], tile['r']),(tile['q'], tile['r']+1))
    if tile['r'] == 14:
        removeEdge(G,(tile['q'], tile['r']),(tile['q']-1, tile['r']+1))
        removeEdge(G,(tile['q'], tile['r']),(tile['q'], tile['r']+1))
    if tile['q'] == -14:
        removeEdge(G,(tile['q'], tile['r']),(tile['q']-1, tile['r']+1))
        removeEdge(G,(tile['q'], tile['r']),(tile['q']-1, tile['r']))
    if tile['q'] + tile['r'] == -14:
        removeEdge(G,(tile['q'], tile['r']),(tile['q']-1, tile['r']))
        removeEdge(G,(tile['q'], tile['r']),(tile['q'], tile['r']-1))
 
def createGraph(tiles):
    G = nx.Graph()
    for tile_row in tiles:
        for tile in tile_row:
            G.add_node((tile['q'],tile['r']), weight=tileWeight(tile['entity']['type']))
    for tile_row in tiles:
        for tile in tile_row:
            addEdges(G, tile)
    return G

def stepsToSomething(G:nx.Graph, player_tile, coords=(0,0)):
    # return nx.dijkstra_path(G, player_tile, coords)
    return nx.astar_path(G, player_tile, coords)