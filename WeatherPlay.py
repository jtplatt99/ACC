from pygame import mixer
from datetime import datetime
import time
from pyowm import OWM

# Program is called at startup at /etc/rc.local


APIKEY = 'Enter your OWM API key here'
localID = 'Enter your OWM location ID number here'
projectDir = 'Enter your project directory here'

# Comment between this and the following comment to disable startup sequence
mixer.init()
mixer.music.load(projectDir+'start.mp3')
mixer.music.play(1)
time.sleep(59)
mixer.music.fadeout(5000)
# The sequence gives the pi time to connect to the internet to sync its time

owm = OWM(APIKEY)
obs = owm.weather_at_id(localID)	
while(1):
    w = obs.get_weather()
    time.sleep(5)
    if(w.get_status() == 'Snow'):
	mixer.music.load(projectDir+'s{}.mp3'.format(datetime.now().hour))
    elif(w.get_status() == 'Rain'):
	mixer.music.load(projectDir+'r{}.mp3'.format(datetime.now().hour))
    else:
	mixer.music.load(projectDir+'/{}.mp3'.format(datetime.now().hour))
    mixer.music.play(-1)
    time.sleep(60 *(59 - datetime.now().minute) + (55 - datetime.now().second))		# Waits for the next hour
    mixer.music.fadeout(5000)
