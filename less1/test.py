import sys
import os
from collections import namedtuple

from pathlib import Path
from time import sleep

sys.path.append("C:\\Users\\pesny\\projects\\learning\\game-dev\\minecraft\\Minecraft_Tools_1_19_Python_3_10\\Minecraft_Tools_1_19_Python_3_10\\minecraftPythonAPI\\py3minepi-master")

import mcpi.minecraft as minecraft
craft = minecraft.Minecraft.create(address="minecraft-server.hcloud")
craft.postToChat("Мини игра найди три секретный места успешно загружено, все :-) можно искать!")

Cor = namedtuple("Cor",["x","y","z"])
game_location = Cor(x=-15,y=13,z=-16)
game_location2 = Cor(x=-14,y=0,z=38)
game_location3 = Cor(x=25,y=-1,z=38)
game_location4 = Cor(x=6,y=-15,z=38)
find_once_loc = Cor(x=None,y=None,z=None)
wait_time = 5
print(game_location)

# x(СеверЮг):6    y(НизВерх):-15, z(ЗападВосток):38
while True:
    cor = None
    players = []
    try:
        players = craft.getPlayerEntityIds()
        if len(players) == 0: 
            raise "No users"
        cor = craft.player.getTilePos()
    except Exception as e:
        pass
    finally:
        if ( len(players) > 0 and find_once_loc is None):
            print("Подключились новые игроки")
            find_once_loc = Cor(x=None,y=None,z=None)

        
    if (cor is not None):
        print(f"x(СеверЮг):{cor.x}\ty(НизВерх):{cor.y},\tz(ЗападВосток):{cor.z}")
        if (cor == game_location ): 
            if (find_once_loc != cor):
                craft.postToChat("Ура,ты нашёл место Полины")
        elif (cor == game_location2):
            if (find_once_loc != cor):
                craft.postToChat("Ура,ты нашёл место Ильи")
        elif (cor == game_location3):
            if (find_once_loc != cor):  
                craft.postToChat("Ура,ты нашёл место Артёма")
        elif (cor == game_location4):
            if (find_once_loc != cor):
                craft.postToChat("Ура ты нашел место Папы!")
        find_once_loc = cor
        wait_time = 0.5    
    else:
        find_once_loc = None
        print("В системе не найдено ни одного игрока, ожидаю игроков, до начала игры")
        wait_time = 5
    sleep(wait_time)