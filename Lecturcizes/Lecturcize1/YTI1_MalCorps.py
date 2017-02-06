print 'How many malcorps did you find on planet Exflon?:',
exflon = raw_input()

print 'How many malcorps did you find on planet Mobiles?:',
mobiles = raw_input()

print 'How many malcorps did you find on planet Monsantoes?:',
monsantoes = raw_input()

total = int(exflon) + int(mobiles) + int(monsantoes)
avg = total / 3.0

print 'You found %i malcorps!' % total

print 'The average malcoprs per planet is %.2f' % avg