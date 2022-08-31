from Game import GameState, Move
from main import create_game


def test_empty_game_state():
    game = create_game(0, 4)

    game.current_player = 0
    game.round = 0
    assert len(game.players) == 4
    assert len(game.board.draw_pile) == 74


def test_game_init():
    game = create_game(0, 4)

    for p in game.players:
        assert len(p.hand) == 6


def test_draw_hand():
    game = create_game(0, 4)

    player = game.players[0]
    game.draw_hand(player)
    assert len(player.hand) == 6
    assert str(player.hand) == "[51, 55, 7, 35, 67, 64]"


def test_seed_0_cards():
    game = create_game(0, 4)

    p1 = game.players[0]

    assert str(p1.hand) == "[51, 55, 7, 35, 67, 64]"


def test_seed_4711_cards():
    game = create_game(4711, 4)

    p1 = game.players[0]

    assert str(p1.hand) == "[19, 64, 90, 72, 5, 47]"


def test_turn():
    game = create_game(0, 4)

    # p1 Hand [51, 55, 7, 35, 67, 64]
    p1 = game.players[0]
    # initial board
    s1 = game.board.stacks[0]

    # 1st move 7 to s1
    # 2nd move 67 to s4
    # draw 2

    game.execute_move(Move(p1, 7, s1))
    assert len(p1.hand) == 5
    assert str(p1.hand) == "[51, 55, 35, 67, 64]"
    assert len(s1) == 2
    assert str(s1.top()) == "7"
