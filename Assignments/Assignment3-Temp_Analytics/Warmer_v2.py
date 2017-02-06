import Toolbox

# Opens File and Compiles formatted list of values
def readTemps():
    file = open('temps.txt', 'r')
    m_temps = []
    
    # removes '\n' (new line) character from strings
    for line in file:
        temp = line.replace('\n','')
        m_temps.append(temp)
    
    # converts all strings to floats in the list
    m_temps = [float(i) for i in m_temps]

    return m_temps


# Calculates the avg from a starting point to an ending point in a list
def calculateAve(temps, start, stop):
    ave = 0
    rangeOfTemps = temps[start:stop]
    for num in rangeOfTemps:
        ave += num
        
    ave = ave / len(rangeOfTemps)
    return ave
    
# Counts how many anomolies are above 0
def count(temps, start, stop):
    count = 0
    rangeOfTemps = temps[start:stop]
    for num in rangeOfTemps:
        if num > 0:
            count += 1
    
    return count

# Testing everything above
def main():
    temps = readTemps()
    
    # Explains how the program actual works. 
    # NOTE TO SELF: Try and figure out how to compare two different percentages (ie. first 50% against last 20%)
    print "*Note: If you enter '80' as a percentage, you would be comparing the first '80%' to the last '20%'.\n"
    userPercent = Toolbox.userInt("Please enter a percentage: ")
    
    # Figuring out how many items the user percentage includes (ie. 70% of 116 temps = 81 items in firstPart, and 30% of 116 temps = 35 leftover items)
    firstPart = int(len(temps)*(userPercent*0.01)) # <- Mark Cohen was Here.
    secondPart = len(temps) - firstPart
    
    # Shows what percentages we are comparing
    print "\nNow comparing the first " + str(userPercent) + "% with the last " + str(100 - userPercent) + "%.\n"
    
    # Averages
    avg1 = calculateAve(temps,0, firstPart)
    avg2 = calculateAve(temps,firstPart,len(temps))
    
    # Count of values above 0
    count1 = count(temps, 0, firstPart)
    count2 = count(temps, firstPart, len(temps))
    
    # First Percentage
    print 'First ' + str(userPercent) + '%:'
    print 'During the first ' + str(firstPart) + ' years, the average deviation from the temperature anomaly is ' + str(avg1) +'.'
    print 'During the first ' + str(firstPart) + ' years, ' + str(count1) + ' had a positive temperature anomaly.'
    
    # Second Percentage
    print '\nSecond ' + str(100 - userPercent) + '%:'
    print 'During the last ' + str(secondPart) + ' years, the average deviation from the temperature anomaly is ' + str(avg2) + '.'
    print 'During the last ' + str(secondPart) + ' years, ' + str(count2) + ' had a positive temperature anomaly.'
    
    
# Running Main   
main()