
from PokerClasses.Card import Card
from PokerClasses.Hand import Hand


def count(hand: Hand, card: Card) -> int:
    return hand.cards.count(card)


def get_best_hand(hand: Hand) -> Hand:
    from Functions.CompareHands import compare_hands
    from itertools import combinations
    from Exceptions.Exceptions import TiedHandsException

    # assuming more than 5 cards hand, get all 5 cards hand and decides the best one, testing each one sequentially
    all_hands = list(combinations(hand, 5))
    best_hand = Hand(*all_hands[0])
    for var_hand in all_hands[1:]:
        var_hand = Hand(*var_hand)
        try:
            best_hand = var_hand if compare_hands(best_hand, var_hand) == var_hand else best_hand
        except TiedHandsException:
            continue
    return best_hand


def order_abbr(abbr1: str, abbr2: str) -> str:
    royals = ('A', 'K', 'Q', 'J', 'T')
    match abbr1, abbr2:
        case x, y if (x in royals) and (y in royals):
            i = royals.index(x)
            j = royals.index(y)
            return royals[min(i, j)] + royals[max(i, j)]
        case x, y if x in royals:
            return x + y
        case x, y if y in royals:
            return y + x
        case x, y:
            return str(max(int(x), int(y))) + str(min(int(x), int(y)))

