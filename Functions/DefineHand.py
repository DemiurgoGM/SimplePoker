
from Exceptions.Exceptions import CardNotFoundError
from Functions.TypeOfPokerHand import PokerHand
from Functions.UtilsFuncs import count
from PokerClasses.Hand import Hand


def get_type_hand(hand: Hand) -> PokerHand:
    hand.sort()
    if is_straight_flush(hand):
        return PokerHand.STRAIGHT_FLUSH
    elif is_quad(hand):
        return PokerHand.QUAD
    elif is_full_house(hand):
        return PokerHand.FULL_HOUSE
    elif is_flush(hand):
        return PokerHand.FLUSH
    elif is_straight(hand):
        return PokerHand.STRAIGHT
    elif is_three_equals(hand):
        return PokerHand.THREE_EQUAL
    elif is_two_pair(hand):
        return PokerHand.TWO_PAIR
    elif is_pair(hand):
        return PokerHand.PAIR
    else:
        return PokerHand.HIGH_CARD


def is_straight_flush(hand: Hand) -> bool:
    return is_straight(hand) and is_flush(hand)


def is_quad(hand: Hand) -> bool:  # if the hand received is ordered, use this
    return count(hand, hand[0]) == 4 or count(hand, hand[-1]) == 4


# def isQuad(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     for i in range(2):
#         if cards_value.count(cards_value[i]) == 4:
#             return True
#     return False


def get_quad_kicker_value(hand: Hand) -> int:  # if the hand received is ordered, use this
    if count(hand, hand[0]) == 4:
        value = hand[-1]
    elif count(hand, hand[-1]) == 4:
        value = hand[0]
    else:
        raise CardNotFoundError
    return 14 if value == 1 else value


# def getQuadKicker(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     value = -1
#     if cards_value.count(cards_value[0]) == 4:
#         value = cards_value[-1]
#     elif cards_value.count(cards_value[-1]) == 4:
#         value = cards_value[0]
#     return 14 if value == 1 else value


def get_quad_card_value(hand: Hand) -> int:  # if the hand received is ordered, use this
    if count(hand, hand[0]) == 4:
        value = hand[0]
    elif count(hand, hand[-1]) == 4:
        value = hand[-1]
    else:
        raise CardNotFoundError
    return 14 if value == 1 else value


# def getQuadCard(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     value = -1
#     if cards_value.count(cards_value[0]) == 4:
#         value = cards_value[0]
#     elif cards_value.count(cards_value[-1]) == 4:
#         value = cards_value[-1]
#     return 14 if value == 1 else value


def is_full_house(hand: Hand) -> bool:  # if the hand received is ordered, use this
    return (count(hand, hand[0]) == 3 and count(hand, hand[-1]) == 2) or \
           (count(hand, hand[0]) == 2 and count(hand, hand[-1]) == 3)


# def isFullHouse(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     return (cards_value.count(cards_value[0]) == 3 and cards_value.count(cards_value[-1]) == 2) or \
#            (cards_value.count(cards_value[0]) == 2 and cards_value.count(cards_value[-1]) == 3)


def get_full_house_three_card_value(hand: Hand) -> int:  # if the hand received is ordered, use this
    if count(hand, hand[0]) == 3:
        value = hand[0]
    elif count(hand, hand[-1]) == 3:
        value = hand[-1]
    else:
        raise CardNotFoundError
    return 14 if value == 1 else value


# def getFullHouseThreeCard(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     value = -1
#     if cards_value.count(cards_value[0]) == 3:
#         value = cards_value[0]
#     elif cards_value.count(cards_value[-1]) == 3:
#         value = cards_value[-1]
#     return 14 if value == 1 else value


def get_full_house_two_card_value(hand: Hand) -> int:  # if the hand received is ordered, use this
    if count(hand, hand[0]) == 2:
        value = hand[0]
    elif count(hand, hand[-1]) == 2:
        value = hand[-1]
    else:
        raise CardNotFoundError
    return 14 if value == 1 else value


# def getFullHouseTwoCard(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     value = -1
#     if cards_value.count(cards_value[0]) == 2:
#         value = cards_value[0]
#     elif cards_value.count(cards_value[-1]) == 2:
#         value = cards_value[-1]
#     return 14 if value == 1 else value


def is_flush(hand: Hand) -> bool:
    first_card = hand[0]
    for card in hand.get_cards()[1:]:
        if card.suit != first_card.suit:
            return False
    return True


def is_straight(hand: Hand) -> bool:  # if the hand received is ordered, use this
    first_card_value = hand[0].value
    for card in hand.get_cards()[1:]:
        if card.value == first_card_value + 1 or (card.value == 10 and first_card_value == 1):
            first_card_value = card.value
            continue
        else:
            return False
    return True


# def isStraight(hand):  # if the hand received isn't ordered, use this instead
#     counter = 0
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     if cards_value[0] == 1 and cards_value[-1] == 13:
#         cards_value[0] = 14
#         cards_value.sort()
#     first_value = cards_value[0]
#     for value in cards_value[1:]:
#         if value == first_value + 1:
#             counter = counter + 1
#             first_value = value
#     return counter == 4


def is_three_equals(hand: Hand) -> bool:  # if the hand received is ordered, use this
    for i in range(3):
        if count(hand, hand[i]) == 3:
            return True
    return False


# def isThreeEquals(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     for i in range(3):
#         if cards_value.count(cards_value[i]) == 3:
#             return True
#     return False


def get_three_equal_card_value(hand: Hand) -> int:  # if the hand received is ordered, use this
    for i in range(3):
        if count(hand, hand[i]) == 3:
            return hand[i] if hand[i] != 1 else 14
    raise CardNotFoundError


# def getThreeEqualCard(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     for i in range(3):
#         if cards_value.count(cards_value[i]) == 3:
#             return cards_value[i] if cards_value[i] != 1 else 14
#     return -1  # didn't find the repeating card.

def get_unrepeated_hand_values(hand: Hand) -> list[int]:
    cards_values = hand.get_cards_values()
    return sorted([x for x in cards_values if cards_values.count(x) == 1])


def is_two_pair(hand: Hand) -> bool:  # if the hand received is ordered, use this
    counter = 0
    for card in hand.get_cards()[::2]:
        if count(hand, card) == 2:
            counter = counter + 1
    return counter == 2


# def isTwoPair(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     counter = 0
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     for value in cards_value:
#         if cards_value.count(value) == 2:
#             counter = counter + 1
#             cards_value.remove(value)
#     return counter == 2

def get_values_from_paired_hand(hand: Hand) -> list[int]:  # if the hand received is ordered, use this
    pair_values = list()
    for card in hand.get_cards()[::2]:
        if count(hand, card) == 2:
            pair_values.append(14 if card.value == 1 else card.value)
    return pair_values


def get_bigger_value_from_paired_hand(hand: Hand) -> int:
    return max(get_values_from_paired_hand(hand))


# def getBiggerValueFromPairedHand(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     pair_values = list()
#     for card in hand:
#         cards_value.append(card.value)
#     while cards_value.count(1) > 0:
#         cards_value.remove(1)
#         cards_value.append(14)
#     for i in range(2, 15):
#         if cards_value.count(i) > 1:
#             pair_values.append(i)
#     return max(pair_values)


def get_smaller_value_from_paired_hand(hand: Hand) -> int:
    return min(get_values_from_paired_hand(hand))


# def getSmallerValueFromPairedHand(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     pair_values = list()
#     for card in hand:
#         cards_value.append(card.value)
#     while cards_value.count(1) > 0:
#         cards_value.remove(1)
#         cards_value.append(14)
#     for i in range(1, 14):
#         if cards_value.count(i) > 1:
#             pair_values.append(i)
#     return min(pair_values)


def is_pair(hand: Hand) -> bool:  # a better name is 'has_pair'...
    for card in hand.get_cards()[::2]:
        if count(hand, card) == 2:
            return True
    return False

# def isPair(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     for i in range(4):
#         if cards_value.count(cards_value[i]) == 2:
#             return True
#     return False


# def getKicker(hand):  # if the hand received is ordered, use this
#     return 14 if hand[0] == 1 else hand[-1]


# def getKicker(hand):  # if the hand received isn't ordered, use this
#     cards_value = list()
#     for card in hand:
#         cards_value.append(card.value)
#     cards_value.sort()
#     return 14 if cards_value[0] == 1 else cards_value[-1]
