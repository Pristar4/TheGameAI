import random

# discard stack types
STACK_TYPE_ASCENDING = 0
STACK_TYPE_DESCENDING = 1

# discard stack indices
STACK_IDX_LEFT_ASC = 0
STACK_IDX_RIGHT_ASC = 1
STACK_IDX_LEFT_DESC = 2
STACK_IDX_RIGHT_DESC = 3


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

    # __copy__??
    def copy(self):
        cpy = DiscardPile(self.constraint)
        cpy.stack = self.stack.copy()
        return cpy

    def top(self):
        return self.stack[-1]

    def isAscending(self):
        return self.constraint == STACK_TYPE_ASCENDING

    def isDescending(self):
        return self.constraint == STACK_TYPE_DESCENDING

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        con = "ASC "
        if self.isDescending():
            con = "DESC"
        top = self.top()

        return f"{con} [{top}]"

# the board has 4 discards stacks in following order
# left ascending, right ascending, left descending, right descending
class Board:

    def __init__(self):
        self.draw_pile = CardPile()
        self.stacks = []
        # create two stacks for each stack type
        self.init_board()

    def init_board(self):
        for i in range(2):
            self.stacks.append(DiscardPile(STACK_TYPE_ASCENDING))
        for i in range(2):
            self.stacks.append(DiscardPile(STACK_TYPE_DESCENDING))
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

    def contains(self, card):
        return card in self.list

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return f"{self.list}"


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __repr__(self):
        return f"{self.name}"

    def isAI(self):
        return False
