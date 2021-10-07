
from functools import total_ordering

from PokerClasses.Suit import Suit


@total_ordering
class Card:

    def __init__(self, card_value: int, suit: Suit):
        self.value = card_value
        self.suit = suit

    def __str__(self):
        if self.value == 1:
            return f"Ace of {self.suit.name}"
        elif self.value == 11:
            return f"Jack of {self.suit.name}"
        elif self.value == 12:
            return f"Queen of {self.suit.name}"
        elif self.value == 13:
            return f"King of {self.suit.name}"
        else:
            return f"{self.value} of {self.suit.name}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if type(other) == Card:
            return self.value == other.value
        elif type(other) == int:
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(other) == Card:
            return self.value < other.value
        elif type(other) == int:
            return self.value < other
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.__repr__())
