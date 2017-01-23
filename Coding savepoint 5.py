#README
#This file is copyrighted property of the TAA Year 10 YGD_Bafta Project for making.
#This project is officially created by John O'Sullivan and Jack Downie-webb
#Assistant creators joining after initial collaboration are Zander Brown and Destiny Abagonisaede
#README
import sys
import time

#begin program

#introduction to program
print("Welcome to the Mass Effect Experience")

time.sleep(3)

print("Along this game you will experience a fan-made story")

time.sleep(3)

print("Within this game you will be partaking in the escape")

time.sleep(3)

print("Of the S.S.V Normandy SR2.")

time.sleep(3)

print("First sir, we need your name and age")

name = str(input("Please enter your name into the registry: "))

age = int(input("Please input your age Captain:"))

print("Welcome to the Normandy Captain",name)

#introduction to simulation
time.sleep(3)

room_CIC_description = """

Welcome to the CIC, captain. This is the command intelligence centre aboard the
S.S.V Normandy SR2. Within this simulation, you will experience the abandon ship
protocols put in place to protect you and the crew sir.

To escape, please traverse the ship to escape in this scenario where
certain features of the ship are locked off and others are available.

"""

time.sleep(2)

#description

room_GalaxyMap_description = "Captain, this is the galaxy map captain,unfortunately this is locked off due to the emergency.Step back from the pedestal by typing B"
room_BridgeHallway_description = "Captain, this is the hallway to the airlock, to go forward type F otherwise return to CIC with B"
room_PortAirlock_description = "Captain, you cannot enter without a spacesuit, return to Bridge Hallway by typing B"
room_SouthAirlock_description = "Captain, you cannot enter without a spacesuit, return to Bridge Hallway by typing B"
room_Bridge_description = "Captain, we have lost power to the bridge, we cannot steer unless you restore power, return to Bridge Hallway by typing B"
room_Lift_description = "Captain, this is the lift, and its working, choose a floor by typing in the floor you want to go to 1-5, type 3 to go back to CIC"
room_Techlab_description = "Captain, this is the tech lab, theres an emergency ladder to deck 3, type S to down the ladder, type E to go to FTL hallway, type B to go back to CIC"
room_FTLHallway_desccription = "Captain, this is the hallway connecting the comms, armory, and tech lab. Type FTL for FTl comms, type Arm for armory or type Tech to return to the tech lab"
room_Armory_description = "Captain, This is the armory where we store weapons, if you want a weapon, head to the locker otherwise leave. Type Locker to headto the locker, else head to the cic by typing cic for head to the hallway by typing e"

pack = ["nothing so far"]

print(room_CIC_description)

print("Captain, where would you like to go?")
print("Your in the CIC , type in what you wish to choose from the list below?")

time.sleep(4)

def dex():
    print(room_CIC_description)
    decisiona = str(input("GalaxyMap,BridgeHallway,Elevator,Techlab,armory"))
    Armory = True
    Elevator = True
    GalaxyMap = True
    BridgeHallway = True
    Techlab = True
    if decisiona.lower() == "armory":
        return()

    if decisiona.lower() == "BridgeHallway":
        return()

    if decisiona.lower() == "Hallway":
        return()

    if decisiona.lower() == "Elevator":
        return()

    if decisiona.lower() == "Techlab":
        return()

time.sleep(3)
dex()

def fix():

 print(room_armory_description)
decisionb = str(input("Would you like to access the terminal, head back to the cic, or go through the hallway?")
    if decisionb.lower() == "terminal": 
                return()

    if decisionb.lower() == "CIC":
                return:

    if decisionb.lower() == "Hallway":
        return()

fix():

print(room_CIC_description)
decisionb = str(input("Would you like to access the galaxy map?, head back to the elevator,go to the armory or techlab or go through the bridge hallwayhallway?")

time.sleep(3)
print("GalaxyMap,BridgeHallway,Armory,Techlab,Elevator
              if decisionb.lower() == "terminal":
                return()

    if decisionb.lower() == "GalaxyMap":
                return:

    if decisionb.lower() == "BridgeHallway":
        return()

    if decisionb.lower() == "Elevator":
        return()
  
    if decisionb.lower() == "Techlab":
        return()

    if decisionb.lower() == "Armory":
        return(99)

time.sleep(5)
