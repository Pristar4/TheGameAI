from Model import Board


class GameState:
    def __init__(self):
        self.board = Board()
        self.players = []
        # add 4 players
        for _ in range(1, 5):
            self.players.append(Player(f"Player {_}"))
        self.current_player = 0
        # shuffle the draw pile
        self.board.draw_pile.shuffle()

    def execute_move(self, move, player):
        self.board.stacks[move[1]-1].push(player.hand.pop(move[0]))


    def print_board(self):
        #print the top card of every stack in the same line separated by a space
        print(" | ".join([str(stack.top()) for stack in self.board.stacks]))
        pass


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return f"{self.name}"
