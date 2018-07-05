from game.dice_roll import roll
import collections


class TextGame:
    # Constants:
    class Stats:
        NAMES = ("pow", "brn", "wis", "agi")

        def __init__(self, pow=10):
            pass

    def __init__(self, char_name):
        self.character = char_name
        self.stats = self.Stats()
