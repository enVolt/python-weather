import subprocess
import urllib2
import json
#import pprint

import sched,time

def showmsg(*msg):
	subprocess.Popen(['notify-send',''.join(msg)])
	return

sch = sched.scheduler(time.time, time.sleep)
s = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Delhi")
s = s.read()

data = json.loads(s)

# pprint.pprint(data)
msg = "Temperature = "+str(data["main"]["temp"] - 273.15)+", Location = "+str(data["name"])

for i in range(1,10000,30):
	sch.enter(i,1,showmsg,msg)

sch.run()
