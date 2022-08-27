from AI import AI
from Game import GameState, Move, Player
from Model import Card, Hand


def main():
    # create a new game
    game = GameState()
    # add 2 4 players
    game.players.append(AI("AI"))
    # game.players.append(Player("Human"))
    game.init(4711)

    # Game loop
    while not game.gameover:
        player = game.players[game.current_player]

        # do players turn
        game.gameover = doTurn(game, player)

        # switch to the next player
        game.current_player = (game.current_player + 1) % len(game.players)
        # if game.current_player == 0:
        #   self.turn += 1

    print("====================================")
    game.print_board()
    x = 0
    for player in game.players:
        print(player)
        x += len(player.hand)
    print(game.board.draw_pile)
    print("Cards Left:",len(game.board.draw_pile) + x)

def doTurn(game, player):
    print("-------------------------")
    print(f"It is {player}'s turn.")
    # FIXME polymorph...
    if player.isAI():
        game.print_board()
        print(f"Hand : {player.hand}")
        ai: AI = player
        moves = ai.findMoves(game)
        if len(moves) < 2:
            return True
    else:
        moves = 0
        while len(player.hand) > 0:

            if (len(game.findValidMoves(player)) == 0):
                print("No more moves possible!")
                return True

            moves += 1
            print(f"-- move {moves} --")
            game.print_board()
            move = inputMove(game, player)
            game.execute_move(move)
            if moves >= 2:
                _ = input("[c]ontinue or [f]inish turn : ")
                if _ == 'f':
                    break
        drawn = game.drawHand(player)
        game.print_board()
        print(f"Draw {drawn} new Cards to Hand : {player.hand}")
        return False

def inputMove(game, player):
    hand: Hand = player.hand

    while True:
        # print the hand of the player
        print(f"Hand : {hand}")
        # input Card
        # TODO loop until valid input
        card = Card(int(input(f"{player.name} choose card value: ")))
        # validate
        if not hand.contains(card):
            raise ValueError(f"Hand does not contain the Card {card}!")
            # TODO handle Error in logic

        # TODO loop until valid input
        stacknr = int(input("Choose Stack (1..4): "))
        # TODO handle invalid input: stacknum not in range(1,5)
        stack = game.board.stacks[stacknr - 1]
        move = Move(player, card, stack)
        # check is move is valid
        if game.test_move(move):
            return move
        else:
            print(f"invalid Move {move}")


if __name__ == "__main__":
    main()
