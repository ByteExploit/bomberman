from tbi import GridSymbols, Wasd


class Player:
    def __init__(self, gameMap, spawnPos=(1, 1)):
        self.playerY, self.playerX = spawnPos
        self.gameMap = gameMap
        self.alive = True

    def can_move(self):
        for height, width in Wasd.DIRECTIONS:
            y = self.playerY + height
            x = self.playerX + width
            if 0 <= y < self.gameMap.height and 0 <= x < self.gameMap.width:
                if self.gameMap.grid[y][x] == GridSymbols.EMPTY:
                    return True
        return False

    def move(self, dy, dx):
        newY = dy + self.playerY
        newX = dx + self.playerX
        if 0 <= newY < self.gameMap.height and 0 <= newX < self.gameMap.width:
            if self.gameMap.grid[newY][newX] == GridSymbols.EMPTY:
                self.gameMap.grid[self.playerY][self.playerX] = GridSymbols.EMPTY
                self.playerY, self.playerX = newY, newX
                self.gameMap.grid[self.playerY][self.playerX] = GridSymbols.HUMAN

    def get_position(self):
        return self.playerY, self.playerX

    def check_collision(self, enemies):
        for enemy in enemies:
            if (self.playerY, self.playerX) == enemy.get_position():
                return True
        return False

    def spawn(self):
        self.gameMap.grid[self.playerY][self.playerX] = GridSymbols.HUMAN
        return self.gameMap.grid

    def die(self):
        self.alive = False


def test_player():
    main()


def main():
    pass
