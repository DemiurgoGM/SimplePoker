
from PokerClasses.Hand import Hand


class Player:
    # missing bank
    def __init__(self, hand: Hand = None):
        self.hand = hand

    def set_hand(self, hand: Hand) -> None:
        self.hand = hand

    def get_hand(self) -> Hand:
        return self.hand


