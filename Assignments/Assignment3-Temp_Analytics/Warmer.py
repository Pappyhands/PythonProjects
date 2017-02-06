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
    avg1 = calculateAve(temps,0,81)
    avg2 = calculateAve(temps,81,116)
    
    count1 = count(temps, 0, 81)
    count2 = count(temps, 81,117)
    
    # 0 - 81
    print 'During the first 81 years, the average deviation from the temperature anomoly is ' + str(avg1)
    print 'During the first 81 years, ' + str(count1) + ' had a positive temperature anomoly'
    
    # 82 - 116
    print 'During the last 35 years, the average deviation from the temperature anomoly is ' + str(avg2)
    print 'During the last 35 years, ' + str(count2) + ' had a positive temperature anomoly'
    
    
# Running Main   
main()