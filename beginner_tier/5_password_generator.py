import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

numbers = [str(number) for number in range(10)]
letters = [letter for letter in alphabet] + [letter.upper() for letter in alphabet]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print("Welcome to the PyPassword Generator!")

length = int(input("What length do you want your password to be?"))
symbol_count = int(input("How many non-alphanum symbols do you want?"))
number_count = int(input("How many numbers do you want?"))
password = ""
assert length >= symbol_count + number_count
for _ in range(number_count):
    password = password + random.choice(numbers)
for _ in range(symbol_count):
    password = password + random.choice(symbols)
for _ in range(length - symbol_count - number_count):
    password = password + random.choice(letters)
password = list(password)
random.shuffle(password)
password = "".join(password)
print(f"Your password is {password}")
