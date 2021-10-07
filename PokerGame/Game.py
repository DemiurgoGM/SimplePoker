
from Functions.UtilsFuncs import get_best_hand
from PokerClasses.Deck import Deck
from PokerClasses.Hand import Hand
from PokerGame.Player import Player


class Game:

    def __init__(self):
        self.deck = Deck()
        self.player1 = None
        self.player2 = None
        self.pot = 0

    def pre_flop(self):
        # jogo comeca, dar shuffle no deck e dar aos jogadores suas primeiras cartas
        # PRE-FLOP
        self.deck.shuffle()
        self.pot = 0
        self.player1 = Player(Hand(self.deck[0], self.deck[1]))

        self.player2 = Player(Hand(self.deck[2], self.deck[3]))
        # Dada as duas cartas, rodada de apostas
        # para debug, printar todos os estagios
        print("-" * 8 + " PRE-FLOP " + "-" * 8)
        self.get_players()
        # TODO para simplificar, pular rodada de apostas
        self.do_bets()

    def start(self):
        while True:

            self.pre_flop()

            self.flop()

            self.turn()

            self.river()

            # GAME FINISH
            self.player1.set_hand(get_best_hand(self.player1.get_hand()))
            self.player2.set_hand(get_best_hand(self.player2.get_hand()))

            self.get_winner()
            # RESTART
            print('/*\\' * 5 + ' FIM ' + '/*\\' * 5)
            input('>')

    def get_players(self):
        print(f"""
        Jogador 1: {self.player1.get_hand()}
        Jogador 2: {self.player2.get_hand()}
        """)

    def do_bets(self):
        pass

    def get_winner(self):
        from Exceptions.Exceptions import TiedHandsException
        from Functions.CompareHands import compare_hands
        try:
            winner = compare_hands(self.player1.get_hand(), self.player2.get_hand())
            if winner == self.player1.get_hand():
                print("JOGADOR 1 VENCEU!!!")
            else:
                print("JOGADOR 2 VENCEU!!!")
            print("Mão vencedora:\n")
            print(winner)
        except TiedHandsException as e:
            print(f"EMPATE!\nMão: {e.hand}")

    def flop(self):
        # FLOP
        for card in self.deck.cards_list[4:7]:
            self.player1.get_hand().add(card)
            self.player2.get_hand().add(card)

        # para debug, printar todos os estagios
        print("-" * 8 + " FLOP " + "-" * 8)
        self.get_players()
        # TODO para simplificar, pular rodada de apostas
        self.do_bets()

    def turn(self):
        # TURN
        self.player1.get_hand().add(self.deck[7])
        self.player2.get_hand().add(self.deck[7])
        # para debug, printar todos os estagios
        print("-" * 8 + " TURN " + "-" * 8)
        self.get_players()
        # TODO para simplificar, pular rodada de apostas
        self.do_bets()

    def river(self):
        # RIVER
        self.player1.get_hand().add(self.deck[8])
        self.player2.get_hand().add(self.deck[8])
        # para debug, printar todos os estagios
        print("-" * 8 + " RIVER " + "-" * 8)
        self.player1.get_hand().sort()
        self.player2.get_hand().sort()
        self.get_players()
        # TODO para simplificar, pular rodada de apostas
        self.do_bets()
