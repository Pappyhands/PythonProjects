print '-- Welcome to Recipe Converter! -- '
print '-- Original Recipe --'

# Takes Initial User Inputs
print 'Please enter the amount of Flour (cups): ',
flour = raw_input()

print 'Please enter the amount of Water (cups): ',
water = raw_input()

print 'Please enter the amount of Salt (teaspoons): ',
salt = raw_input()

print 'Please enter the amount of yeast (teaspoons): ',
yeast = raw_input()

# Loaf Adjustment
print 'Please enter the loaf adjustment factor (e.g. 2.0 = double the size): ',
loafAdjust = raw_input()

# Modified Recipe Calculations

ModifiedFlour = float(flour) * float(loafAdjust)
ModifiedWater = float(water) * float(loafAdjust)
ModifiedSalt = float(salt) * float(loafAdjust)
ModifiedYeast = float(yeast) * float(loafAdjust)

print ''
print '-- Modified Recipe --'
print 'Flour: %.2f cups' % ModifiedFlour
print 'Water: %.2f cups' % ModifiedWater
print 'Salt: %.2f teaspoons' % ModifiedSalt
print 'Yeast: %.2f teaspoons' % ModifiedYeast

# Modified Recipe in Grams Calculations

ModifiedFlourGrams = float(flour) * float(loafAdjust) * 120
ModifiedWaterGrams = float(water) * float(loafAdjust) * 237
ModifiedSaltGrams = float(salt) * float(loafAdjust) * 5
ModifiedYeastGrams = float(yeast) * float(loafAdjust) * 3

print ''
print '-- Modified Recipe in Grams--'
print 'Flour: %.2f g' % ModifiedFlourGrams
print 'Water: %.2f g' % ModifiedWaterGrams
print 'Salt: %.2f g' % ModifiedSaltGrams
print 'Yeast: %.2f g' % ModifiedYeastGrams

print 'Happy Baking!'