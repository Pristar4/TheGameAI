import random

from Model import Board, Card, DiscardPile, Hand


class GameListener:

    def __init__(self):
        ...

    def start_round(self, game) -> None:
        ...

    def start_turn(self, game, player) -> None:
        ...

    def start_move(self, game, player) -> None:
        ...

    def do_move(self, move):
        ...

    def game_over(self, game) -> None:
        raise NotImplementedError()

    def log_ai(self, text):
        raise NotImplementedError()




class GameState:

    def __init__(self):
        self.current_player = None
        self.hand_limit = None
        self.board = Board()
        self.players = []
        self.game_over = False
        self.round = 0
        self.listener = GameListener()

    def set_listener(self, listener):
        self.listener = listener

    def init(self, seed=0):
        num_players = len(self.players)
        if num_players < 1 or num_players > 5:
            raise ValueError(f"invalid number of players! is {num_players}, "
                             f"should be 1..5.")
        self.hand_limit = 6
        if num_players == 2:
            self.hand_limit += 1
        if num_players == 1:
            self.hand_limit += 2
        self.current_player = 0

        random.seed(seed)

        # reset board and shuffle the draw pile
        self.board = Board()
        self.board.draw_pile.shuffle()

        # reset players
        for player in self.players:
            # empty hand
            player.hand = Hand()
            self.draw_hand(player)

        self.current_player = 0

    def draw_hand(self, player):
        drawn = 0
        while len(player.hand) < self.hand_limit and self.board.draw_pile:
            card = self.board.draw_pile.pop()
            player.hand.append(card)
            drawn += 1
        return drawn

    def execute_move(self, move):
        self.listener.do_move(move)
        # remove card from hand
        move.player.hand.remove(move.card)
        # discard card to stack
        move.pile.push(move.card)

    # return True if move is valid

    def find_valid_moves(self, player):
        valid_moves = []
        for pile in self.board.stacks:
            for card in player.hand.list:
                move = Move(player, card, pile)

                if self.test_move(move):
                    valid_moves.append(move)
        return valid_moves

    def print_board(self):
        # print the top card of every stack in the same line separated by a
        # space
        print("Board :",
              " | ".join([str(stack.top()) for stack in self.board.stacks]))

    def remaining_cards(self):
        total = 0
        for player in self.players:
            total += len(player.hand)
        total += len(self.board.draw_pile)
        return total

    @staticmethod
    def test_move(move):
        delta = move.delta()
        return delta == -10 or delta > 0


class Move:

    def __init__(self, player, card_or_value, stack: DiscardPile):
        self.player = player
        self.pile = stack
        if type(card_or_value) is Card:
            self.card = card_or_value
        else:
            self.card = Card(card_or_value)

        self._delta = self.calculate_delta()

    def calculate_delta(self):
        pile = self.pile
        card = self.card
        value = pile.top().value
        if pile.isAscending():
            return card.value - value
        return value - card.value

    def delta(self):
        """The delta of a move gives the difference between the value of the
        card and the value of the top card of the pile.

        :return: The delta of the move.
        :rtype: int
        """
        return self._delta

    def valid(self):
        return self.special() or self._delta > 0

    def special(self):
        """Special moves have a -10 delta value.

        :return: True if the move is special, False otherwise.
        :rtype: bool
        """
        return self._delta == -10

    def __repr__(self):
        return (f"Player {self.player} discards {self.card} "
                f"to pile {self.pile} ({self.delta()}) ")
