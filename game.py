"""
(C) Copyright 2017 TAA BAFTA Game Project

This file is copyrighted property of the TAA Year 10 YGD_Bafta Project for
making. This project is officially created by John O'Sullivan and
Jack Downie-Webb assistant creators joining after initial collaboration are
Zander Brown and Destiny Abagonisaede
"""

from time import sleep
from json import load as load_json


def get_string():
    with open('strings.json') as f:
        try:
            return load_json(f)
        except ValueError:
            print('Failed to load strings!')


# begin program

# hi.

# introduction to program

for msg in get_string()['start']['scrolling']:
    print(msg)
    sleep(3)

print("First sir, we need your name and age")

name = str(input("Please enter your name into the registry: "))

age = int(input("Please input your age Captain:"))

print("Welcome to the Normandy Captain", name)

# introduction to simulation
sleep(3)

# description

pack = ["nothing so far"]

# Because strings are stored in JSON and JSON doesn't support multiline
# strings each line is sored as a list element. This sticks them back
# together joining them with the newline chareter
print('\n'.join(get_string()['room']['CIC']['description']))
print("Captain, where would you like to go?")
print(get_string()['general']['yourin'].format(room='CIC'))

sleep(4)


def dex():
    print('\n'.join(get_string()['room']['CIC']['description']))
    decisiona = str(input("GalaxyMap,BridgeHallway,Elevator,Techlab,armory"))
    Armory = True
    Elevator = True
    GalaxyMap = True
    BridgeHallway = True
    Techlab = True
    if decisiona.lower() == "armory":
        print(get_string()['room']['Armory']['description'])
        sleep(3)
        print(get_string()['room']['Armory']['enter'])
dex()
