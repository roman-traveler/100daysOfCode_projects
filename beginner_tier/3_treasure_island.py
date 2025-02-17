treasure_ascii = '''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
while True:
    import os
    clear = lambda: os.system('clear')
    clear()
    print(treasure_ascii)
    print("Welcome to Treasure Island.")
    print("Your mention is to find the treasure.")
    print("You're at a crossroads. Where do you want to go?")
    first_choice=input("Type Left or Right\n")
    if first_choice.lower() != "left":
        input("You got eaten by a grue. Game Over")
        continue
    print("You are at an island. Do you want to swim or wait for a boat?")
    second_choice=input("Type Swim or Wait\n")
    if second_choice.lower() != "wait":
        input("You drowned. Game Over")
        continue
    third_choice=input("Type Red, Blue or Green\n")
    if third_choice.lower() != "blue":
        print("The door exploded in your face. Game Over")
    else:
        print("You found the treasure!")