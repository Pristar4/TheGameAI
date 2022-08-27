import random
import pytest

import Model
from Model import Card, CardPile, DiscardPile, Board


# Card tests
def test_invalid_cards():
    with pytest.raises(ValueError):
        card = Card(0)
    with pytest.raises(ValueError):
        card = Card(101)


def test_special_cards():
    assert not Card(1).isValid()
    assert not Card(100).isValid()


def test_all_valid_cards():
    for v in range(2, 99):
        card = Card(v)
        assert card.value == v
        assert card.isValid()


def test_str_repr():
    card = Card(14)
    assert str(card) == "14"


# CardPile tests
def test_draw_pile_construction():
    deck = CardPile()
    assert len(deck.stack) == 98


def test_discard_pile():
    discard = DiscardPile(0)
    assert discard.constraint == Model.STACK_TYPE_UP
    assert discard.isUp()
    discard = DiscardPile(1)
    assert discard.constraint == 1


def test_board_construction():
    board = Board()
    assert len(board.stacks) == 4
    assert board.stacks[0].constraint == Model.STACK_TYPE_UP
    assert board.stacks[1].constraint == Model.STACK_TYPE_UP
    assert board.stacks[2].constraint == 1
    assert board.stacks[3].constraint == 1
