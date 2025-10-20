class GridSymbols:
    EMPTY = "."
    ENEMY = "E"
    HUMAN = "P"
    BORDER = "W"
    BUILDING = "B"
    BARRICADE = "b"
    BOMB = "H"
    SIGHT = ","


class Wasd:
    DIRECTIONS = {
        "w": (-1, 0),
        "s": (1, 0),
        "a": (0, -1),
        "d": (0, 1),
    }
