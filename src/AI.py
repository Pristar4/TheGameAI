from Model import Board, Card, DiscardPile, Hand
from Game import Player, GameState, Move


class AI(Player):

    def __init__(self, name):
        super().__init__(name)

    def isAI(self):
        return True;

    # find valid moves for complete turn
    def findMoves(self, game: GameState):
        moves = []
        # find 2 moves
        while len(moves) < 2:
            validMoves = game.findValidMoves(self)
            validMoves.sort(key=lambda m: m.delta(), reverse=True)
            if not validMoves:  # empty
                return moves

            move = validMoves.pop()
            print(f"AI moves {move}")
            game.execute_move(move)
            moves.append(move)
            game.drawHand(self)

        return moves
