import Toolbox
import os

# --------------------------------------------------------------
# returns a list of all files in directory that end with '.txt'
# --------------------------------------------------------------
def getTxtFiles():
    files = os.listdir(".")

    newFiles = []

    for f in files:
        if ".txt" in f:
            newFiles.append(f)
    return newFiles

# --------------------------------------------------------------
# reads each individual file for a list and creates data set 
# using a dictonary in which each key is the name of the file and 
# the value for those keys are data from each given file
# --------------------------------------------------------------
def readFiles(files):
    catalog = {}
    for file in files:
        data = []
        for line in open(file):
            data.append(line.upper())
    
        catalog[file] = data

    return catalog
    
# --------------------------------------------------------------
# takes in search word for user and Data Set of text within
# files. Searches each file, line by line, looking for the
# search term. If found increments 'count' by 1 and adds the
# file name + line to a key list of results, returns the results
# --------------------------------------------------------------
def searchFileData(word, dataSet):
    
    count = 0;
    fileData = []
    for key, value in dataSet.items():
        for line in value:
            if word.upper() in line:
                x = "%s: %s" % (key, line)
                x = x.strip()
                fileData.append(x)
                count += 1
    print "I found %s results." % count
    return fileData

# --------------------------------------------------------------
# pulls it all together.
# --------------------------------------------------------------
def main():
    # searches current directory for files ending in '.txt'
    files = getTxtFiles()
    
    # reads the data from files
    dataSet = readFiles(files)
    
    # prompts user for a search term
    userInput = Toolbox.userString("Enter a search term:"),
    
    # returns the results of matching lines
    results = searchFileData(userInput[0], dataSet)
    
    # displays all the results
    for value in results:
	    print value
    
main()