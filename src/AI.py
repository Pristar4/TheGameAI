from Model import Board, Card, DiscardPile, Hand
from Game import Player, GameState, Move


class AI(Player):

    def __init__(self, name):
        super().__init__(name)

    def isAI(self):
        return True;

    # find valid moves for complete turn
    def findMoves(self, game: GameState):
        # find 2 moves
        move1 = self.findBestValidMove(game)
        print(f"AI moves {move1}")
        game.execute_move(move1)
        move2 = self.findBestValidMove(game)
        print(f"AI moves {move2}")
        game.execute_move(move2)
        game.drawHand(self)
        return [move1, move2]

    def findBestValidMove(self, game: GameState):

        # TODO extract to static util method
        validMoves = game.findValidMoves(self)

        # sort validMoves by delta function
        validMoves.sort(key=lambda m: m.delta(), reverse=True)
        best = validMoves.pop()
        return best


