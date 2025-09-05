import random
from art import logo

# deal_card() function that returns a random card each time it is called
def deal_card():
    # Cards deck that contains ace = 1 | 11, 2 to 10 and additional 3 10's for face cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# calculate_score function to calculate and return the total cards or returns zero in case of Blackjack
def calculate_score(cards):
    # Return zero in case of Blackjack and ends the game
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Replaces the 11 with 1 if the score is over the 21
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    score = sum(cards)
    return score
