import random
from tbi import GridSymbols, Wasd


class Enemy:
    def __init__(self, gameMap, startPos=(1, 1)):
        self.y, self.x = startPos
        self.gameMap = gameMap
        self.lastDir = None

    def spawn(self):
        self.gameMap.grid[self.y][self.x] = GridSymbols.ENEMY

    def move(self):
        directions = list(Wasd.DIRECTIONS.values())
        chance = []
        for dy, dx in directions:
            if self.lastDir and (dy, dx) == (-self.lastDir[0], -self.lastDir[1]):
                chance.append(1)
            elif self.lastDir and (dy, dx) == self.lastDir:
                chance.append(6)
            else:
                chance.append(3)

        dy, dx = random.choices(directions, weights=chance, k=1)[0]
        newY, newX = self.y + dy, self.x + dx
        if 0 <= newY < self.gameMap.height and 0 <= newX < self.gameMap.width:
            if self.gameMap.grid[newY][newX] == (
                GridSymbols.EMPTY or GridSymbols.HUMAN
            ):
                self.gameMap.grid[self.y][self.x] = GridSymbols.EMPTY
                self.y, self.x = newY, newX
                self.gameMap.grid[self.y][self.x] = GridSymbols.ENEMY
                self.lastDir = (dy, dx)

    def get_position(self):
        return self.y, self.x
