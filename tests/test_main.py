from main import Card, Deck


def test_card_construction():
    card = Card(4)
    assert card.value == 4


def test_deck_construction():
    deck = Deck()
    assert len(deck.cards) == 98



