##Sample code snippet for multidimensional lists


##This is a two dimensional list which is a way of saying a list that contains other lists.

#!/usr/bin/python3

dungeon=[                     # Start list of floors
         ['a','b','c','d'],     # 1st floor room contents
         ['1','2','3','4'],     # 2nd floor room contents
         ['@','#','$','*'],     # 3rd floor room contents
        ]                     # end list of floors

floor= 2                      # Index for floors
room = 1                      # Index for rooms

# Accessing the information in a “room” is done by specifying
# both the floor and room indexes of the multidimensional list

# This will print the hash (#) mark
print("Room "+str(room)+", floor "+str(floor)+" contains "+dungeon[floor][room]);

# Using the for loop (discussed in unit 4) and the len function
# we can print a multidimensional list in nested for loops

for floor in range(len(dungeon)):                   # len will return # of floors
    for room in range(len(dungeon[floor])):         # len will return # of rooms
        print(" "+dungeon[floor][room]+" ", end='') # <- does not print newline
    print("")                                       # print newline between floors
