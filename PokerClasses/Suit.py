
from enum import Enum, auto, unique


@unique
class Suit(Enum):
    Hearts = auto()
    Clubs = auto()
    Diamonds = auto()
    Spades = auto()
