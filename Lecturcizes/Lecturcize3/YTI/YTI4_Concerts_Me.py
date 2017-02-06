import Toolbox

file = open('concerts.txt', 'r')
userChoice = Toolbox.userString("Enter  the band you want to follow: ")

print "--------------"

for line in file:
    if userChoice in line:
        print line,

print "\nHave fun and wear your ear plugs!"