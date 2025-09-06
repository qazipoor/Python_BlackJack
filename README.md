# 🃏 Blackjack Game (Python)

A simple command-line Blackjack game built with Python.  
This project is a fun way to practice Python basics such as loops, conditionals and game logic.

---

## 🎮 Features
- Play against the dealer with standard Blackjack rules.
- Supports card shuffling and dealing.
- Keeps track of player and dealer hands.
- Determines winner based on Blackjack rules.
- Simple, text-based interface (no external libraries required).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher installed on your system.

### Installation
1. Clone the repository:
   - git clone https://github.com/qazipoor/Python_BlackJack.git 
2. Navigate into the project folder:
    - cd Python_Blackjack
3. Run the game:
    - python main.py

## 📖 How to Play

1. Start the game and you’ll be dealt two cards.
2. The dealer also receives two cards (one hidden). 
3. You can choose:

   - **y**: Draw another card.
   - **n**: Keep your current hand and let the dealer play. 

4. The goal is to get as close to **21** as possible without going over. 
5. The dealer will reveal their hand and play by the rules:
    - Must hit until reaching 17 or higher. 
6. Whoever has the higher total without busting wins.

## 🖥️ **Demo**

Example game flow in the terminal:

Your cards: **['10', '7']**  current score: **17** \
Dealer first card: **['10']**

Type **y** to get another card, type '**n**' to pass: **n**

Your final hand: **['10', '7']**, final score: **17** \
Dealer's final hand: **['10', '10']**, final score: **20** \
You lose 😭 \
Dealer wins!

## 🛠️ Built With

* **Python** – Core language for game logic.

## 📌 Future Improvements
* Add betting system with chips.
* Add multiple players.
* Add GUI version using Tkinter or PyQt.
* Track win/loss history.

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

