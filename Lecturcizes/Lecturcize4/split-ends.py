# s = "A-B-C-D-E"
# l = s.split('-')
# print l

for line in open('split-ends.txt'):
    temp = line.split(',')
    name = temp[0].strip()
    age = temp[1].strip()
    print name
    print age