import json
from tkinter import messagebox as mb

gamemodes = ["Escolta", "Control de Zonas", "Dominacion", "Ocupacion", "Estrella", "CLB", "TDM"]

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
        if item["name"].lower() == gamemode.lower():
            return item
    return None

def add_record(gamemode, kd):
    selected = get_gamemode_info(gamemode)
    if selected is None:
        mb.showerror(title = "Error", message = "No se ha seleccionado un modo de juego")
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

# Luego puedes llamar a las funciones como en el siguiente ejemplo:
# new_kd("Deathmatch", 100, 50, db)
new_kd('control de zonas', 100, 50)
