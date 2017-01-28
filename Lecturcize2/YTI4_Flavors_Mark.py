import Toolbox

flavors = ['vanilla','chocolate','strawberry','bacon']
ratings = []

for flavor in flavors:
    rating = Toolbox.userString("Rate %s from 1 to 5: " % flavor)
    ratings.append("%s rated as a %s" % (flavor, rating))

print ratings