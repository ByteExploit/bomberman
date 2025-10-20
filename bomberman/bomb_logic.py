from tbi import GridSymbols, Wasd
import time


class Bomb:
    def __init__(self, gameMap, bombLocation=[1, 1], radius=4):
        self.bombY, self.bombX = bombLocation
        self.gameMap = gameMap
        self.radius = radius
        self.exploded = False
        self.plantedTime = time.time()

    def can_plant(self):
        return self.gameMap.grid[self.bombY][self.bombX] == GridSymbols.EMPTY

    def bomb_plant(self):
        if self.can_plant():
            self.gameMap.grid[self.bombY][self.bombX] = GridSymbols.BOMB

    def check_explosion(self):
        if time.time() - self.plantedTime >= 3 and not self.exploded:
            self.bomb_explode()

    def bomb_explode(self):
        if time.time() - self.plantedTime >= 3 and not self.exploded:
            for height, width in Wasd.DIRECTIONS.values():
                for step in range(self.radius + 1):
                    y = self.bombY + height * step
                    x = self.bombX + width * step
                    if not 0 <= y < self.gameMap.height and 0 <= x < self.gameMap.width:
                        break
                    elif self.gameMap.grid[y][x] == GridSymbols.BUILDING:
                        break
                    elif self.gameMap.grid[y][x] == GridSymbols.BARRICADE:
                        self.gameMap.grid[y][x] = GridSymbols.EMPTY
                        break
            self.gameMap.grid[self.bombY][self.bombX] = GridSymbols.EMPTY
            self.exploded = True


def main():
    pass


if __name__ == "__main__":
    main()
