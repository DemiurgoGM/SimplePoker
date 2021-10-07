
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
        self.cards.sort()
        return self.cards

    def sort(self) -> None:
        self.cards.sort()

    def __getitem__(self, item: int) -> Card:
        return self.cards[item]

    def __setitem__(self, key: int, value: Card) -> None:
        self.cards[key] = value

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__repr__())

    def get_cards_values(self) -> list[int]:
        return [x.value for x in self.cards]
