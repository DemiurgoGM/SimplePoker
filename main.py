
from Functions.UtilsFuncs import get_best_hand
from PokerClasses.Card import Card
from PokerClasses.Hand import Hand
from PokerClasses.Suit import Suit
from PokerGame.Game import Game

if __name__ == '__main__':
    game = Game()
    game.start()
    # hand = Hand(
    #     Card(2, Suit.Hearts),
    #     Card(3, Suit.Diamonds),
    #     Card(3, Suit.Spades),
    #     Card(3, Suit.Clubs),
    #     Card(11, Suit.Diamonds),
    #     Card(11, Suit.Hearts),
    #     Card(13, Suit.Diamonds)
    # )
    # print(get_full_house_three_card_value(hand))

