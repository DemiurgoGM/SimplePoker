
from Exceptions.Exceptions import TiedHandsException
from Functions.DefineHand import *
from Functions.TypeOfPokerHand import PokerHand
from PokerClasses.Hand import Hand


def compare_hands_values(hand_one: Hand, hand_two: Hand) -> Hand:  # assuming all different cards
    # if the hand received is ordered, use this
    # try for Ace
    if (hand_one[0].value == 1 and hand_one[-1].value == 13) and hand_two[0].value != 1:
        return hand_one
    elif hand_one[0].value != 1 and (hand_two[0].value == 1 and hand_two[0].value == 13):
        return hand_two
    else:
        for i in range(1, len(hand_one.get_cards()) + 1):
            i = -i
            if hand_one[i].value > hand_two[i].value:
                return hand_one
            elif hand_two[i].value > hand_one[i].value:
                return hand_two
    raise TiedHandsException(hand_one)


def compare_pair(hand_one: Hand, hand_two: Hand) -> Hand:
    hand_one_pair_value = get_bigger_value_from_paired_hand(hand_one)
    hand_two_pair_value = get_bigger_value_from_paired_hand(hand_two)
    if hand_one_pair_value > hand_two_pair_value:
        return hand_one
    elif hand_two_pair_value > hand_one_pair_value:
        return hand_two
    else:
        hand_one_unrepeated = get_unrepeated_hand_values(hand_one)
        hand_two_unrepeated = get_unrepeated_hand_values(hand_two)
        while hand_one_unrepeated.count(1) > 0:
            hand_one_unrepeated.remove(1)
            hand_one_unrepeated.append(14)
        while hand_two_unrepeated.count(1) > 0:
            hand_two_unrepeated.remove(1)
            hand_two_unrepeated.append(14)
        hand_one_unrepeated.sort()
        hand_two_unrepeated.sort()
        for i in range(1, len(hand_one_unrepeated) + 1):
            i = -i
            if hand_one_unrepeated[i] > hand_two_unrepeated[i]:
                return hand_one
            elif hand_two_unrepeated[i] > hand_one_unrepeated[i]:
                return hand_two
    raise TiedHandsException(hand_one)


def compare_quad(hand_one: Hand, hand_two: Hand) -> Hand:
    hand_one_quad_card = get_quad_card_value(hand_one)
    hand_two_quad_card = get_quad_card_value(hand_two)
    if hand_one_quad_card == hand_two_quad_card:  # if same quad
        hand_one_quad_kicker = get_quad_kicker_value(hand_one)
        hand_two_quad_kicker = get_quad_kicker_value(hand_two)
        if hand_one_quad_kicker > hand_two_quad_kicker:
            return hand_one
        elif hand_two_quad_kicker > hand_one_quad_kicker:
            return hand_two
        else:
            raise TiedHandsException(hand_one)
    # different quads...
    elif hand_one_quad_card > hand_two_quad_card:
        return hand_one
    else:
        return hand_two


def compare_full_house(hand_one: Hand, hand_two: Hand) -> Hand:
    hand_one_three_card = get_full_house_three_card_value(hand_one)
    hand_two_three_card = get_full_house_three_card_value(hand_two)
    if hand_one_three_card > hand_two_three_card:  # bigger three card wins
        return hand_one
    elif hand_two_three_card > hand_one_three_card:
        return hand_two

    # same three card, compare two-card...
    hand_one_two_card = get_full_house_two_card_value(hand_one)
    hand_two_two_card = get_full_house_two_card_value(hand_two)
    if hand_one_two_card > hand_two_two_card:
        return hand_one
    elif hand_two_two_card > hand_one_two_card:
        return hand_two
    raise TiedHandsException(hand_one)


def compare_three_equal(hand_one: Hand, hand_two: Hand) -> Hand:
    # compare the triple
    hand_one_three_card = get_three_equal_card_value(hand_one)
    hand_two_three_card = get_three_equal_card_value(hand_two)
    if hand_one_three_card > hand_two_three_card:
        return hand_one
    elif hand_two_three_card > hand_one_three_card:
        return hand_two
    else:
        # compare the rest of the hand
        hand_one_cards = get_unrepeated_hand_values(hand_one)
        hand_two_cards = get_unrepeated_hand_values(hand_two)
        if hand_one_cards.count(1) > 0:
            hand_one_cards[hand_one_cards.index(1)] = 14
        if hand_two_cards.count(1) > 0:
            hand_two_cards[hand_two_cards.index(1)] = 14
        hand_one_cards.sort()
        hand_two_cards.sort()
        for i in range(1, len(hand_one_cards) + 1):
            i = -i
            if hand_one_cards[i] > hand_two_cards[i]:
                return hand_one
            elif hand_two_cards[i] > hand_one_cards[i]:
                return hand_two
    raise TiedHandsException(hand_one)


def compare_two_pair(hand_one: Hand, hand_two: Hand) -> Hand:
    match (get_bigger_value_from_paired_hand(hand_one),
           get_bigger_value_from_paired_hand(hand_two)):
        case (1, x) if x != 1:
            return hand_one
        case (x, 1) if x != 1:
            return hand_two
        case (x, y) if x > y:
            return hand_one
        case (x, y) if y > x:
            return hand_two

    match (get_smaller_value_from_paired_hand(hand_one),
           get_smaller_value_from_paired_hand(hand_two)):
        case (1, x) if x != 1:
            return hand_one
        case (x, 1) if x != 1:
            return hand_two
        case (x, y) if x > y:
            return hand_one
        case (x, y) if y > x:
            return hand_two

    match (get_unrepeated_hand_values(hand_one)[0],
           get_unrepeated_hand_values(hand_two)[0]):
        case (1, x) if x != 1:
            return hand_one
        case (x, 1) if x != 1:
            return hand_two
        case (x, y) if x > y:
            return hand_one
        case (x, y) if y > x:
            return hand_two

    raise TiedHandsException(hand_one)

    # OLD
    # hand_one_big_value = get_bigger_value_from_paired_hand(hand_one)
    # hand_two_big_value = get_bigger_value_from_paired_hand(hand_two)
    # if hand_one_big_value > hand_two_big_value:
    #     return hand_one
    # elif hand_two_big_value > hand_one_big_value:
    #     return hand_two
    # else:
    #     hand_one_small_value = get_smaller_value_from_paired_hand(hand_one)
    #     hand_two_small_value = get_smaller_value_from_paired_hand(hand_two)
    #     if hand_one_small_value > hand_two_small_value:
    #         return hand_one
    #     elif hand_two_small_value > hand_one_small_value:
    #         return hand_two
    #     else:
    #         hand_one_unrepeated = get_unrepeated_hand_values(hand_one)[0]
    #         hand_two_unrepeated = get_unrepeated_hand_values(hand_two)[0]
    #
    #         match (hand_one_unrepeated, hand_two_unrepeated):
    #             case (1, x) if x != 1:
    #                 return hand_one
    #             case (x, 1) if x != 1:
    #                 return hand_two
    #             case (x, y) if x > y:
    #                 return hand_one
    #             case (x, y) if y > x:
    #                 return hand_two
    #             case (_, _):
    #                 raise TiedHandsException(hand_one)


# def compare_hands(hand_one: Hand, hand_two: Hand) -> Hand:
#     # sorting before all...
#     hand_one.sort()
#     hand_two.sort()
#     if is_straight_flush(hand_one):
#         if is_straight_flush(hand_two):
#             return compare_hands_values(hand_one, hand_two)
#         else:
#             return hand_one
#     elif is_straight_flush(hand_two):
#         return hand_two
#     elif is_quad(hand_one):  # if quad
#         if is_quad(hand_two):  # if 2 quads
#             return compare_quad(hand_one, hand_two)
#         else:
#             return hand_one
#     elif is_quad(hand_two):
#         return hand_two
#     elif is_full_house(hand_one):
#         if is_full_house(hand_two):  # if both full houses
#             return compare_full_house(hand_one, hand_two)
#         else:
#             return hand_one
#     elif is_full_house(hand_two):
#         return hand_two
#     elif is_flush(hand_one):
#         if is_flush(hand_two):
#             return compare_hands_values(hand_one, hand_two)
#         else:
#             return hand_one
#     elif is_flush(hand_two):
#         return hand_two
#     elif is_straight(hand_one):
#         if is_straight(hand_two):
#             return compare_hands_values(hand_one, hand_two)
#         else:
#             return hand_one
#     elif is_straight(hand_two):
#         return hand_two
#     elif is_three_equals(hand_one):
#         if is_three_equals(hand_two):
#             return compare_three_equal(hand_one, hand_two)
#         else:
#             return hand_one
#     elif is_three_equals(hand_two):
#         return hand_two
#     elif is_two_pair(hand_one):
#         if is_two_pair(hand_two):
#             return compare_two_pair(hand_one, hand_two)
#         else:
#             return hand_one
#     elif is_two_pair(hand_two):
#         return hand_two
#     elif is_pair(hand_one):
#         if is_pair(hand_two):
#             return compare_pair(hand_one, hand_two)
#         else:
#             return hand_one
#     elif is_pair(hand_two):
#         return hand_two
#     else:  # Bigger kicker wins, if equals see other big card...
#         return compare_hands_values(hand_one, hand_two)


# returns the better hand
def compare_hands(hand_one: Hand, hand_two: Hand) -> Hand:
    match (get_type_hand(hand_one), get_type_hand(hand_two)):
        # Different levels of hands
        case (x, y) if x.value > y.value:
            return hand_one
        case (x, y) if y.value > x.value:
            return hand_two
        # Same level
        # If you can compare the values directly...
        case (PokerHand.STRAIGHT_FLUSH | PokerHand.STRAIGHT | PokerHand.FLUSH | PokerHand.HIGH_CARD, _):
            return compare_hands_values(hand_one, hand_two)
        # hands with duplicates...
        case (PokerHand.PAIR, _):
            return compare_pair(hand_one, hand_two)
        case (PokerHand.TWO_PAIR, _):
            return compare_two_pair(hand_one, hand_two)
        case (PokerHand.THREE_EQUAL, _):
            return compare_three_equal(hand_one, hand_two)
        case (PokerHand.FULL_HOUSE, _):
            return compare_full_house(hand_one, hand_two)
        case (PokerHand.QUAD, _):
            return compare_quad(hand_one, hand_two)
