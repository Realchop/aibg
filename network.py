import requests as req
import json
from utils import getGameState

url = "http://aibg22.com:8081"

creds = {
    "username": "CHOP1",
    "password": "6bkBHDs#zA"
}

headers = {
    "Content-Type": "application/json"
}

def login():
    res = req.post(f"{url}/user/login", json=creds)
    headers["Authorization"] = f'Bearer: {json.loads(res.text)["token"]}'

def joinGame():
    res = req.get(f"{url}/game/joinGame", headers=headers)
    gameState = getGameState(res.text)
    return gameState, json.loads(res.text)["playerIdx"]

def train():
    payload = {
        "mapName": "test2.txt",
        "playerIdx": 1,
        "time": 1
    }
    res = req.post(f"{url}/game/train", json=payload, headers=headers)
    state = getGameState(res.text)
    return state, 1
 
def actionTrain(code):
    payload = {
        "action": code
    }
    res = req.post(f"{url}/game/actionTrain", json=payload, headers=headers)
    return getGameState(res.text)
    
def action(code):
    payload = {
        "action": code
    }
    res = req.post(f"{url}/game/doAction", json=payload, headers=headers)
    return getGameState(res.text)