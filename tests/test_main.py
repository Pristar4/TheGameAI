import random

from Game import GameState, Player
from Model import Card, CardPile, DiscardPile, Board


def test_card_construction():
    card = Card(4)
    assert card.value == 4


def test_draw_pile_construction():
    deck = CardPile()
    assert len(deck.stack) == 98


def test_discard_pile():
    discard = DiscardPile(0)
    assert discard.constraint == 0
    discard = DiscardPile(1)
    assert discard.constraint == 1


def test_board_construction():
    board = Board()
    assert len(board.stacks) == 4
    assert board.stacks[0].constraint == 0
    assert board.stacks[1].constraint == 0
    assert board.stacks[2].constraint == 1
    assert board.stacks[3].constraint == 1

