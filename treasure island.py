print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')
print('Welcome to Treasure Island. Your mission is to find the treasure.')
direction = input("Do you want to go left or right? Type 'left' or 'right'\n").lower()
if direction != 'left':
    print('Fall into a hole. Game over.')
else:
    swim_or_wait = input("You've come to a lake. Do you want to swim or do you want to wait for a boat? Type 'swim' or 'wait'.\n").lower()
    if swim_or_wait != 'wait':
        print('Attacked by trout. Game over.')
    else:
        which_door = input('You arrive at the Island unharmed. There is a house with three doors, one red, one yellow, one blue. Which color do you choose?\n').lower()
        if which_door == 'red':
            print('You were burned by fire. Game over.')
        elif which_door == 'blue':
            print('You were eaten by beasts. Game over.')
        elif which_door == 'yellow':
            print('You found the treasure! You Win!')
        else:
            print("You chose a door that doesn't exist. Game over.")
