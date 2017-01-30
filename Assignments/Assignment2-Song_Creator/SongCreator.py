import Toolbox

data = []

#Promting user WHILE adding to user data list.
data.append(Toolbox.userString("Enter the first verse: "))
data.append(Toolbox.userString("Enter the second verse: "))
data.append(Toolbox.userString("Enter the third verse: "))
data.append(Toolbox.userString("Enter the fourth verse: "))
data.append(Toolbox.userString("Enter the chorus: "))
data.append(Toolbox.userInt("Repeat Chorus __ amount of times: "))

# print data

omt = ["...one more time!..."]

#setting chorus
chorus = data[4] + " "

# print chorus

script = []
for i in xrange(len(data)-2):
    script.append(data[i])
    if(i == len(data)-3):
        script.append(chorus * (data[5]+1))
    else:
        script.append(chorus * data[5])
        
# adds it all together to make the song
lyrics = []
lyrics = script + omt + script

print lyrics

print
print 'BEFORE the ban on "cookies"'

for word in lyrics:
    print word
    
print 
print 'AFTER the ban on "cookies"'

lyrics = [w.replace('cookies', '_______') for w in lyrics] #sensoring all instances of 'cookies'
for word in lyrics:
    print word
    
    

        
