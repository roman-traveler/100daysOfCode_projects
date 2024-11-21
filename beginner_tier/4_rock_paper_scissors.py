import random

rockpaperscissors = [
    """ 
           ______
       ___,  ____)
            (_____)
            (_____)
            (____)
       ---.__(__)
""",
    """
        _______
    ___'   ____)____
            _________)
           __________)
            ________)
    ---.___________)
    
    """,
    """
        _______
    ___'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    
    """,
]

player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
)
print(rockpaperscissors[player_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: \n {rockpaperscissors[computer_choice]}")

if computer_choice == player_choice:
    print("Tie")
elif (
    computer_choice == player_choice + 1 or computer_choice == 0 and player_choice == 2
):
    print("Computer wins; YOU LOSE")
else:
    print("You win!")
