from Game import GameListener


class ConsoleUI(GameListener):

    def startRound(self, game) -> None:
        print(f"== Round {game.round} =====================")

    def startTurn(self, game, player):
        print(f"It is {player}'s turn.")

    def startMove(self, game, player):
        game.print_board()
        print(f"Hand : {player.hand}")

    def doMove(self, move):
        print(f"{move}")

    def game_over(self, game) -> None:
        print("====================================")
        game.print_board()
        for player in game.players:
            moves = len(game.findValidMoves(player))
            print(f"{player}'s Hand : {player.hand} ({moves} moves left)")
        print(game.board.draw_pile)
        print("Cards Left:", game.remainingCards(),
              f"after {game.round} rounds.")

    def logAI(self, text):
        print(text)
