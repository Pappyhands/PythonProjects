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


# checks if user entered data is within the set of data, displays results
def checkData(data, userInput, check):
    for product in data:
        if userInput.upper() in product[check].upper():
            print "%s - %s" % (product["Product"], product["Price"])


# main function
def main():
    data = readJson('PetStore.json')
    userInput = Toolbox.userString("Search by category (c) or keyword (k)?: ")
    
    # if case to decide where the checkData function will be looking with the data set
    if userInput.upper() == "C":
        userInput = Toolbox.userString("Enter a category: ")
        checkData(data, userInput, "Category")
    elif userInput.upper() == "K":
        userInput = Toolbox.userString("Enter a keyword: ")
        checkData(data, userInput, "Product")
    
    

main()
    