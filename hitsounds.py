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
while True:
    time.sleep(0.2)
    if(len(mp3names) > 1):
        chancenew = chance
        while chancenew == chance:
            chancenew = random.randint(0, len(mp3names) - 1)
        chance = chancenew
    try:
        if keyboard.read_key():
            sound(chance, mp3names)
    except:
        print("", end="")
