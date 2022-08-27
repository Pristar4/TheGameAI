import random

STACK_TYPE_UP = 0
STACK_TYPE_DOWN = 1


class Card:
    def __init__(self, value):
        self.value = value
        if value not in range(1, 101):
            raise ValueError('valid value 1..100')

    def isValid(self):
        return self.value in range(2, 100)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False
    def __str__(self):
        return f"{self.value}"
    def __repr__(self):
        return f"{self.value}"


class CardPile:
    def __init__(self):
        self.stack = []
        for i in range(2, 100):
            self.stack.append(Card(i))

    def pop(self):
        return self.stack.pop()

    def shuffle(self):
        random.shuffle(self.stack)

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return f"{self.stack}"


class DiscardPile:
    def __init__(self, stack_type):
        self.stack = []
        self.constraint = stack_type

    def push(self, card):
        self.stack.append(card)

    def top(self):
        return self.stack[-1]

    def isUp(self):
        return self.constraint == STACK_TYPE_UP

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return f"{self.stack}"


class Board:

    def __init__(self):
        self.draw_pile = CardPile()
        self.stacks = []
        # create two stacks for each stack type
        self.init_board()

    def init_board(self):
        for i in range(2):
            self.stacks.append(DiscardPile(STACK_TYPE_UP))
        for i in range(2):
            self.stacks.append(DiscardPile(STACK_TYPE_DOWN))
        # add to every Stack_type_up stack a 0 to the top
        for stack in self.stacks[:2]:
            stack.push(Card(1))
        for stack in self.stacks[2:]:
            stack.push(Card(100))

    def __repr__(self):
        return f"{self.stacks}"


class Hand:
    def __init__(self):
        self.list = []

    def append(self, card):
        self.list.append(card)

    def remove(self, card):
        self.list.remove(card)

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return f"{self.list}"


