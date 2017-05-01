import Toolbox

# asdsadsadsadsad
def createPossibilities():
    weapons = ['Miss Scarlet' , 'Col Mustard', 'Mr Green']
    suspects = ['Candlestick', 'Wrench', 'Pipe']

    p = []
    
    for w in weapons: # 3 times
        for s in suspects: # 3 times
            p.append("%s with the %s" % (w, s))
    
    return p
            # list, string

# adssadsadas
def checkFor(words, word):
    p = []
    
    for w in words:
        if word.upper() not in w.upper():
             p.append(w)
    
    return p

# sadsadsadsad
def main():
    p = createPossibilities()
    print p
    
    while len(p) > 1:
        print "%s possibilities left." % len(p)
        x = Toolbox.userString("Is the clue about a weapon or a suspect (w or s)?: ").upper()
        
        if x == "W":
            clue = Toolbox.userString("Enter the weapon that was not used (['Candlestick', 'Wrench', 'Pipe']): ").upper()
        elif x == "S":
            clue = Toolbox.userString("Enter the innocent suspect (['Miss Scarlet', 'Col Mustard', 'Mr Green']): ").upper()
        
        p = checkFor(p, clue)
    
    print "You found out who commited the fiendish crime! It was %s..." % p[0]
    
main()

    


    

