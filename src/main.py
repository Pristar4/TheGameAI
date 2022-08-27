import sys

from AI import AI
from ConsoleUI import ConsoleUI
from Game import GameState, Move, GameListener
from Model import Card, Hand, Player


def main():

    games = []
    best = 100
    for i in range(2, 2+1):
        game = createGame(i, 2)
        runGame(game)
        games.append(game)
        best = min(best, game.remainingCards())

    print(f"run {len(games)} games, best result: {best}")


def createGame(seed=0, numKI=1, numHuman=0):
    # create a new game
    game = GameState()
    game.setListener(ConsoleUI())

    for _ in range(numKI):
        game.players.append(AI(f"AI{_+1}"))
    for _ in range(numHuman):
        game.players.append(Player(f"Human{_+1}"))

    game.init(seed)
    return game


def runGame(game):
    while not game.gameover:

        if game.current_player == 0:
            game.round += 1
            game.listener.startRound(game)

        player = game.players[game.current_player]

        # do players turn
        game.gameover = doTurn(game, player)

        # switch to the next player
        game.current_player = (game.current_player + 1) % len(game.players)

    game.listener.gameover(game)


def doTurn(game, player):

    game.listener.startTurn(game, player)
    # FIXME polymorph...
    if player.isAI():
        game.listener.startMove(game, player)
        ai: AI = player
        moves = ai.findMoves(game)
        if len(moves) < 2:
            return True
    else:
        # TODO move to ConsoleUI (only human)
        moves = 0
        while len(player.hand) > 0:

            if (len(game.findValidMoves(player)) == 0):
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
