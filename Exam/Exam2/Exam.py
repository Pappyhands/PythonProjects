import Toolbox

# Reads in each Player and their times from a txt file
def readData(file):
    d = {}
    for line in open(file):
        data = line.split(",")
        name = data[0].strip()
        value = float(data[1].strip())

        d[name] = value
    return d

# takes in a dictonary and then seperates the players into sub dictonaries based on their time
def seperateData(dic):
    
    # All the different brackets a player can fall into.
    bracket = [
        {'Cube Head (0 - 9.99):' : []},
        {'Square Master (10-19.99):' : []},
        {'Advanced Twister (20-29.99):' : []},
        {'Intermediate Turner (30-39.99):' : []},
        {'Average Mover (40 - 59.99):' : []},
        {'Pathetic (60 and beyond):' : []}
    ]
    
    # Where the actual sorting happens, players are placed into brackets based on their times
    for player in dic:
        if dic[player] < 10:
            bracket[0]['Cube Head (0 - 9.99):'].append(player)
        elif dic[player] > 9.99 and dic[player] < 20:
            bracket[1]['Square Master (10-19.99):'].append(player)
        elif dic[player] > 19.99 and dic[player] < 30:
            bracket[2]['Advanced Twister (20-29.99):'].append(player)
        elif dic[player] > 29.99 and dic[player] < 40:
            bracket[3]['Intermediate Turner (30-39.99):'].append(player)
        elif dic[player] > 39.99 and dic[player] < 60:
            bracket[4]['Average Mover (40 - 59.99):'].append(player)
        elif dic[player] > 59.99:
            bracket[5]['Pathetic (60 and beyond):'].append(player)
                
    return bracket
    
# Main Function
def main():
    
    # Takes the List of Data, formats and displays the results
    data = seperateData(readData("timings.txt"))
    for item in data:
        temp = item
        for i in temp:
            print i
            for y in temp[i]:
                print "        %s" % y
            print


# Calling Main Function
main()
