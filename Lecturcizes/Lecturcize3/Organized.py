# Gets the predetermined grades
def getGrades():
    grades = [87, 66, 92, 75]
    return grades
    
# Returns the max out of a list of numbers
def getMax(grades):
    largest = 0
    for g in grades:
        if g > largest:
            largest = g
    return largest
    
def main():
    grades = getGrades()
    best = getMax(grades)
    print "Your best grade is %s." % best
    
main()