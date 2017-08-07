from pygame import mixer
from datetime import datetime
import time

# Program is called at startup at /etc/rc.local
#'''
mixer.init()
mixer.music.load('/home/pi/Documents/ACC/start.mp3')
mixer.music.play(1)
time.sleep(59)
mixer.music.fadeout(5000)
time.sleep(5)
#'''
while(1):
    mixer.music.load('/home/pi/Documents/ACC/{}.mp3'.format(datetime.now().hour))
    mixer.music.play(-1)
    time.sleep(60 *(59 - datetime.now().minute) + (55 - datetime.now().second))
    mixer.music.fadeout(5000)
    time.sleep(5)



