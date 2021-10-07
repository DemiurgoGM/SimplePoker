
from PokerClasses.Card import Card
from PokerClasses.Hand import Hand


def count(hand: Hand, card: Card) -> int:
    return hand.cards.count(card)


def get_best_hand(hand: Hand) -> Hand:
    from Functions.CompareHands import compare_hands
    from itertools import combinations
    from Exceptions.Exceptions import TiedHandsException

    # assuming more than 5 cards hand, get all 5 cards hand and decides the best one, testing each one sequentially
    all_hands = list(set(combinations(hand, 5)))
    best_hand = Hand(*all_hands[0])
    for var_hand in all_hands[1:]:
        var_hand = Hand(*var_hand)
        try:
            best_hand = var_hand if compare_hands(best_hand, var_hand) == var_hand else best_hand
        except TiedHandsException:
            continue
    return best_hand
