import random
import pytest

from Game import GameState, Player, Move


def test_empty_game_state():
    # TODO pass num players
    game = GameState()

    assert len(game.players) == 4
    assert len(game.board.draw_pile) == 98
    # TODO turn count == 1
    # TODO current Player index == 0


def test_game_init():
    game = GameState()
    game.init()

    for p in game.players:
        assert len(p.hand) == 6


def test_drawHand():
    game = GameState()
    player = game.players[0]
    actual = game.drawHand(player)
    assert actual == 6
    assert len(player.hand) == 6


def test_seed_0_cards():
    game = GameState()
    game.init(0)

    p1 = game.players[0]
    p2 = game.players[1]

    assert str(p1.hand) == "[51, 55, 7, 35, 67, 64]"


def test_seed_4711_cards():
    game = GameState()
    game.init(4711)

    p1 = game.players[0]
    p2 = game.players[1]

    assert str(p1.hand) == "[19, 64, 90, 72, 5, 47]"


def test_turn():
    game = GameState()
    game.init(0)

    # p1 Hand [51, 55, 7, 35, 67, 64]
    p1 = game.players[0]
    # initial board
    s1 = game.board.stacks[0]
    s4 = game.board.stacks[3]

    # 1st move 7 to s1
    # 2st move 67 to s4
    # draw 2

    game.execute_move(Move(p1, 7, s1))
    assert len(p1.hand) == 5
    assert str(p1.hand) == "[51, 55, 35, 67, 64]"
    assert len(s1) == 2
    assert str(s1.top()) == "7"




