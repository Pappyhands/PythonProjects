import json
import Toolbox

# Takes a file name and creates a list containing the JSON object
def readJson(file):
    jsonTxt = ""
    f = open(file)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    classes = json.loads(jsonTxt)
    return classes

# Takes a the list containg the JSON object and a user inputted name, prints out contact and course information
def printInfo(classes,name):
    for c in classes:
         if c["Name"] == name:
             print "\nEmail(s):"
             for email in c["Email"]:
                 print email
             print "\nCourses:"
             for course in c["Courses"]:
                 print course

# main function
def main():
    data = readJson('classes.json')
    
    print "Welcome to Class Lookup v0.3..."
    
    # Creates then displays a list of all teachers currently in the JSON file. Adding a new teacher would be very simple.
    teachers = ""
    for d in data:
        teachers += d["Name"].strip()
        teachers += " | "
    print "Current Logged Teachers: %s" % teachers
    
    # prompting user for name of Teacher.
    name = Toolbox.userString("Enter a name:")
    printInfo(data,name)
    

main()
    