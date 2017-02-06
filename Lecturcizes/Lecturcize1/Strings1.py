print "What is your name?",
name = raw_input()
print "%s, your name is %s characters long." % (name, len(name))


s1 = "Python is boring!"
s2 = s1.replace('boring' , 'awesome')
print s2

print s1[0]

print "Python" in s1