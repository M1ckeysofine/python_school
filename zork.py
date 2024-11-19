#! /usr/bin/python3
import random


playerItems = [] #The players pocket fills and empties as items are added and removed
playerFloor = 0 #Variable to track the floor a player is on
allowedCommands = ["right", "left", "straight", "climb", "fight", "flee", "help", "instructions", "inventory", “grab”, “open”,”leave”] # just using this to track permitted commands

initialObstacles = [\
['a sword', 'a monster', 'a sword'],\
['a monster', 'a sword', 'a monster'],\
['a sword', 'magic crystals', 'boss monster']\
] #Each nested list is a floor

floorObstacles = [[],[],[]] #Just for fun, randomize location of items so game has some variety
for i in range(3): #this is a “for” loop. “i” is a temp variable and “range(3)” means loop 3 times
    floorObstacles[i] = random.sample(initialObstacles[i], len(initialObstacles[i]))

isAlive = True #Tracking life status
gameWon = False #Tracking if the game was won

#Initial Game Greeting
print('Welcome to the maze!\n Your mission is to locate the treasure chest.')
print('Every room has a staircase that goes further into the maze')
print('Beware there are monsters running free in the maze')
print('they can be defeated with a sword.')
print('Be aware a massive monster has been reported in the area.\
Magic Crystals will help')

#Main Game Loop
while isAlive and not gameWon:
    command = input(' What would you like to do?\n You are ' + str(playerFloor) + ' floors below ground\n')
    if command == 'help' or command == 'instructions':
        print('You can type: \n right \n left \n straight \n climb \n grab \n fight \n inventory')
    elif command == 'right':
        obstacle = floorObstacles[playerFloor][0]
        index = 0
        print('you take the door to the right and find ' + obstacle)
        if obstacle == 'a monster' or obstacle == 'boss monster':
            fightCommand = input('You have encountered a monster would you like to: \n fight or flee?')
            if fightCommand == 'flee':
                diceRoll = random.choice(['live', 'die'])
                if diceRoll == 'live':
                    print('You survived now go find a sword and come back to fight another day')
                else:
                    print("You weren't quiet enough; the monster has defeated you")
                    isAlive = False
            elif fightCommand == 'fight':
                command = 'fight'

    elif command == 'left':
        obstacle = floorObstacles[playerFloor][1]
        index = 1
        print('you take the door to the left and find ' + obstacle)
        if obstacle == 'a monster' or obstacle == 'boss monster':
            fightCommand = input('You have encountered a monster would you like to: \n fight or flee?')
            if fightCommand =='flee':
                diceRoll = random.choice(['live', 'die'])
                if diceRoll == 'live':
                    print('You survived now go find a sword and come back to fight another day')
                else:
                    print("You weren't quiet enough; the monster has defeated you")
                    isAlive = False
            elif fightCommand == 'fight':
                command = 'fight'

    elif command == 'straight':
        obstacle = floorObstacles[playerFloor][2]
        index = 2
        print('you take the door in front of you and find ' + obstacle)
        if obstacle == 'a monster' or obstacle == 'boss monster':
            fightCommand = input('You have encountered a monster would you like to: \n fight or flee?')
            if fightCommand == 'flee':
                diceRoll = random.choice(['live', 'die'])
                if diceRoll == 'live':
                    print('You survived now go find a sword and come back to fight another day')
                else:
                    print("You weren't quiet enough; the monster has defeated you")
                    isAlive = False
            elif fightCommand == 'fight':
                command = 'fight'

    elif command == 'grab':
        if obstacle == 'a sword' or obstacle == 'magic crystals':
            playerItems.append(obstacle)
            print(floorObstacles[playerFloor][index] + ' added to inventory')
            floorObstacles[playerFloor][index] = 'nothing'
        else:
            print('There is nothing to grab')
    elif command == 'inventory':
        if len(playerItems) > 0:
            print('\n-------------\n')
            for item in playerItems:
                print('| '  + item )
            print('\n-------------\n')
        else:
            print('\n-------------\n')
            print('Inventory Empty')
            print('\n-------------\n')
    elif command == 'climb':
        playerFloor = playerFloor + 1
        print('You climb down stairs')
    if command == 'fight':
        if obstacle == 'a monster' or obstacle =='boss monster':
            if obstacle == 'a monster' and 'a sword' in playerItems:
                print('you have defeated ' + obstacle)
                floorObstacles[playerFloor][index] = 'nothing'
                playerItems.remove('a sword')
            elif obstacle == 'boss monster' and 'a sword' in playerItems and 'magic crystals' in playerItems:
                print('you have defeated ' + obstacle)
                print('As the slain boss falls to the ground you see a treasure chest')
                command = input('The chest has a skull and crossbones symbol, would you like to open it or leave it for another adventurer\n choose open or leave?')
                if command == 'open':
                    print('As you open the chest a gas is emitted slowly suffocating you. You have died')
                    isAlive = False
                elif command == 'leave':
                    print("""Wise choice as you walk out of the room you encounter
                    a princess, she is so very appreciative of your efforts and rewards you
                    with the true treasure and a portal gun""")
                    gameWon = True
                else:
                    print("That wasn't a choice. You die")
                    isAlive = False
            else:
                print('you got got')
                isAlive = False
        else:
            print('There is nothing here to fight, settle down spazzy')
    if command not in allowedCommands:
        print("I don't understand that command\n")
if not isAlive and not gameWon:
    print('You Lose')

if isAlive and gameWon:
    print('You Win, The Cake is a Lie!')
