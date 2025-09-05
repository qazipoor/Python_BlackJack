import random
from art import logo

# deal_card() function that returns a random card each time it is called
def deal_card():
    # Cards deck that contains ace = 1 | 11, 2 to 10 and additional 3 10's for face cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

