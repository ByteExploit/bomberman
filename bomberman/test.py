from map import map_pop_all
from bomb_logic import Bomb
from player import test_player
import player


def main():
    gameMap = map_pop_all("15,15", spawnLocation=[1, 1])
    print("poped all")
    for row in gameMap.grid:
        print(" ".join(f"{cell:2}" for cell in row))
    theBomb = Bomb(gameMap)
    if theBomb.can_plant():
        theBomb.bomb_plant()
        print("bomb palnted")
        for row in gameMap.grid:
            print(" ".join(f"{cell:2}" for cell in row))
        theBomb.bomb_explode()
        print("bomb exploded")
        for row in gameMap.grid:
            print(" ".join(f"{cell:2}" for cell in row))
    test_player()


main()
