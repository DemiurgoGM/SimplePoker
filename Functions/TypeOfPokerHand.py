
from enum import Enum


class PokerHand(Enum):
    STRAIGHT_FLUSH = 100
    QUAD = 90
    FULL_HOUSE = 80
    FLUSH = 70
    STRAIGHT = 60
    THREE_EQUAL = 50
    TWO_PAIR = 40
    PAIR = 30
    HIGH_CARD = 20
