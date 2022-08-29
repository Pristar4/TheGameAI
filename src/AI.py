from Game import GameState, Move
from Model import Player

THRESHOLD = 1


class AI(Player):

    @staticmethod
    def isAI():
        return True

    # find valid moves for complete turn
    def findMoves(self, game: GameState):
        """Finds all valid moves for the AI player.
        :param game: The game state to find moves for.
        :type game:  GameState
        :return:   A list of valid moves.
        :rtype:   list[Move]
        """
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
        """Find the best combo available for the current game state.
        :param game: The game state to find the combo for.
        :type game: GameState
        :param best: The number of best moves to return.
        :type best: int
        :return: The best combo available for the current game state.
        :rtype: Combo
        """
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
    """Find all valid combos for the given moves.
    :param moves: The moves to find combos for.
    :type moves: list[Move]
    :return: The valid combos for the given moves.
    :rtype: list[Combo]
    """
    # assert(all moves on same stack)
    result = []
    for m in moves:
        if m.valid():
            result.append(Combo(m))
    return result


def combine2(l1moves):
    """Find the best combo  for two moves.
    :param l1moves:
    :type l1moves:
    :return:
    :rtype:
    """
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
    """Find the best combo  for three moves.
    :param l1moves: The given valid moves.
    :type l1moves: list[Move]
    :return: valid 3 move combos.
    :rtype: list[Combo]
    """
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
