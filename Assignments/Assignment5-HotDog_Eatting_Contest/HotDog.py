import random
import time
import Toolbox

# Allows a contest to be repeated, if a secondary contest was made you could easliy change this to work with it by changing the method on line 15

# NOTE TO SELF: This is a little messy, would be neat to make 'runContest()' instead a method that takes a contest as a variable and would run whatever contest you'd pass it. 
# ************* would have to figure out the whole 'userCash' attribute as currently if it is not nested inside of the 'repeatPrompt()' method and passed to the const, but
# ************* instead put inside the contest itself, the variable simply resets because of the 'while' statement within 'repeatPrompt()'

def repeatContest(userCredits): # <--- See above comments
    keepGoing = True
    while keepGoing:
        userCredits= runContest(userCredits) #<--- See above comments
        if userCredits == False:
            keepGoing = False
    print "\nYou're all out of cash! Better luck next time!"


# Runs the Contest a single time through
# NOTE TO SELF: I believe this might able to be broken apart into components to make it more abstract and allow for the easy creation of other contests, look into object orientated design in python (?)

def runContest(userCredits):
    
    
    guess = ""
    
    if userCredits <= 0:
        return False
    else:
        totals = {
            "Tom" : 0,
            "Sally" : 0,
            "Fred" : 0
        }
        print "Remaing Credits: %s" % userCredits
        guess = Toolbox.userString("\nPick a winner (Tom, Sally, or Fred): ")
        bet = Toolbox.userInt("How much do you want to bet? (Credits: %s): " % userCredits)
            
        finishLine = 0
        while finishLine <= 50:
            time.sleep(1)
            print "\nchomp...   chomp...   chomp... \n"
            for person in totals:
                eattenDogs = random.randrange(1, 8)
                totals[person] += eattenDogs
                if totals[person] > finishLine:
                    finishLine = totals[person]
                    winner = person
                print "%s has eaten %s hot dogs!" % (person, totals[person])
        
        if winner == guess:
            userCredits += bet
            print "\nYou guessed right, %s wins! +%s credits." % (winner, bet)
            return userCredits
        else:
            userCredits-= bet
            print "\nNice try, but %s is top dog! -%s credits." % (winner, bet)
            return userCredits

# Starts the prompt             
def main():
    repeatContest(100)
         
main()