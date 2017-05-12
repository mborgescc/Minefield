class Square:

    MINE = 0
    DOUBT = 1
    OPEN = 2
    CLOSED = 3

    # Defines if has mine and initializes it as a closed square
    def __init__(self, has_mine):
        self.has_mine = has_mine
        self._values = {
            "MINE": self.MINE,
            "DOUBT": self.DOUBT,
            "OPEN": self.OPEN,
            "CLOSED": self.CLOSED
        }
        self.value = self._values["CLOSED"]
        self.number = -1  # Not initialized

    @property
    def value_name(self):
        for name, value in self._values:
            if self.value == value:
                return name

    def set_value(self, value_name):
        self.value = self._values[value_name]


class Field:

    EXTRA_SMALL = 10
    SMALL = 50
    LARGE = 100
    EXTRA_LARGE = 200
    WORLD = 500
    GALAXY = 1000

    EASY = 2.0
    MEDIUM = 3.5
    HARD = 5.0
    EXTRA_HARD = 6.0
    EXTREME = 7.0
    IMPOSSIBLE = 8.5

    def __init__(self, chosen_size, chosen_level):
        self._sizes = {
            "EXTRA_SMALL": self.EXTRA_SMALL,
            "SMALL": self.SMALL,
            "LARGE": self.LARGE,
            "EXTRA_LARGE": self.EXTRA_LARGE,
            "WORLD": self.WORLD,
            "GALAXY": self.GALAXY,
        }
        self._levels = {
            "EASY": self.EASY,
            "MEDIUM": self.MEDIUM,
            "HARD": self.HARD,
            "EXTRA_HARD": self.EXTRA_HARD,
            "EXTREME": self.EXTREME,
            "IMPOSSIBLE": self.IMPOSSIBLE,
        }
        self.size = self._sizes[chosen_size]
        self.level = self._levels[chosen_level]
        self.squares = []
        for i in xrange(self.size):
            row = []
            for j in xrange(self.size):
                row.append(Square(self._mine_decider(self.level)))
            self.squares.append(row)

    @staticmethod
    def _mine_decider(difficulty_level):
        import random
        return difficulty_level > random.uniform(0.0, 10.0)

    def choose(self, i, j):
        if self.squares[i+1][j+1].has_mine:
            return True
        else:
            return False

    def calculate_number(self, i, j):
        raise NotImplementedError
