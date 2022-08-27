import random

from Model import Board, Card, DiscardPile, Hand


class GameState:

    def __init__(self):
        self.board = Board()
        self.players = []

    def init(self, seed=0):
        num_players = len(self.players)
        if num_players < 1 or num_players > 5:
            raise ValueError(f"invalid number of players! is {num_players}, should be 1..5.")
        self.handLimit = 6
        if num_players == 2:
            self.handLimit += 1
        if num_players == 1:
            self.handLimit += 2
        self.current_player = 0

        random.seed(seed)

        # reset board and shuffle the draw pile
        self.board = Board()
        self.board.draw_pile.shuffle()

        # reset players
        for player in self.players:
            # empty hand
            player.hand = Hand()
            self.drawHand(player)

        self.current_player = 0

    def drawHand(self, player):
        drawn = 0
        while len(player.hand) < self.handLimit:
            card = self.board.draw_pile.pop()
            player.hand.append(card)
            drawn += 1
        return drawn

    def execute_move(self, move):
        # remove card from hand
        move.player.hand.remove(move.card)
        # discard card to stack
        move.pile.push(move.card)

    # return True if move is valid
    def test_move(self, move):
        pile: DiscardPile = move.pile
        card: Card = move.card
        if pile.isAscending():
            return card.value > pile.top().value
        else:  # descending pile
            return card.value < pile.top().value

    def findValidMoves(self, player):
        validMoves = []
        for pile in self.board.stacks:
            for card in player.hand.list:
                move = Move(player, card, pile)

                if self.test_move(move):
                    validMoves.append(move)
        return validMoves

    def print_board(self):
        # print the top card of every stack in the same line separated by a space
        print("Board :", " | ".join([str(stack.top()) for stack in self.board.stacks]))


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __repr__(self):
        return f"{self.name}"

    def isAI(self):
        return False;


class Move:
    def __init__(self, player, cardOrValue, stack: DiscardPile):
        self.player = player
        self.pile = stack
        if type(cardOrValue) == Card:
            self.card = cardOrValue
        else:
            self.card = Card(cardOrValue)

    def delta(self):
        return abs(self.card.value - self.pile.top().value)

    def __repr__(self):
        return f"Player {self.player} discards {self.card} to pile {self.pile}"
