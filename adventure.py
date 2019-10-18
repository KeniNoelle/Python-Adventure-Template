__author__ = 'Les Pounder'

"""
    The lines below import modules of code into our game,
    in particular these import time functions allow us to pause and stop the game,
    and random provides a method of choosing random numbers or characters.
"""
from time import *
from random import *
import os,sys
from art import *

"""
    Simple function that clears the terminal screen
"""
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def title():
    print(text2art('Be', font='alpha'))
    print(text2art('  a', font='alpha'))
    print(text2art(' Rebel', font='alpha'))
    print(text2art('But', font='alpha'))
    print(text2art('Not', font='alpha'))
    print(text2art('Too', font='alpha'))
    print(text2art('Much', font='alpha'))




def north():
    print ("To go north press n then enter")

def east():
    print ("To go east press e then enter")

def south():
    print ("to go south press s then enter")

def west():
    print ("To go west press w then enter")


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What's your name student?")
    #randint is a great way of adding some variety to your players statistics through randomness
    HP = randint(5,20)
    MP = randint(5,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi", "Are you a student here?", "What year are you in?", "The humdrum sent a dragon!"]
    npcnamechoice = ["Penelope", "Simon", "Agatha", "Tyrannus Basilton Grimm-Pitch"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to the student")
    if input() == "y":
        print ("%s: %s" % (npcname, responses[0]))
    else:
        print ("%s: Goodbye" % npcname)

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "Dragon"
    print ("\nSuddenly you hear a roar, and from the sky you see an "+enemyname+" coming straight at you....")
    #print enemyname
    print ("Your enemy has %s Health Points" % str(enemyHP))
    print ("Your enemy has %s Magic Points" % str(enemyMP))

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi", "Are you a student here?", "What year are you in?", "The humdrum sent a dragon!"]
    npcnamechoice = ["Penelope", "Simon", "Agatha", "Tyrannus Basilton Grimm-Pitch"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to the student")
    if input() == "y":
        print ("%s: %s" % (npcname, responses[0]))
    else:
        print ("%s: Goodbye" % npcname)

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "Dragon"
    print ("\nSuddenly you hear a roar, and from the sky you see an "+enemyname+" coming straight at you....")
    #print enemyname
    print ("Your enemy has %s Health Points" % str(enemyHP))
    print ("Your enemy has %s Magic Points" % str(enemyMP))

def unicorn():
    print ("You glide through the portal to your right and sure enough there is a unicorn waiting for you.")
    print ("To pet the pretty pony input p")
    print ("To greet the beast as you would a friend input g")
    if input() == "p":
        print("You have offended the unicorn.")
        sleep(4)
        print("The unicorn seeks revenge.")
        sleep(4)
        print("The unicorn spears you through you're stomache with it's noble horn.")
        sleep(4)
        print("You bleed out slowly, unable to move, not even in your own dimension.")
        sleep(4)
        print("How tragic.")
        sys.exit(0)
    elif input() == "g":
        print("The unicorn stands up on it's hind legs and greets you holding out it's hoove for you to shake")
        print("Input y to shake the unicorn's hoove.")
        if input() == "y":
            print("The unicorn says it want's to marry you. Input y to marry the unicorn.")
            if input() == "y":
                print("You live happily ever after.")
                sys.exit(0)
            else:
                print("The unicorn kills you for wasting it's time.")
                sys.exit(0)
        else:
            print("The unicorn is becoming enraged. You have two options, run or die.")
            print("Input r to run")
            print("Input d to die")
            if input() == "r":
                print("You run in a random direction into this strange land, which turns out to be mostly forest.")
                print("You slowly die of not knowing how to survive in the wild.")
                sys.exit(0)
            elif input() == "d":
                print("Okay.")
                sys.exit(0)

def deadCassie():
    print("Would you like to hide? Input y to hide.")
    if input() == "y":
        print("Scott Summers (the jerk that he is) catches you, blasts you and you die.")
        sys.exit(0)
    else:
        print("yee")

def glitchinthematrix():
    print("Your soul which was previously playing this game has now re-entered your body.")
    print("Now get up and go live you're life.")
    sys.exit(0)


"""
    We now use our functions in the game code, we call functions title() and setup() for our character.
"""
clear_screen()
title()
setup()
global name
global HP
global MP
global move
global enemyHP
print ("Welcome to the Watford School of Magicks, %s" % name)
#Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour health is" + " " + str(HP))
print ("Your magic skill is" + " " + str(MP))



print ("Would you like to explore the school? Press y then enter to continue")
#Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    print ("You are in your room, working on your homework, your wand is lying on your bed.")
    print ("Would you like to take wand and summon the sword of mages? Press y then enter to continue")
    if input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("sword")
        weapons.append("wand")
        print ("You are now carrying your %s and your %s" % (weapons[0], weapons[1]))
        print ("Armed with your %s and %s you swing open the door to your room, out of your house, and see a green field gleaming in the sunshine." % (weapons[0], weapons[1]))
    else:
        print ("You choose not to take your weapons")
        print ("You open the door to the stairs and begin to walk.")
        print ("You here an odd noise to the right of you while on the stairs. Would you like to instinctivly look in it's direction for a split second while you continue your main task?")
        if input() == "y":
            print ("You aren't looking where you are going while on the stairs.")
            print ("You trip and fall to your death.")
            print ("Game Over (obviously)")
            sys.exit(0)
        else:
            print ("Good choice.")


else:
    print ("You stay in your room, sitting at your desk and do your homework. You die of boredom.")
    print ("Game Over")
    sys.exit(0)

print ("In the distance to the north you can see a the white chapel, to the east you can see the wavering wood and to the west the weeping tower.")

#Remember those functions we created at the start of the code? Well here we are using them in the game.
print ("\n")
north()
east()
west()
move = input("Where would you like to go? ")
if move == 'n':
    print ("\nYou move to the north, walking under the cloudy sky.")
    print ("You see you're friend ")
    print ("A student is in your path and greets you")
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == 'e':
    print ("\nYou walk to the wavering wood which sucks, why did you go there? Anyways...")
    print ("A student is in your path and greets you")
elif move == 'w':
    print ("\nYou walk to the weeping tower, stopping to reget your descision wondering what you think you're doing. What are you planning on doing, seeing the mage? No one likes the mage!")
    print ("A student is in your path and greets you\n")
else:
    print ("a rebel huh. you've unlocked a bonus quest!")
    print ("suddenly a portal opens on the ground a step ahead of you. Input 'y' to step through.")
    if input() == "y":
        print ("you fall through the multiverse, viewing many different realities as you fall.")
        print ("It appears that you can enter whichever you please. But for the simplicity of this game I'm only going to give you three options.")
        print ("You see a majestic unicorn in the portal to you're right, to you're left you catch a glimpse of Scott lang holding his dead daughter surrounded by the Young Avengers with the Avengers and X-Men standing nearby with a look of guilt as they know this is all their fault and that if they had just listened to Wiccan none of this would have happened, and below you you see yourself in this very moment.")
        print ("To go right input r")
        print ("To go left input l")
        print ("To go down input d")
        if input() == "r":
            unicorn()
        elif input() == "l":
            deadCassie()
        elif input() == "d":
            glitchinthematrix()
        else:
            print("im actually mad u pulled that")
            sys.exit(0)
    else:
        print ("Really?")
        sleep(2)
        print ("You're a coward, you know that?!?!")
        sleep(2)
        print ("No more game for you.")
        print (":(")
        sys.exit(0)




villager()
enemy()
sleep(3)

fight = input("Do you wish to fight?" )

if fight == "y":
    while HP > 0:
#This loop will only work while our characters HP is greater than 0.
        hit = randint(0,5)
        print ("You cast a spell and cause %s of damage" % str(hit))
        enemyHP = enemyHP - hit
        sleep(2)
        print (enemyHP)
        enemyhit = randint(0,5)
        sleep(2)
        print ("The dragon breathes fire at you at you and causes %s of damage" % str(enemyhit))
        HP = HP - enemyhit
        sleep(2)
        print (HP)
else:
    print ("You turn and run away from the dragon, like a sensible person, let Simon Snow handle that.")


print ("   ,")
print ("_,,)\.~,,._")
print ("(()`  ``)\))),,_ ")
print (" |     \ ''((\)))),,_          ____")
print (" |6`   |   ''((\())) '-.____.-'    `-.-,")
print (" |    .'\    ''))))'                  \)))")
print (" |   |   `.     ''                     ((((")
print (" \, _)     \/                          |))))")
print ("  `'        |                          (((((")
print ("            \                  |       ))))))")
print ("             `|    |           ,\     /((((((")
print ("              |   / `-.______.<  \   |  )))))")
print ("              |   |  /         `. \  \  ((((")
print ("              |  / \ |           `.\  | (((")
print ("              \  | | |             )| |  ))")
print ("               | | | |             || |  '")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")
print ("	           | | | |             || |  ")

