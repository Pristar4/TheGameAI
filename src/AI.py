from Game import GameState, Move
from Model import Player

THRESHOLD = 1


class AI(Player):

    @staticmethod
    def isAI():
        return True

    # find valid moves for complete turn
    def findMoves(self, game: GameState):
        moves = []
        # find 2 moves
        while True:  # len(moves) < 2:

            best = game.findValidMoves(self)
            best.sort(key=lambda m: m.delta(), reverse=False)
            if not best:  # empty
                return moves
            move = best[0]

            # find special combo
            delta = move.delta()
            special = self.findSpecialCombo(game, delta)
            if special:
                game.listener.logAI("* special combo found!")
                for move in special.moves:
                    game.execute_move(move)
                    moves.append(move)
            else:
                if delta > THRESHOLD and len(moves) >= 2:
                    break
                game.execute_move(move)
                moves.append(move)
        # while

        game.drawHand(self)
        return moves

    def findSpecialCombo(self, game: GameState, best=2):
        for pile in game.board.stacks:
            pms = []
            for card in self.hand.list:
                pms.append(Move(self, card, pile))

            combos = combine3(pms)
            for combo in combos:
                if combo.delta < best:
                    return combo
            combos = combine2(pms)
            for combo in combos:
                if combo.delta < best:
                    return combo

            # for stacks
        return None


class Combo:
    def __init__(self, move):
        self.moves = [move]
        self.delta = move.delta()

    def add(self, move):
        self.moves.append(move)
        self.delta += move.delta()

    def __repr__(self):
        return f"Combo {len(self.moves)} move to delta {self.delta}"


def combine1(moves):
    # assert(all moves on same stack)
    result = []
    for m in moves:
        if m.valid():
            result.append(Combo(m))
    return result


def combine2(l1moves):
    # assert(all moves on same stack)
    result = []
    for l1 in l1moves:
        if l1.valid():
            l2moves = reduce(l1moves, l1)
            for l2 in l2moves:
                if l2.special():
                    combo = Combo(l1)
                    combo.add(l2)
                    result.append(combo)

    return result


def reduce(moves, move):
    result = []
    stack = move.pile.copy()
    stack.push(move.card)
    for m in moves:
        if m != move:
            result.append(Move(move.player, m.card, stack))
    return result


def combine3(l1moves):
    # assert(all moves on same stack)
    result = []
    for l1 in l1moves:
        if l1.valid():
            l2moves = reduce(l1moves, l1)
            for l2 in l2moves:
                if l2.valid():
                    l3moves = reduce(l2moves, l2)
                    for l3 in l3moves:
                        if l3.special():
                            combo = Combo(l1)
                            combo.add(l2)
                            combo.add(l3)
                            result.append(combo)
    return result
