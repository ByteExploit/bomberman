# from nt import system
from map import Map, map_pop_all

# from tbi import GridSymbols, Wasd
from player import Player
from bomb_logic import Bomb
import msvcrt

# import os
import time
from ai import Enemy
import shutil


def get_key():
    key = msvcrt.getch().decode("utf-8").lower()
    return key


def print_screen_centered(gameMap):
    term_width, term_height = shutil.get_terminal_size()
    map_height = len(gameMap.grid)
    map_width = max(len(row) * 3 for row in gameMap.grid)  # 3 per cell for padding

    top_padding = max((term_height - map_height) // 2, 0)
    side_padding = max((term_width - map_width) // 2, 0)

    print("\033[H\033[J", end="")  # clear screen
    print("\n" * top_padding)  # vertical centering

    for row in gameMap.grid:
        line = " ".join(f"{cell:2}" for cell in row)
        print(" " * side_padding + line)  # horizontal centering


def clear_screen():
    print("\033[H\033[J", end="")


#
#
# def print_screen(gameMap):
#     for row in gameMap.grid:
#         print(" ".join(f"{cell:2}" for cell in row))


def main():
    gameMap = Map((15, 15))
    map_pop_all([1, 1], gameMap)
    human = Player(gameMap)
    human.spawn()
    enemy1 = Enemy(gameMap, (1, 5))
    enemy2 = Enemy(gameMap, (11, 11))
    tickRate = 0.5
    lastTick = time.time()
    enemy1.spawn()
    enemy2.spawn()
    enemies = [enemy1, enemy2]
    bombPlanted = False
    theBomb = None
    screenDirty = True

    while human.alive:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8").lower()

            if key == "w":
                human.move(-1, 0)
                screenDirty = True

            elif key == "a":
                human.move(0, -1)
                screenDirty = True

            elif key == "s":
                human.move(1, 0)
                screenDirty = True

            elif key == "d":
                human.move(0, 1)
                screenDirty = True

            elif key == "e":
                playerLocation = human.get_position()
                theBomb = Bomb(gameMap, playerLocation)
                theBomb.bomb_plant()
                bombPlanted = True
                screenDirty = True

            elif key == "q":
                clear_screen()
                print("Quit")
                break
        if human.check_collision(enemies):
            human.die()

        currentTime = time.time()
        if currentTime - lastTick >= tickRate:
            enemy1.move()
            enemy2.move()
            if bombPlanted and theBomb:
                theBomb.check_explosion()
            screenDirty = True
            lastTick = currentTime

        if screenDirty:
            print_screen_centered(gameMap)
            screenDirty = False

        time.sleep(0.01)


if __name__ == "__main__":
    # main()
    print(help("map"))