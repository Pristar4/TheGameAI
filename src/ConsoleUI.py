from Game import GameListener


class ConsoleUI(GameListener):

    @staticmethod
    def startRound(game) -> None:
        print(f"== Round {game.round} =====================")

    @staticmethod
    def startTurn(game, player):
        print(f"It is {player}'s turn.")

    @staticmethod
    def startMove(game, player):
        game.print_board()
        print(f"Hand : {player.hand}")

    @staticmethod
    def doMove(move):
        print(f"{move}")

    @staticmethod
    def game_over(game) -> None:
        print("====================================")
        game.print_board()
        for player in game.players:
            moves = len(game.findValidMoves(player))
            print(f"{player}'s Hand : {player.hand} ({moves} moves left)")
        print(game.board.draw_pile)
        print("Cards Left:", game.remainingCards(),
              f"after {game.round} rounds.")

    @staticmethod
    def logAI(text):
        print(text)
