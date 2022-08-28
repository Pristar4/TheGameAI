# Handle the GUI of each Class


# Print Board:
#
# def print_board(self, board):

class GameUi:
    def __init__(self, game_state):
        self.game_state = game_state

    def getMove(self, player, board):
        raise NotImplementedError()

    @staticmethod  # staticmethod is a decorator
    def takeTurn(game_state, player):
        # get possible move from Input from human
        i = input("Enter your move: ")
        # execute move
        game_state.execute_move(i, player)

    def test_Move(self):
        raise NotImplementedError()
