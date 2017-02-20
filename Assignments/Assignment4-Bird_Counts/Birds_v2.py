# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

import Toolbox

def countBirds(file):
    d = {}
    
    for line in open(file):
        
        # Seperating Data
        temp = line.split(",")
        birdName = temp[0].strip().upper() # Pt.1 ) Changing all names to Upper Case for easier case insensitive
        birdSightings = int(temp[1].strip())
        
        # If a bird hasn't been seen before add it to the dictionary, else adding all the sightings together
        if birdName not in d.keys():
            d[birdName] = birdSightings
        else:
            d[birdName] += birdSightings
    
    return d

def askUser(d, repeat):
    
    # Repeat until user inputs "Exit" (case insensitive)
    while repeat:
        # Finding the Most Sighted Bird
        mostCount = 0
        mostSeen = {}
        
        # Finding the largest value amongst the data
        for bird in d:
            if d[bird] >= mostCount:
                mostCount = d[bird]
        
        # Adding all birds with largest value as their own values into a secondary dictionary
        for bird in d:
            if d[bird] == mostCount:
                mostSeen.update({bird:d[bird]})
        
        print "Most Sighted Bird(s): %s" % mostSeen
        
        print "Type 'Exit' to end the program."
        
        # Prompting for User Input
        n = Toolbox.userString("Enter a bird name:").upper() # Pt.2 ) Changing all user inputs to Upper Case for easier case insensitive
        
        # Checking to see if the bird has any sightings
        if n == "EXIT":
            print "Goodbye!\n"
            repeat = False
        elif n in d:
            print "I have seen that bird %i time(s).\n" % d[n]
        else:
            print "I have seen that bird %i time(s).\n" % 0

# Pulling it all together
def main():
    askUser(countBirds("Birds.txt"), True)
    
main()