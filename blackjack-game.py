#                     blackjack-game.py written by
#  _______  _______  ___  __    _  ___   _  ___  _______  _______  _______
# |       ||       ||   ||  |  | ||   | | ||   ||       ||       ||       |
# |  _____||_     _||   ||   |_| ||   |_| ||   ||    _  ||    ___||____   |
# | |_____   |   |  |   ||       ||      _||   ||   |_| ||   |___  ____|  |
# |_____  |  |   |  |   ||  _    ||     |_ |   ||    ___||    ___|| ______|
#  _____| |  |   |  |   || | |   ||    _  ||   ||   |    |   |___ | |_____
# |_______|  |___|  |___||_|  |__||___| |_||___||___|    |_______||_______|

import random, os

def clear():
    os.system("clear")

# will be copied to "deck" variable each time a new hand is dealt
new_deck = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
user = 0

title = ('''
# # # # # # # # # # ~ blackjack-game.py written by ~  # # # # # # # # # # # #
#  _______  _______  ___  __    _  ___   _  ___  _______  _______  _______  #
# |       ||       ||   ||  |  | ||   | | ||   ||       ||       ||       | #
# |  _____||_     _||   ||   |_| ||   |_| ||   ||    _  ||    ___||____   | #
# | |_____   |   |  |   ||       ||      _||   ||   |_| ||   |___  ____|  | #
# |_____  |  |   |  |   ||  _    ||     |_ |   ||    ___||    ___|| ______| #
#  _____| |  |   |  |   || | |   ||    _  ||   ||   |    |   |___ | |_____  #
# |_______|  |___|  |___||_|  |__||___| |_||___||___|    |_______||_______| #
#                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
''')
welcome_message = ('''
     _____
    |A .  | _____                      Welcome! This is my first game
    | /.\ ||A ^  | _____               programmed using Python 3.
    |(_._)|| / \ ||A _  | _____
    |  |  || \ / || ( ) ||A_ _ |       Enjoy :)
    |____V||  .  ||(_'_)||( v )|                       -StinkiPez
           |____V||  |  || \ / |
                  |____V||  .  |
                         |____V|
''')

def refresh():
    clear()
    print(title)
    if user == 0:
        print(welcome_message)
        resp = input("Would you like to start a new game? (Y/N) ")

    else:
        print("Player exists")

class Player:

    # initialize and parse attributes
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.hand = []
        self.wins = 0
        self.losses = 0

    # calculates score in your current hand
    def score_hand(self):
        score = 0
        for card in self.hand:
            if card == 1:
                if (score + 11) > 21:
                    score += 1
                else:
                    score += 11
            else:
                score += self.hand
        return score

    # refresh screen for clearer dispay
    def refresh(self, player):
        clear()
        print('''
# # # # # # # # # # ~ blackjack-game.py written by ~  # # # # # # # # # # # #
#  _______  _______  ___  __    _  ___   _  ___  _______  _______  _______  #
# |       ||       ||   ||  |  | ||   | | ||   ||       ||       ||       | #
# |  _____||_     _||   ||   |_| ||   |_| ||   ||    _  ||    ___||____   | #
# | |_____   |   |  |   ||       ||      _||   ||   |_| ||   |___  ____|  | #
# |_____  |  |   |  |   ||  _    ||     |_ |   ||    ___||    ___|| ______| #
#  _____| |  |   |  |   || | |   ||    _  ||   ||   |    |   |___ | |_____  #
# |_______|  |___|  |___||_|  |__||___| |_||___||___|    |_______||_______| #
#                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        ''')
        print("Wins: " + player.wins + " // Losses: " + self.losses)

# Deal card
def deal(target):
    card = random.randint(1,13)
    while deck[card] == 0:
        card = random.randint(1,13)
    target.hand.append(card)
    deck[card] = deck[card] - 1

# Start New Game
def init_game():
    deck = new_deck

refresh()
