import Toolbox

sentence = Toolbox.userString("Please enter a sentence: ")
words = sentence.split(' ')
largeWords = []
mediumWords = []
smallWords = []

for word in words:
    if len(word) > 5:
        largeWords.append(word)
    elif len(word) > 3:
        mediumWords.append(word)
    else:
        smallWords.append(word)
        
print largeWords
print mediumWords
print smallWords