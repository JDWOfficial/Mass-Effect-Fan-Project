"""
(C) Copyright 2017 TAA BAFTA Game Project

This file is copyrighted property of the TAA Year 10 YGD_Bafta Project for
making. This project is officially created by John O'Sullivan and
Jack Downie-Webb assistant creators joining after initial collaboration are
Zander Brown and Destiny Abagonisaede
"""

from time import sleep
from shipmap import Map
from util import get_str



# begin program

# introduction to program

for msg in get_str()['start']['scrolling']:
    print(msg)
    #sleep(3)

game = Map(0)
game.pack()

print("First sir, we need your name and age")

#name = str(input("Please enter your name into the registry: "))
name = game.ask_string('Please enter your name into the registry:', 'Name')

#age = int(input("Please input your age Captain:"))
age = game.ask_integer('Please input your age Captain:', 'Age')


print("Welcome to the Normandy Captain", name)

# introduction to simulation
#sleep(3)

# description

pack = ["nothing so far"]

# Because strings are stored in JSON and JSON doesn't support multiline
# strings each line is sored as a list element. This sticks them back
# together joining them with the newline chareter
print('\n'.join(get_str()['room']['CIC']['description']))
print("Captain, where would you like to go?")
print(get_str()['general']['yourin'].format(room='CIC'))

sleep(4)

def dex():
    print('\n'.join(get_str()['room']['CIC']['description']))
    decisiona = game.ask_multiple(get_str()['room']['CIC']['goto'], 'Where To?')
    Armory = True
    Elevator = True
    GalaxyMap = True
    BridgeHallway = True
    Techlab = True
    if decisiona.lower() == "armory":
        print(get_str()['room']['Armory']['description'])
        sleep(3)
        print(get_str()['room']['Armory']['enter'])
dex()
