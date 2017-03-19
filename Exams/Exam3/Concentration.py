import Toolbox
import random

# Generates a Randomized Set of choices
def makeGame(choices):
    
    r = random.randrange(0, 9)
    choices.append(choices[r])
    random.shuffle(choices)
    
    return choices

# Checks the values of of the picks to make sure that they are allowed
def checkPicks(firstPick, secondPick):
    
    if firstPick > 9 or firstPick < 0:
        print "\nInvalid Input! You must pick different cards and the card must be a number from 1-10.\n"
        return False
    elif secondPick > 9 or secondPick < 0:
        print "\nInvalid Input! You must pick different cards and the card must be a number from 1-10.\n"
        return False
    elif firstPick == secondPick:
        print "\nInvalid Input! You must pick different cards and the card must be a number from 1-10.\n"
        return False
        
    return True

# Building the Prompt
def main():
    
    choices = ['bird', 'dog' , 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
    makeGame(choices)
    pickTest = False
    
    while pickTest == False:
        
        print "Pick the first card to turn over (1-10): ",
        firstPick = int(raw_input()) - 1
        
        print "Pick the second card to turn over (1-10): ",
        secondPick = int(raw_input()) - 1
        
        pickTest = checkPicks(firstPick, secondPick)
        
    # BELOW LINE IS USED TO TEST THE PROGRAM
    # print choices
    
    count = 1
    
    while choices[firstPick] != choices[secondPick]:
        
        print "\nCard %s is a %s." % (firstPick + 1 , choices[firstPick])
        print "Card %s is a %s.\n" % (secondPick + 1 , choices[secondPick])
        
        count += 1
        
        pickTest = False
        while pickTest == False:
        
            print "Pick the first card to turn over (1-10): ",
            firstPick = int(raw_input()) - 1
        
            print "Pick the second card to turn over (1-10): ",
            secondPick = int(raw_input()) - 1
        
            pickTest = checkPicks(firstPick, secondPick)
            
    print "\nCard %s is a %s." % (firstPick + 1 , choices[firstPick])
    print "Card %s is a %s.\n" % (secondPick + 1 , choices[secondPick])
    
    print "You win! It took you %s tries." % count
    

# Calling main
main()