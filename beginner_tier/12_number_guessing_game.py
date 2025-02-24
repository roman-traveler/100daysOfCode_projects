import random

difficulties = {"easy": 10, "hard": 5}

number = random.choice(range(1, 100))
guess = -1

print("Welcome to the number guessing game!")
print("I think of the number between 1 and 100")

difficulty = input("Choose a difficulty. Type easy or hard\n")

for attempt in range(difficulties[difficulty]):
    print(
        f"You have {difficulties[difficulty] - attempt} guess{"es" if attempt!=difficulties[difficulty]-1 else ""} remaining"
    )
    guess = int(input("Type a number between 1 and 100\n"))

    if guess == number:
        print("You won! That was indeed the number")
        break
    else:
        print(f"Your guess was {"lower" if guess<number else "higher"} than my number.")

else:
    print(f"My number was {number}")
    print("Out of tries. Game over")
