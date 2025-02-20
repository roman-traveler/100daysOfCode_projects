from urllib.request import Request, urlopen
import random

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

# Pick random word
url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})

web_byte = urlopen(req).read()

webpage = web_byte.decode("utf-8")
word_to_find = random.choice(webpage.split("\n"))

# Initialize
lives_remaining = 7
guessed_word = ""
fail_guesses = []
correct_guesses = []
print(f"Word: {"_"*len(word_to_find)}")
print(hangman_array[lives_remaining])

# Guessing loop
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

# Evaluate win condition
print(f"The word was: {word_to_find.capitalize()}")
if not lives_remaining:
    print("Game Over")
else:
    print(f"You won! You still had {lives_remaining} lives")
