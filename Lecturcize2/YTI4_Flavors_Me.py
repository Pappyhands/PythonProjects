import Toolbox

flavors = ['vanilla','chocolate','strawberry','bacon']
ratings = []

ratings.append(Toolbox.userInt("Rate %s from 1 to 5: " % flavors[0]))
ratings.append(Toolbox.userInt("Rate %s from 1 to 5: " % flavors[1]))
ratings.append(Toolbox.userInt("Rate %s from 1 to 5: " % flavors[2]))
ratings.append(Toolbox.userInt("Rate %s from 1 to 5: " % flavors[3]))

display = []
display.append("%s rated as a %s" % (flavors[0], ratings[0]))
display.append("%s rated as a %s" % (flavors[1], ratings[1]))
display.append("%s rated as a %s" % (flavors[2], ratings[2]))
display.append("%s rated as a %s" % (flavors[3], ratings[3]))

print display