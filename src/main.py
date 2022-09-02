from AI import AI
from ConsoleUI import ConsoleUI
from Game import GameState, Move
from Model import Card, Hand, Player


def main():
    """
    Main function

    :rtype: None
    """
    games = []
    best = 100
    for i in range(2, 2 + 1):
        game = create_game(i, 2)
        run_game(game)
        games.append(game)
        best = min(best, game.remaining_cards())

    print(f"run {len(games)} games, best result: {best}")


def create_game(seed=0, num_ai=1, num_human=0):
    """Create a new Game This function creates a new Game with the given
    number of AI and Human players.

    :param seed: seed for the random generator
    :type seed: int
    :param num_ai: number of AI players
    :type num_ai: int
    :param num_human: number of human players
    :type num_human: int
    :return: game
    :rtype: GameState
    """
    # create a new game
    game = GameState()
    game.set_listener(ConsoleUI())

    for _ in range(num_ai):
        game.players.append(AI(f"AI{_ + 1}"))
    for _ in range(num_human):
        game.players.append(Player(f"Human{_ + 1}"))

    game.init(seed)
    return game


def run_game(game):
    """Run the game

    :param game: game to run
    :type game: GameState
    """
    while not game.game_over:

        if game.current_player == 0:
            game.round += 1
            game.listener.start_round(game)

        player = game.players[game.current_player]

        # do players turn
        game.game_over = do_turn(game, player)

        # switch to the next player
        game.current_player = (game.current_player + 1) % len(game.players)

    game.listener.game_over(game)


def do_turn(game, player):
    """Do a turn for the player in the game

    :param game: game to do the turn in
    :type game: GameState
    :param player: player to do the turn for
    :type player: Player
    :return: True if the game is over, False otherwise
    :rtype: bool
    """
    game.listener.start_turn(game, player)
    # FIXME polymorph...
    if player.is_ai():
        game.listener.start_move(game, player)
        ai: AI = player
        moves = ai.findMoves(game)
        if len(moves) < 2:
            return True
    else:
        # TODO move to ConsoleUI (only human)
        moves = 0
        while len(player.hand) > 0:

            if len(game.find_valid_moves(player)) == 0:
                return True

            moves += 1
            print(f"-- move {moves} --")
            game.print_board()
            move = input_move(game, player)
            game.execute_move(move)
            # Check if the player made two or more moves then ask if he wants to continue

            if moves > 1 and input("Continue? (y/n)") == "n":
                return True
            # if moves >= 2:
            #
            #     _ = input("Continue or Finish turn : ")
            #     if _ == "f":
            #         break

        drawn = game.draw_hand(player)
        game.print_board()
        print(f"Draw {drawn} new Cards to Hand : {player.hand}")
        return False


def input_move(game, player):
    """Manager the human input for a move

    :param game: game to do the turn in
    :type game: GameState
    :param player: player to do the turn for
    :type player: Player
    :return: move
    :rtype: Move
    """
    hand: Hand = player.hand

    while True:
        # print the hand of the player
        print(f"Hand : {hand}")
        # input Card
        # TODO loop until valid input33

        card = Card(int(input(f"{player.name} choose card value: ")))
        # check if the card is in the hand
        if card not in hand:
            import logging

            logging.error(f"Hand does not contain the Card {card}!")
            continue

        stack_nr = int(input("Choose Stack (1..4): "))
        if stack_nr < 1 or stack_nr > 4:
            import logging

            logging.error(f"Invalid Stack Number {stack_nr}!")
            continue
        stack_nr = game.board.stacks[stack_nr - 1]
        move = Move(player, card, stack_nr)
        # check is move is valid
        if game.test_move(move):
            return move
        print(f"invalid Move {move}")


if __name__ == "__main__":
    main()
