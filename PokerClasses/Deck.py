
from random import shuffle
from PokerClasses.Card import Card
from PokerClasses.Suit import Suit


class Deck:

    def __init__(self) -> None:
        self.cards_list = list()
        for value in range(1, 14):
            for suit in Suit:
                self.cards_list.append(Card(value, suit))

    def __str__(self) -> str:
        string = ""
        for i in self.cards_list:
            string += f"{i}\n"
        return string

    def __getitem__(self, item: int) -> Card:
        return self.cards_list[item]

    def __setitem__(self, key: int, value: Card) -> None:
        self.cards_list[key] = value

    def __iter__(self):
        return self.cards_list.__iter__()

    def get_n_cards(self, n: int) -> list[Card]:
        n_cards = list()
        for _ in range(n):
            n_cards.append(self.cards_list.pop())
        return n_cards

    def add_card(self, card: Card, *args: Card) -> None:
        self.cards_list.append(card)
        for other_card in args:
            self.cards_list.append(other_card)

    def pop(self, index=0) -> Card:
        return self.cards_list.pop(index)

    def shuffle(self) -> None:
        shuffle(self.cards_list)
