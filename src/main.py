import random


class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 100):
            self.cards.append(Card(i))

    def rm_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.card = []
        self.name = name

    def draw(self, deck):
        self.card.append(deck.rm_card())
        return self

    def show_hand(self):
        for card in self.card:
            print(card)
        return self


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.player_count = 4
        # TODO: create player objects and add them to the player list


# Testing:
game = Game()

try:
    game.players[0].show_hand()
    # print length of deck
    print("Cards Left: ", len(game.deck))
except:
    print("No players")
