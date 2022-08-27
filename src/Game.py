import random

from Model import Board, Card, DiscardPile, Hand


class GameListener:
    def __init__(self):
        pass

    def startRound(self, game) -> None:
        pass

    def startTurn(self, game, player) -> None:
        pass

    def startMove(self, game, player) -> None:
        pass

    def doMove(self, move):
        pass

    def gameover(self, game) -> None:
        pass

    def logAI(self, text):
        pass


class GameState:

    def __init__(self):
        self.board = Board()
        self.players = []
        self.gameover = False
        self.round = 0
        self.listener = GameListener()

    def setListener(self, listener):
        self.listener = listener

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
        while len(player.hand) < self.handLimit and self.board.draw_pile:
            card = self.board.draw_pile.pop()
            player.hand.append(card)
            drawn += 1
        return drawn

    def execute_move(self, move):
        self.listener.doMove(move)
        # remove card from hand
        move.player.hand.remove(move.card)
        # discard card to stack
        move.pile.push(move.card)

    # return True if move is valid
    def test_move(self, move):
        delta = move.delta()
        return delta == -10 or delta > 0

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

    def remainingCards(self):
        sum = 0
        for player in self.players:
            sum += len(player.hand)
        sum += len(self.board.draw_pile)
        return sum



class Move:

    def __init__(self, player, cardOrValue, stack: DiscardPile):
        self.player = player
        self.pile = stack
        if type(cardOrValue) == Card:
            self.card = cardOrValue
        else:
            self.card = Card(cardOrValue)

        self._delta = self.calculate_delta()

    def calculate_delta(self):
        pile = self.pile
        card = self.card
        value = pile.top().value
        if pile.isAscending():
            return card.value - value
        else:  # descending
            return value - card.value

    def delta(self):
        return self._delta

    def valid(self):
        return self.special() or self._delta > 0

    def special(self):
        return self._delta == -10

    def __repr__(self):
        return f"Player {self.player} discards {self.card} to pile {self.pile} ({self.delta()})"
