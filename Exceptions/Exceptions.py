
from PokerClasses.Hand import Hand


class CardNotFoundError(Exception):
    pass


class TiedHandsException(Exception):
    hand = None

    def __init__(self, hand: Hand = None):
        self.hand = hand
