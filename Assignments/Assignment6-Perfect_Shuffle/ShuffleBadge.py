import Toolbox
import random

# Suits and Ranks of Cards
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']


# Adds a card for every rank from every suit
def buildDeck(rank, suit):
    deck = [r + " of " + s for r in rank for s in suit]
    return deck
    

# Performs a "Random Shuffle"
def shuffle(deck):
    random.shuffle(deck)
    return deck

# Returns first 5 cards from the top of the deck
def deal(deck):
    return deck[:5]

# Prompts user for how many shuffles to perform, returns a hand of 5 cards
def main():
    deck = buildDeck(rank,suit)
    
    count = Toolbox.userInt("How many times do you want me to shuffle?: ")
    
    for i in range(0,count):
        shuffle(deck)
        
    # for card in deck:
    #     print card
        
    print deal(deck);

# Calling main
main()
