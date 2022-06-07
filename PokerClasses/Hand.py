from typing import Iterator

from PokerClasses.Card import Card


class Hand:

    def __init__(self, card1: Card, card2: Card, *args: Card) -> None:
        self.cards = list()
        self.cards.append(card1)
        self.cards.append(card2)
        for arg in args:
            self.cards.append(arg)
        self.sort()

    def __str__(self) -> str:
        return ", ".join([card.__str__() for card in self.cards])

    def add(self, card: Card) -> None:
        self.cards.append(card)

    def get_cards(self) -> list[Card]:
        self.sort()
        return self.cards

    def sort(self) -> None:
        self.cards.sort()

    def __getitem__(self, item: int) -> Card:
        return self.cards[item]

    def __setitem__(self, key: int, value: Card) -> None:
        self.cards[key] = value

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __iter__(self) -> Iterator:
        return iter(self.cards)

    def get_cards_values(self) -> list[int]:
        return [x.value for x in self.cards]

    def abbr(self) -> str:
        from Functions.UtilsFuncs import order_abbr
        c1 = self.cards[0]
        c2 = self.cards[1]
        if c1.suit == c2.suit:
            suit = 's'
        elif c1.value == c2.value:
            suit = ''
        else:
            suit = 'o'
        c1 = c1.abbr()
        c2 = c2.abbr()
        c = order_abbr(c1, c2)
        return c + suit
