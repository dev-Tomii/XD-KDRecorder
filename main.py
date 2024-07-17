import json
from tkinter import messagebox as mb

gamemodes = ["Escort", "Zone Control", "Domination", "Occupy", "Hot Shot", "CTF", "TDM"]

with open("./db.json", "r") as file:
    db = json.load(file)

def resetDB():
    for i in db:
        i["kd"] = 0
        i["record"] = []
    with open("./db.json", "w") as file:
        json.dump(db, file)


def get_gamemode_info(gamemode):
    for item in db:
        if item["name"].upper() == gamemode.upper():
            return item
    return None

def add_record(gamemode, kd):
    selected = get_gamemode_info(gamemode)
    if selected is None:
        mb.showerror(title = "Error", message = "Plase, choose a gamemode from the list")
        return
    games = selected["record"]

    if len(games) < 10:
        games.append(kd)
    else:
        games.pop(0)
        games.append(kd)

    total = sum(games)
    selected["kd"] = round(total / len(games), 2)

def new_kd(gamemode_name, kills, deaths):
    kd = kills / deaths if deaths != 0 else kills
    add_record(gamemode_name, kd)
    with open("./db.json", "w") as file:
        json.dump(db, file)

