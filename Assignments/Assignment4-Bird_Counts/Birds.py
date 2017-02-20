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
# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds(file):
    d = {}
    
    for line in open(file):
        
        # Seperating Data
        temp = line.split(",")
        birdName = temp[0].strip()
        birdSightings = int(temp[1].strip())
        
        # If a bird hasn't been seen before add it to the dictionary, else adding all the sightings together
        if birdName not in d.keys():
            d[birdName] = birdSightings
        else:
            d[birdName] += birdSightings
    
    return d
# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    n = Toolbox.userString("Enter a bird name:")
    if n in d:
        return "I have seen that bird %i time(s)." % d[n]
    else:
        return "I have seen that bird %i time(s)." % 0
    
def main():
    print askUser(countBirds("Birds.txt"))
    
    

main()