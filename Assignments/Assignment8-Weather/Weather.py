import Toolbox
import json
import urllib2

def loadJson(url):
    abbr = Toolbox.userString("Please enter a zip code or city name:")
    url += abbr
    jsonTxt = urllib2.urlopen(url).read()
    return json.loads(jsonTxt)

def AnswerPrompt(weather):
    print "\nHere is the current weather for %s, %s." % (weather['location']['name'], weather['location']['region'])
    
    units = Toolbox.userString("Would you like the temperature in Fahrenheit (F) or Celsuis (C)?").upper()
    
    if units != 'F':
        print "\n%s and %s degrees (C)." % (weather['current']['condition']['text'], weather['current']['temp_c'])
        print "It actually feels like %s (C)." % weather['current']['feelslike_c']
    else:
        print "\n%s and %s degrees (F)." % (weather['current']['condition']['text'], weather['current']['temp_f'])
        print "It actually feels like %s (F)." % weather['current']['feelslike_f']
    
    
def main():
    keepTrying = True
    while keepTrying:
        weather = loadJson('https://api.apixu.com/v1/current.json?key=f159b8380cac43d2b1c191629172903&q==')
        AnswerPrompt(weather)
        check = Toolbox.userString("Want to check another location (y/n)?").upper()
        
        if check == "N":
            keepTrying = False
    
main()