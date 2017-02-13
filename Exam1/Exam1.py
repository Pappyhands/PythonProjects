import Toolbox

# By Austin Thompson
# Python Exam #1

# Reads File and converts all items into floats
def readDataFloat(file): # Note to Self: Add this 'Toolbox' as this will be useful
    l = []
    file = open(file)
    for line in file:
        l.append(line.strip())
    
    # Converts all items in list to floats (where the magic lives)
    l = [float(i) for i in l]
    return l

# Calculates the average of a list of numbers
def getAverage(l):
    total = 0.0
    
    for num in l:
        total += num
    
    total /= len(l)
    return total

# Counts how many numbers within a list are above an adjustable limit
def countSpeeders(l, maxSpeed):
    count = 0
    for num in l:
        if num >= maxSpeed:
            count += 1
    return count

# Calculates the fine of all the speeds depending on if they were during rush hour or not
def calculateFine(num, speeding):
    fine = 0.0
    
    # Rush Hour 
    if speeding:
        fine = num * 150
    # Not Rush Hour
    else:
        fine = num * 100
        
    return fine

# Creating a Main function that runs all the code and displays an output
def main():
    
    # Not Rush Hour Stats
    nRush = readDataFloat("data-not-rush.txt")
    nR_Avg = getAverage(nRush)
    nR_Speeders = countSpeeders(nRush, 70)
    nR_Fines = calculateFine(nR_Speeders, False)
    
    # Rush Hour Stats
    Rush = readDataFloat("data-rush.txt")
    R_Avg = getAverage(Rush)
    R_Speeders = countSpeeders(Rush, 70)
    R_Fines = calculateFine(R_Speeders, True)
    
    # Printing out the results
    print "The average speed during rush hour was %.2f." % R_Avg
    print "The average speed not during rush hour was %.2f." % nR_Avg
    print "There were %i speeders during rush hour.  Total fine = $%i" % (R_Speeders, R_Fines)
    print "There were %i speeders during rush hour.  Total fine = $%i" % (nR_Speeders, nR_Fines)

main()