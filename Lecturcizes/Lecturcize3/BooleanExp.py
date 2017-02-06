# if height is < 54 or age < 14 cannot ride
# if height == 54 and age == 14 ask attendant
# if height > 54 and age > 14 can ride

import Toolbox

height = Toolbox.userInt("Please enter your height in inches: ")
age = Toolbox.userInt("Please enter your age: ")

if height > 54 and age > 14:
    print "You can ride!"
elif height < 54 or age < 14:
    print "You cannot ride!"
elif height == 54 and age == 14:
    print "You musk ask!"


