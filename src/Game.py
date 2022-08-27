import random

from Model import Board, Card, DiscardPile, Hand


class GameState:

    def __init__(self):
        self.board = Board()
        self.handLimit = 6
        self.current_player = 0
        self.players = []
        # add 4 players
        for _ in range(1, 5):
            player = Player(f"Player {_}")
            self.players.append(player)

    def init(self, seed=0):
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
        pile:DiscardPile = move.pile
        card:Card = move.card
        if pile.isAscending():
            return card.value > pile.top().value
        else:  # descending pile
            return card.value < pile.top().value

    def print_board(self):
        # print the top card of every stack in the same line separated by a space
        print("Board :",  " | ".join([str(stack.top()) for stack in self.board.stacks]))


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __repr__(self):
        return f"{self.name}"


class Move:
    def __init__(self, player, cardOrValue, stack:DiscardPile):
        self.player = player
        self.pile = stack
        if type(cardOrValue) == Card:
            self.card = cardOrValue
        else:
            self.card = Card(cardOrValue)

    def __repr__(self):
        return f"Player {self.player} discards {self.card} to pile {self.pile}"
