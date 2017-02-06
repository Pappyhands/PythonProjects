import Toolbox

adj1 = Toolbox.userString("Enter an adjective: ")
adj2 = Toolbox.userString("Enter anoter adjective: ")
pluralNoun1 = Toolbox.userString("Enter a plural noun: ")
pluralNoun2 = Toolbox.userString("Enter another plural noun: ")
celeb = Toolbox.userString("Enter a celebrity: ")
noun = Toolbox.userString("Enter a noun: ")
print 
print "In the shadow world of spies, a/an %s organization like the US Government uses spies to infiltrate %s groups for the purpose of obtaining top secret %s. A teacher, %s, or even the little old %s with a cane and fifteen pet %s could be a spy." % (adj1, adj2 , pluralNoun1, celeb, noun, pluralNoun2)