from random import randint
from time import sleep
from keyboard import press, release, wait
from spelunkymemreader import readWord

up, left, down, right = 'i', 'j', 'k', 'l' #cannot use arrow keys; keyboard module outputs numpad arrow events
jump, whip, bomb, rope = 'z', 'x', 'a', 's' #bomb and rope switched from defaults!
door = 'space' #also purchase
#run is toggled on at all times

pid = int(input('process id in hex > '),16)

def gameState():
    #thanks to Sawr - https://github.com/Sawrr/Spelunky-RTA-Tracker/blob/master/AchievementsTracker/AchievementsTracker/ScreenState.cs
    #the pointers to find it were also lifted from this
    return readWord(pid, readWord(pid, 0x2784b4) + 0x58)

def play():
    horiz = randint(0,2)
    if horiz == 1:
        press(left)
    elif horiz == 2:
        press(right)
        
    vert = randint(0,2)
    if vert == 1:
        press(up)
    elif vert == 2:
        press(down)
        
    jumpy = randint(0,1)
    if jumpy == 1:
        press(jump)
        
    action = randint(0,199)
    if action == 1:
        press(bomb)
    elif action == 2:
        press(rope)
    elif action > 100:
        press(whip)

    sleep(randint(1,60) / 60) #1-60 frames of a random action
    for i in [up, left, down, right, jump, whip, bomb, rope]:
        release(i)
        
    press(door) #then attempt to exit (or purchase something)
    sleep(1/60)
    release(door)

def loading():
    sleep(1)

def levelTransition():
    press(jump)
    sleep(1/60)
    release(jump)
    sleep(1)
    
def restart():
    press(whip)
    sleep(1/60)
    release(whip)
    sleep(1)

print('click into spelunky then press p to start the bot')
wait('p')
while 1:
    gs = gameState()
    if gs == 0:
        play()
    elif gs in [1,2,3]:
        loading()
    elif gs == 11:
        levelTransition()
    elif gs == 30:
        restart()
    else:
        print('error: unknown game state',gs)
        break
