from Game import GameListener


class ConsoleUI(GameListener):

    @staticmethod
    def start_round(game) -> None:
        print(f"== Round {game.round} =====================")

    @staticmethod
    def start_turn(game, player):
        print(f"It is {player}'s turn.")

    @staticmethod
    def start_move(game, player):
        game.print_board()
        print(f"Hand : {player.hand}")

    @staticmethod
    def do_move(move):
        print(f"{move}")

    @staticmethod
    def game_over(game) -> None:
        print("====================================")
        game.print_board()
        for player in game.players:
            moves = len(game.find_valid_moves(player))
            print(f"{player}'s Hand : {player.hand} ({moves} moves left)")
        print(game.board.draw_pile)
        print("Cards Left:", game.remaining_cards(),
              f"after {game.round} rounds.")

    @staticmethod
    def log_ai(text):
        print(text)
