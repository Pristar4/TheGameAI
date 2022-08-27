
from Game import GameState, Move
from Model import Card, Hand


# constants for stack types


def main():
    # create a new game
    game = GameState()
    game.init()

    # Game loop
    while True:
        player = game.players[game.current_player]

        # do players turn
        doTurn(game, player)

        # switch to the next player
        game.current_player = (game.current_player + 1) % len(game.players)
        # if game.current_player == 0:
        #   self.turn += 1


def doTurn(game, player):
    print("-------------------------")
    print(f"It is {player}'s turn.")
    moves = 0
    while len(player.hand) > 0:
        moves += 1
        print(f"-- move {moves} --")
        game.print_board()
        move = inputMove(game, player)
        game.execute_move(move)
        if moves >= 2:
            _ = input("[c]ontinue or [f]inish turn : ")
            if _ == 'f':
                break
    game.drawHand(player)

def inputMove(game, player):
    hand: Hand = player.hand

    # print the hand of the player
    print(f"Hand : {hand}")
    # input Card
    card = Card(int(input(f"{player.name} choose card value: ")))
    # validate
    if not hand.contains(card):
        raise ValueError(f"Hand does not contain the Card {card}!")

    stacknum = int(input("Choose Stack (1..4): "))
    stack = game.board.stacks[stacknum-1]
    move = Move(player, card, stack)
    return move


if __name__ == "__main__":
    main()
