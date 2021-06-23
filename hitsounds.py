import playsound
import keyboard
import random
import time
import os

def sound(chance, soundlist):
    soundname = soundlist[chance]
    playsound.playsound(soundname, block=False)

#getting number and names of mp3s
mp3names = []
for filename in os.listdir():
    file = str(filename).split("'")[0]
    if file.endswith('.mp3'):
        mp3names.append(file)

chance = 0
#infinite loop
while True:
    #setting 0.2 second cooldown so files only play once on hit
    time.sleep(0.2)
    #generating random number for playing a sound if there is more than 1 sound file
    if(len(mp3names) > 1):
        chancenew = chance
        while chancenew == chance:
            chancenew = random.randint(0, len(mp3names) - 1)
        chance = chancenew
    #checking if a key is held down
    try:
        if keyboard.read_key():
            sound(chance, mp3names)
    except:
        #does nothing
        print("", end="")
