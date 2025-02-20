hangman_array = [
    r"""
  ____
  |  |
     |
     |
     |
     |
---------
""",
    r"""
  ____
  |  |
  O  |
     |
     |
     |
---------
""",
    r"""
  ____
  |  |
  O  |
  |  |
     |
     |
---------
""",
    r"""
  ____
  |  |
  O  |
 /|  |
     |
     |
---------
""",
    r"""
  ____
  |  |
  O  |
 /|\ |
     |
     |
---------
""",
    r"""
  ____
  |  |
  O  |
 /|\ |
     |
     |
---------
""",
    r"""
  ____
  |  |
  O  |
 /|\ |
 /   |
     |
---------
""",
    r"""
  ____
  |  |
  O  |
 /|\ |
 / \ |
     |
---------
""",
][::-1]  # Displaying this way feels more natural, but I would rather have a count down

lives_remaining = 7
guessed_word = ""
word_to_find = "placeholder"
fail_guesses = []
correct_guesses = []
print(f"Word: {"_"*len(word_to_find)}")
print(hangman_array[lives_remaining])
while lives_remaining and guessed_word != word_to_find:
    guess = input("Type a letter\n")
    if len(guess) != 1:
        print("Invalid guess")
        continue
    if guess in fail_guesses or guess in correct_guesses:
        print("Choose a new letter; guess already made")
        continue
    if guess in word_to_find:
        print("Correct guess")
        correct_guesses.append(guess)
    else:
        print("Incorrect")
        fail_guesses.append(guess)
        lives_remaining -= 1
    print(f"Fail letters: {fail_guesses}")
    guessed_word = "".join(
        [letter if letter in correct_guesses else "_" for letter in word_to_find]
    )
    print(f"Word: {guessed_word}")
    print(hangman_array[lives_remaining])
if not lives_remaining:
    print("Game Over")
else:
    print("You won!")
