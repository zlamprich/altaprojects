#!/usr/bin/python3
from pickle import FALSE
from random import randint
import random
from turtle import width
import dice  # for dice role function
import sys
import os
import pyfiglet  # for banner ASCII art
from os import system  # for windows
import time

result = pyfiglet.figlet_format("SLAYER", font="doh", width=200, )
print(result)
input("Press Enter to Continue")

# function to clear screen


def console():
    print("\nWelcome to Slayer! For eons, tales of legendary beasts and creatures have only been dreamt up in the minds of bards and rooms of local inns; Nothing more than nightmares and folktales.\n" +
          "However, today that all changes...\n" + "\nAs one of the few survivors of a brutal attack on the local town, you find yourself awake at the local Inn, surrounded by chaos. Grab weapons and items to survive!\n" +
          "Slay the monsters you come across and fight your way to the entity that caused all of this! Good luck, Slayer! \n")


console()

input("PRESS ANY KEY TO BEGIN GAME")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# clear the screen
cls()

'''Chad's Ongoing RPG Game'''

bestiary = [{'name': 'ghoul', 'health': 10, 'damage': '1d5'},
            {'name': 'imp', 'health': 10, 'damage': '1d8'},
            {'name': 'skeleton', 'health': 15, 'damage': '1d8'},
            {'name': 'wraith', 'health': 20, 'damage': '1d8'},
            ]
boss = [{'name': 'entity', 'health': 25, 'damage': '1d10'}]
weapon = {'sword': {'damage': '1d10 + 4'},
          'razor': {'damage': '(2d20 + 10)*3'}}


player_health = 20
inventory = []
weapons = []


def combat():
    monster_ID = randint(0, 3)

    global player_health, inventory, weapon, bestiary, boss
    round = 1

    monster_health = bestiary[monster_ID]['health']

    print(
        f"A ferocious {bestiary[monster_ID]['name']} approaches! COMBAT HAS BEGUN!\n")

    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Monster Health: [" + str(monster_health) + "]")

        # gotta write code for cast
        print("Type: RUN, or USE [weapon]")
        # converts move into a lower-case list to deal with each item in list separately
        move = input().lower().split()
        monster_damage = sum(dice.roll(bestiary[monster_ID]['damage']))
        print("\n=========================")

        if move[0] == 'use':
            if move[1] in weapon:  # checks if weapon is in your inventory
                player_damage = dice.roll(weapon[move[1]]['damage'])
                print(
                    f"You hit a {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in weapon:
                print(f"You are not carrying a {move[1]}!")

        if move[0] == 'run':
            # + player_speed # if I set this variable later, here's where it would work
            escape_chance = randint(1, 10)

            if escape_chance >= 10:
                print("You make a flawless escape!")
                break
            if escape_chance >= 5:
                print(
                    "You expose your back as you turn and flee- the monster takes advantage.")
                print(
                    f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
                player_health -= int(monster_damage)
                if player_health >= 1:
                    print("You managed to escape.")
                    break
                if player_health < 1:
                    print("You have been slain.")
                    print("\nGAME OVER")
                    sys.exit()
            if escape_chance >= 0:
                print("The monster out-maneuvers you and attacks! You do not escape.")

        try:
            monster_health -= int(player_damage)
        except:
            pass
        if monster_health <= 0:
            print(
                f"The {bestiary[monster_ID]['name']} lies dead. You are victorious!\n")
            break

        print(
            f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
        print("=========================\n")
        round += 1
        player_health -= int(monster_damage)

        if player_health <= 0:
            print("You have been vanquished! You are dead.")
            sys.exit()


def showInstructions():
    print('''
ZACH'S RPG GAME BUT PARTIALLY RIPPED OFF FROM CHAD
OBJECTIVE: Collect spells and weapon- fight and survive!
--------
Actions:
    GO [north, south, east, west, up, down]
    GET [item, weapon]
    USE [item, weapon]
    LOOK
    INV/INVENTORY
Type 'help' at any time! Type 'q' to quit!''')


def playerinfo():
    #    print('')
    #    print('YOU ARE IN THE ' + currentRoom + '.')
    print('=================================')
    print('Inventory :', str(inventory))
    print('weapon :', str(weapons))
    print('=================================')


def showStatus():  # display the player's status
 #   if 'desc' in rooms[currentRoom]:
 #       print(rooms[currentRoom]['desc'])
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'] +
              rooms[currentRoom]['item_status'] + '.')

    if 'weapon' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['weapon'] +
              rooms[currentRoom]['weapon_status'] + '.')
#    print('=================')


def trap():
    if combat() == False:
        global player_health
    cls()
    traps = ['You feel a pressure plate underneath your foot but it is too late! An arrow suddenly pierces your knee. You\'ll never be an adventurer again.', 'Random numbers suddenly fill your mind, disorienting you. The numbers Mason, what do they mean?!',
             'You find bandages under some rubble! After tending to your wounds, you realize they were all extremely unsterile. You now have dysentry.', 'You find a Green Herb poking out of the ground, famous for its healing capabilities and utilized heavily in a land known as Raccoon City. After consuming it, you realize it was poison ivy, and you should not eat unknown plants.', 'You suddenly hear music playing from behind you. Confused, you turn around only to find a llama with a golden headdress surrounded by guards. After he angrily stops singing, he informs you that you have thrown off his groove. His \
                 guards attack you.']
    print(random.choice(traps))
    print("You have lost 2 Health!")
    player_health -= 2
    print("You now have " + str(player_health) + " health left.")


def boss_battle():
    entity_ID = 0
    global boss_health, player_health, inventory, weapon, boss
    boss_health = boss[entity_ID]['health']
    round = 1

    print(
        f"A dark force materializes within the Basement with you! Shadows overtake the room, and the {boss[entity_ID]['name']} approaches! FIGHT!\n")
    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Boss Health: [" + str(boss_health) + "]")

        # gotta write code for cast
        print("Type: RUN, or USE [weapon]")
        # converts move into a lower-case list to deal with each item in list separately
        move = input().lower().split()
        monster_damage = sum(dice.roll(boss[entity_ID]['damage']))
        print("\n=========================")

        if move[0] == 'use':
            if move[1] in weapon:  # checks if weapon is in your inventory
                player_damage = dice.roll(weapon[move[1]]['damage'])
                print(
                    f"You hit a {boss[entity_ID]['name']} for {player_damage} damage!")
            if move[1] not in weapon:
                print(f"You are not carrying a {move[1]}!")

        if move[0] == 'run':
            # + player_speed # if I set this variable later, here's where it would work
            escape_chance = randint(1, 10)

            if escape_chance >= 10:
                print("You make a flawless escape!")
                break
            if escape_chance >= 5:
                print(
                    "You expose your back as you turn and flee- the monster takes advantage.")
                print(
                    f"A {boss[entity_ID]['name']} hits you for {monster_damage} damage!")
                player_health -= int(monster_damage)
                if player_health >= 1:
                    print("You managed to escape.")
                    break
                if player_health < 1:
                    print("You have been slain.")
                    print("\nGAME OVER")
                    sys.exit()
            if escape_chance >= 0:
                print("The monster out-maneuvers you and attacks! You do not escape.")

        try:
            boss_health -= int(player_damage)
        except:
            pass
        if boss_health <= 0:
            end = pyfiglet.figlet_format(
                "CONGRATULATIONS", font="banner3", width=300, )
            print(
                f"The {boss[entity_ID]['name']} lies dead. You are victorious! The damage has been done but the town is saved. Congratulations, YOU HAVE WON THE GAME!\n")
            print(end)
            input("Press Enter to Exit Game")
            sys.exit()

        print(
            f"A {boss[entity_ID]['name']} hits you for {monster_damage} damage!")
        print("=========================\n")
        round += 1
        player_health -= int(monster_damage)

        if player_health <= 0:
            print("You have been vanquished! The Entity has succeeded!")
            sys.exit()


def random_encounter():
    if ((int(rooms[currentRoom]['randenc'])) + 8) >= 10:
        combat()
    if ((int(rooms[currentRoom]['randenc'])) + 1) == 1:
        boss_battle()
    if ((int(rooms[currentRoom]['randenc'])) + 10) == 11:
        trap()


rooms = {
    'Inn': {
        'south': 'Town Entrance',
        'east': 'Residential Area',
        'weapon': 'sword\n',
        'weapon_status': ' A standard, steel sword. Nothing special',
        'item': 'keyring\n',
        'item_status': ' An ornate keyring with six wings protruding from it. It has an engraving that reads "Mother Miranda" on it. It rests inside of a smashed display case',
        'randenc': '20',
        'desc': 'You are in the main room of the local inn. The scene is grisly, with multiple corpses of the townspeople littered across the floor. You get the feeling you are being watched. Upon exiting \
        you are met with the scene of death and carnage. To the east is the Residential Area. Maybe you can some some of them? To the South is the Town Entrance... Hopefully there may be some survivors there'
    },
    'Town Entrance': {
        'north': 'Inn',
        'randenc': '1',
        'down': 'Stockades',
        'desc': 'You are at the town entrance. What was once a bustling gated entrance to a city is now reduced to rubble. The words "WALL ROSE" are inscribed among the ruins that still stand. There is a column that has been crushed by something, revealing an entrance that goes underground. Where it leads you have no idea.'
    },
    'Stockades': {
        'desc': 'You descend the stairs, taking you from the destroyed town entrance to a sort of underground compound. Using what little light is leaking through, you look around only to see what looks to be an weapon, however all of the equipment has been taken. \
        Upon further inspection you notice a blue and white insignia on the walls with a golden Lion\'s crest on it',
        'randenc': '1',
        'up': 'Town Entrance',
    },
    'Residential Area': {
        'west': 'Inn',
        'south': 'Abandoned House',
        'desc': 'You have arrived at the residential area. From the destruction that still smolders you infer that whatever caused this must be close. To the South there is an Abandoned House, and to the West is the Inn',
        'randenc': '2',
        'item': 'estus\n',
        'item_status': '  An Estus Flask sitting among the bottles of wine. It glows with an orange intensity unlike anything you\'ve ever seen'
    },
    'Abandoned House': {
        'north': 'Residential Area',
        'down': 'Basement',
        'randenc': '20',
        'weapon': 'razor\n',
        'weapon_status': ' A seemingly enchanted dagger of some kind. You can tell it is not from this universe, but still can feel its immense power.\
        You get the sense it belonged to someone named Mehrunes Dagon',
        'item': 'tinypaladin\n',
        'item_status': ' An extremely small, level 2 Paladin sits in a chair in the corner, glowing with righteous might. You suspect he could be a powerful ally, and coincidentally would also fit in your pocket',
        'desc': '  An now abandoned house. It seems the family was not able to flee before whatever force took their lives\
        the stench of stale blood fills the air.',
    },
    'Basement': {
        'up': 'Abandoned House',
        'randenc': '0',
        'item': 'zerg\n',
        'item_status': ' A mini, plastic Zerg figurine. You aren\'t sure what a Zerg is, but looking at it makes you feel grossed out.',
        'desc': 'A disgusting basement filled with what looks to be one of the local families. Wait....what\'s that sound',
        'fight': 'boss'
    }
}

currentRoom = 'Inn'   # player start location

cls()  # start game with a fresh screen
showInstructions()     # show instructions to the player

while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()
    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('>')  # so long as the move does not
        # have a value. Ask the user for input

    # make everything lower case because directions and items require it, then split into a list
    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc'])
            cls()
            random_encounter()
            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")
    if move[0] == 'use':
        if move[1].lower() == 'estus' and 'estus' in inventory:
            print("You drink from the flask. Your health has been restored!")
            print("Your Estus Flask magically refills itself! Handy!")
            player_health = 20
        if move[1].lower() == 'zerg' and 'zerg' in inventory:
            print(
                "You pull out your plastic Zerg. You're not sure why but it grosses you out.")
            print("You lose 250 resources!")
        if move[1].lower() == 'tinypaladin' and 'tinypaladin' in inventory:
            print("You slap your pocket to get your Tiny Paladin's attention. He is ready to revive you at a moment's notice!")
        if move[1].lower() == 'keyring' and 'keyring' in inventory:
            print("You jingle your keyring. Almost immediately you hear howls in the distance. You think it would've been scarier with zombies for some reason.")
    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]  # add item to inv
            # msg saying you received the item
            print(move[1].capitalize() + ' received!')
            # deletes that item from the dictionary
            del rooms[currentRoom]['item']

        elif 'weapon' in rooms[currentRoom] and move[1] in rooms[currentRoom]['weapon']:
            inventory += [move[1]]  # add item to inv
            # msg saying you received the item
            print(move[1].capitalize() + ' received!')
            # deletes that item from the dictionary
            del rooms[currentRoom]['weapon']

        else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!')

    if move[0] == 'look':
        if 'desc' in rooms[currentRoom]:
            print(rooms[currentRoom]['desc'])  # print the look description
        else:
            print('You can\'t see anything.')

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes', 'Yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass
