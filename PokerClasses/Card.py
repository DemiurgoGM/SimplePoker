
from functools import total_ordering

from PokerClasses.Suit import Suit


@total_ordering
class Card:

    def __init__(self, card_value: int, suit: Suit) -> None:
        self.value = card_value
        self.suit = suit

    def __str__(self) -> str:
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

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        if type(other) == Card:
            return self.value == other.value
        elif type(other) == int:
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if type(other) == Card:
            return self.value < other.value
        elif type(other) == int:
            return self.value < other
        else:
            return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def abbr(self) -> str:
        match self.value:
            case x if x == 1:
                return "A"
            case x if x == 10:
                return "T"
            case x if x == 11:
                return "J"
            case x if x == 12:
                return "Q"
            case x if x == 13:
                return "K"
            case _:
                return str(self.value)
