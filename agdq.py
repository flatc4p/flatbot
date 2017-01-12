# intentioned for flatbot
# parses the timetable from gamesdonequick.com for the ongoing event and returns upcoming games


import re
import mechanicalsoup
from datetime import datetime

lookuptime = datetime.now()

browser = mechanicalsoup.Browser()
schedule = browser.get("https://gamesdonequick.com/schedule")
datestring = str(lookuptime.date())
timestring = str(lookuptime.time())
timestring = re.split('\.',timestring)[0]
print("Current date: ", datestring)
print("Current time: ", timestring)
times = re.split(datestring.encode(),schedule.content)[1]
#print(schedule.content)

for entry in re.split(datestring.encode(),schedule.content):
    print(re.split(b'Z', re.split(b'T', entry)[1])[0])

print("Ende")
