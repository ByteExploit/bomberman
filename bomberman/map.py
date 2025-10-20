import random
from tbi import GridSymbols


class Map:
    def __init__(self, mapSize):
        self.height, self.width = mapSize
        self.grid = [
            [GridSymbols.EMPTY for _ in range(self.width)] for _ in range(self.height)
        ]

    def add_borders(self):
        for h in range(self.height):
            for w in range(self.width):
                if w == 0 or w == self.width - 1 or h == 0 or h == self.height - 1:
                    self.grid[h][w] = GridSymbols.BORDER

    def add_buildings(self):
        for h in range(self.height):
            for w in range(self.width):
                if w % 2 == 0 and h % 2 == 0:
                    self.grid[h][w] = GridSymbols.BUILDING

    def add_barricade(self):
        for h in range(self.height):
            for w in range(self.width):
                if random.randint(1, 3) == 1:
                    self.grid[h][w] = GridSymbols.BARRICADE

    def clear_spawn(self, spawnY=1, spawnX=1, radius=1):
        for h in range(-radius, radius + 1):
            for w in range(-radius, radius + 1):
                y, x = h + spawnY, w + spawnX
                if self.grid[y][x] == GridSymbols.BARRICADE:
                    self.grid[y][x] = GridSymbols.EMPTY


def map_pop_all(spawnLocation, gameMap):
    gameMap.add_barricade()
    gameMap.add_buildings()
    gameMap.add_borders()
    gameMap.clear_spawn(*spawnLocation)
    return gameMap


def main():
    pass


if __name__ == "__main__":
    main()
