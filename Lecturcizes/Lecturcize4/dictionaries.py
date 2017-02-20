d = {
    "Tim" : ['red','blue'],
    "Sally" : ['blue','green','yellow']
}

# print d['Tim'][0]

# print d.values()

# print 'Tim' in d

# print len(d)

for k in d.keys():
    print "%s -> %s" % (k, d[k])
