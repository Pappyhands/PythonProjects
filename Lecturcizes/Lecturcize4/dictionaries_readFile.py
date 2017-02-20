d = {}

for line in open('dictionaries_data.txt'):
    temp = line.split(',')
    name = temp[0].strip()
    age = temp[1].strip()
    d[name] = age

print "%s -> %s" % (d.keys(), d.values())

print "Enter a name:",
n = raw_input()

print d[n]