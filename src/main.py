
import Game

# constants for stack types


def main():
    # create a new game
    game = Game.GameState()
    game.init()

    # print the board
    game.print_board()

    # Game loop
    while True:
        # get the current player
        player = game.players[game.current_player]
        # get the player's move
        # print the hand of the player
        print(player, player.hand)
        move = (int(input(f"{player.name} choose Hand Card: ")), int(
            input("Choose Stack: ")))

        # execute the move
        game.execute_move(move, player)

        # print the board
        game.print_board()
        # switch to the next player
        game.current_player = (game.current_player + 1) % len(game.players)


if __name__ == "__main__":
    main()
