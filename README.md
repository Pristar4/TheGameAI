You can find the Documentation at: https://pristar4.github.io/TheGameAI/



# TheGame AI



# Introduction

    TheGame AI is going to be a AI that can play "TheGame".
# About TheGame:
    TheGame is a Card Game,
    is played with 4 players.
    TheGame is played with a deck of 52 cards.
## TheGame Rules:
- TheGame is played with a deck of cards going from 2 to 99.
- Each player has a hand of 6 cards.
- There are 4 Stacks of cards: 2 going `up` from 2 to 99, and the other 2 going `down` from 99 to 2.
- Each Turn, a player:
    - Play a card from their hand.
    - The Player has to play a minimum of 2 cards.
    - After the Player doesn't want to play more cards or cant he draws new cards from the deck until he has 6 cards again.
    - The Player can only play cards that are lower than the top card of a `down-stack` or higher than the top card of an `up-stack`.
# Down-stack:

      - Counts down (99 to 2).
# Up-stack:

      - Counts up (2 to 99).

# Result:

  - When the game finished, the score is calculated by:
      - the sum of the remaining cards in the players hands
      -  the sum of the cards in the stacks.
  - The Lower the score the better.

# Features:

## Delete the old documentation
    ```
    when in docs directory:
    ```make clean
    ```

## Generate new Documentation
    when in docs directory:
    ```make html
    this way you generate the html documentation based your latest version
    ```