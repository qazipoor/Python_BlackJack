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

# Comparing the score of players to check who is the winner or if it's a draw or Blackjack and prints the result
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw! 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😭"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😁"
    else:
        return "You lose 😭"

# Initialize and start the game
def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Giving the players first two cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Asking the user if s/he wants to get a new card or else end the game
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards {user_cards}, current score {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Giving the computer a new card if the computer's score is not over 17 or Blackjack
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Prints the final scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
