import math
from enum import Enum

from Functions.UtilsFuncs import get_best_hand
from PokerClasses.Deck import Deck
from PokerClasses.Hand import Hand
from PokerGame.Player import Player


class Table:
    def __init__(self,
                 player_bank_start: int = 1 * 10 ** 5,
                 blind: int = 400,
                 blind_increase_rate: int = -1,  # negative number, no increase
                 blind_increase_size: float = 0.5
                 ):
        self.game = Game(player_bank_start,
                         blind,
                         blind_increase_rate,
                         blind_increase_size)

    def play(self):
        self.game.start()


class Game:
    class GamePhase(Enum):
        PRE_FLOP = 1
        FLOP = 2
        TURN = 3
        RIVER = 4
        END = 5

    def __init__(self, player_bank_start: int = 1 * 10 ** 5,
                 blind: int = 400,
                 blind_increase_rate: int = -1,  # negative number, no increase
                 blind_increase_size: float = 0.5):
        self.deck = Deck()
        self.player1 = Player(hand=None, chips=player_bank_start)
        self.player2 = Player(hand=None, chips=player_bank_start)
        self.pot = 0
        self.blind = blind
        self.blind_increase_rate = 0
        self.BLIND_INCREASE_RATE_REFERENCE = blind_increase_rate
        self.blind_increase_size = blind_increase_size
        self.starter_player = 1
        self.round_over = False

    def start(self):
        while True:
            winner = self.pre_flop()
            if not self.round_over:
                winner = self.flop()
            if not self.round_over:
                winner = self.turn()
            if not self.round_over:
                winner = self.river()
            # GAME FINISH
            self.finish_game(winner is None, winner)

    def pre_flop(self) -> Player | None:
        # At the start of the game, shuffle the deck, reset the pot and give the players their hands
        # PRE-FLOP
        self.deck.shuffle()
        self.pot = 0

        self.player1 = Player(Hand(self.deck[0], self.deck[1]), self.player1.chips)
        self.player2 = Player(Hand(self.deck[2], self.deck[3]), self.player2.chips)

        print("-" * 8 + " PRE-FLOP " + "-" * 8)
        # to debug, getting players at all stages
        self.get_players()
        return self.do_bets(self.GamePhase.PRE_FLOP)

    def get_players(self):
        print(f"""
        Jogador 1: {self.player1.hand} | Chips: {self.player1.chips}
        Jogador 2: {self.player2.hand} | Chips: {self.player2.chips}
        """)

    def do_bets(self, phase: GamePhase = None) -> Player | None:
        player1_bets = 0
        player2_bets = 0

        def blinds():
            nonlocal player1_bets
            nonlocal player2_bets
            if self.starter_player > 0:
                player1 = self.player1
                player2 = self.player2
            else:
                player1 = self.player2
                player2 = self.player1
            og = player1.chips
            player1.chips = player1.chips - self.blind
            player1_bets = og - player1.chips
            self.pot += player1_bets

            # p2
            og = player2.chips
            player2.chips = player2.chips - self.blind // 2
            player2_bets = og - player2.chips
            self.pot += player2_bets

        def bets(is_pre_flop: bool = True):
            nonlocal player1_bets
            nonlocal player2_bets
            first_bet_round = True
            if self.starter_player > 0:
                player1 = self.player1
                player2 = self.player2
            else:
                player1 = self.player2
                player2 = self.player1
            if is_pre_flop:  # in pre_flop, the order of who bets first in inverted from the rest of the game
                while player1_bets != player2_bets or first_bet_round:
                    if player1_bets > player2_bets or first_bet_round:
                        while True:
                            player2_next_bet = int(input(f'Player ({player2}) small blind get bet: '))
                            if player2_next_bet < 0:
                                # Fold
                                self.round_over = True
                                return player1
                            elif player2_next_bet + player2_bets >= player1_bets and player2.has_amount(
                                    player2_next_bet):
                                og = player2.chips
                                player2.chips = player2.chips - player2_next_bet
                                bet = og - player2.chips
                                self.pot += bet
                                player2_bets += bet
                                break
                            else:
                                print(f"Invalid betting amount.")
                    if player1_bets < player2_bets or first_bet_round:
                        while True:
                            player1_next_bet = int(input(f'Player ({player1}) big blind get bet: '))
                            if player1_next_bet < 0:
                                # Fold
                                self.round_over = True
                                return player2
                            elif player1_bets + player1_next_bet >= player2_bets and player1.has_amount(
                                    player1_next_bet):
                                og = player1.chips
                                player1.chips = player1.chips - player1_next_bet
                                bet = og - player1.chips
                                self.pot += bet
                                player1_bets += bet
                                break
                            else:
                                print("Invalid betting amount.")
                        first_bet_round = False
            else:
                while player1_bets != player2_bets or first_bet_round:
                    if player1_bets < player2_bets or first_bet_round:
                        while True:
                            player1_next_bet = int(input(f'Player ({player1}) big blind get bet: '))
                            if player1_next_bet < 0:
                                # Fold
                                self.round_over = True
                                return player2
                            elif player1_bets + player1_next_bet >= player2_bets and player1.has_amount(
                                    player1_next_bet):
                                og = player1.chips
                                player1.chips = player1.chips - player1_next_bet
                                bet = og - player1.chips
                                self.pot += bet
                                player1_bets += bet
                                break
                            else:
                                print("Invalid betting amount.")
                    if player1_bets > player2_bets or first_bet_round:
                        while True:
                            player2_next_bet = int(input(f'Player ({player2}) small blind get bet: '))
                            if player2_next_bet < 0:
                                # Fold
                                self.round_over = True
                                return player1
                            elif player2_next_bet + player2_bets >= player1_bets and player2.has_amount(
                                    player2_next_bet):
                                og = player2.chips
                                player2.chips = player2.chips - player2_next_bet
                                bet = og - player2.chips
                                self.pot += bet
                                player2_bets += bet
                                break
                            else:
                                print(f"Invalid betting amount.")
                        first_bet_round = False

        if phase == self.GamePhase.PRE_FLOP:
            blinds()

        return bets(phase == self.GamePhase.PRE_FLOP)

    def get_winner(self):
        try:
            winner = compare_hands(self.player1.hand, self.player2.hand)
            if winner == self.player1.hand:
                self.player1.chips = self.player1.chips + self.pot
                print("JOGADOR 1 VENCEU!!!")
            else:
                self.player2.chips = self.player2.chips + self.pot
                print("JOGADOR 2 VENCEU!!!")
            print(f"Mão vencedora:\n{winner} | Ganhou um pot = {self.pot}")
        except TiedHandsException as e:
            self.player1.chips = self.player1.chips + math.floor(self.pot / 2)
            self.player2.chips = self.player2.chips + math.floor(self.pot / 2)
            print(f"EMPATE!\nMão: {e.hand}")

    def flop(self) -> Player | None:
        # FLOP
        for card in self.deck.cards_list[4:7]:
            self.player1.add(card)
            self.player2.add(card)

        # to debug, getting players at all stages
        print("-" * 8 + " FLOP " + "-" * 8)
        self.get_players()
        return self.do_bets()

    def turn(self) -> Player | None:
        # TURN
        self.player1.add(self.deck[7])
        self.player2.add(self.deck[7])

        # to debug, getting players at all stages
        print("-" * 8 + " TURN " + "-" * 8)
        self.get_players()
        return self.do_bets()

    def river(self) -> Player | None:
        # RIVER
        self.player1.add(self.deck[8])
        self.player2.add(self.deck[8])

        # to debug, getting players at all stages
        print("-" * 8 + " RIVER " + "-" * 8)
        self.player1.sort()
        self.player2.sort()
        self.get_players()
        return self.do_bets()

    def finish_game(self, showdown: bool = True, winner: Player = None):
        if showdown:
            self.player1.hand = get_best_hand(self.player1.hand)
            self.player2.hand = get_best_hand(self.player2.hand)

            self.get_winner()
        else:
            winner.chips += self.pot
            print(f'Ganhador: {winner.hand} | tamanho do pot: {self.pot}')

        # RESTART
        print('/*\\' * 5 + ' FIM ' + '/*\\' * 5)
        if self.player1.is_all_in() or self.player2.is_all_in():
            print('Jogo Terminou, um jogador perdeu!')
            exit()
        # change player that starts the game
        self.starter_player *= -1
        # increase the blind
        self.blind_increase_rate += 1
        if self.blind_increase_rate % self.BLIND_INCREASE_RATE_REFERENCE == 0:
            self.blind += self.blind * self.blind_increase_size
            self.blind_increase_rate = 0
        self.round_over = False
        input('>')


from Exceptions.Exceptions import TiedHandsException
from Functions.CompareHands import compare_hands
