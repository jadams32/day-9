# Welcome to day 9 of 100 days of code. On this day I build a silent auction
# program designed to take bids from users and display the largest bid. Users
# will be bidding on random items selected by the program.
from logo_art import logo
from os import system, name
import random

# Logo and welcom statement
print(logo)
print("Welcome to the slient auction! Enter your bid then pass the program"
        " to the next bidder if any!\n")

# List of items to bid on.
bid_item =["lip gloss", "pc monitor", "chocolate bar", "sand paper", "couch", \
"surge protector", "old lamp shade", "useless remote", "fake flowers", \
"60” TV", "ham radio", "balloon", "leg warmers", "video games", "money", \
"drill press", "Iphone 13", "xbox controller", "keys", "twezzers", \
"scotch tape", "keyboard", "candy wrapper", "bottle cap", "moldy food", \
"collarless shirt", "tooth picks", "phone charger", "helmet", "broken glass", \
"mp3 player", "piano", "sidewalk chalk", "infinity mirror", "pool stick", \
"electromagnet", "chevy truck", "cinder block", "headphones", "toothbrush"]

# Choosing a random item from the list.
print(f"Today we are bidding on a(n) {random.choice(bid_item)}\n")

# Fuction to clear the screen after each person enters their bid amount
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Itializing program state
more_players = True

# Creating empty dictionary to store the users.
auction_list = {}

# Game Logic
while more_players:
    user_name = input("What is your name?\n").title()
    user_bid = int(input("What is your highest bid?\n"))

 # Adding new user to dictionary
    auction_list[user_name] = user_bid

# Asking for input for additonal players
    additional_bidders = input('Are there any more bidders? "Yes" or "No"\n').lower()

# Addtional player logic
    if additional_bidders == "yes":
        clear()
    else:
        clear()
        more_players = False

# Finding the maximum bid and displaying the winner.
max_bid = max(auction_list, key = auction_list.get)
print(f"The winner is {max_bid} with an amount of ${auction_list[max_bid]}")
