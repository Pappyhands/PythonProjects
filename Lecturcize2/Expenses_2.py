import Toolbox

kmWeekday = Toolbox.userInt("How many km did you travel on a weekday?")
kmWeekend = Toolbox.userInt("How many km did you travel on a weekend?")

miWeekday = Toolbox.kmToMi(kmWeekday)
miWeekend =Toolbox. kmToMi(kmWeekend)

dollarsWeekday = miWeekday * 0.13
dollarsWeekend = miWeekend * 0.23

print "Weekday $%.2f" % dollarsWeekday
print "Weekend $%.2f" % dollarsWeekend
print "Total $%.2f" % (dollarsWeekday + dollarsWeekend)