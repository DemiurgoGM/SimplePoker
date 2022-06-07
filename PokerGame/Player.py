from dataclasses import dataclass

from PokerClasses.Card import Card
from PokerClasses.Hand import Hand


@dataclass
class Player:
    _hand: Hand = None
    _chips: int = 0

    def __init__(self, hand: Hand = None, chips: int = 1000):
        self._hand = hand
        self._chips = chips

    @property
    def hand(self) -> Hand:
        return self._hand

    @hand.setter
    def hand(self, hand: Hand) -> None:
        self._hand = hand

    @property
    def chips(self) -> int:
        return self._chips

    @chips.setter
    def chips(self, chips: int) -> None:
        if chips < 0:
            self._chips = 0
        else:
            self._chips = chips

    def __sub__(self, other) -> int:
        if type(other) == int:
            sub = self.chips - other
        elif type(other) == Player:
            sub = self.chips - other.chips
        else:
            raise NotImplementedError
        if sub < 0:
            return 0
        else:
            return sub

    def __add__(self, other) -> int:
        if type(other) == int:
            return self.chips + other
        elif type(other) == Player:
            return self.chips + other.chips
        else:
            raise NotImplementedError

    def is_all_in(self) -> bool:
        return self.chips == 0

    def has_amount(self, amount: int) -> bool:
        return self.chips >= amount

    def add(self, card: Card) -> None:
        self.hand.add(card)

    def sort(self) -> None:
        self.hand.sort()
