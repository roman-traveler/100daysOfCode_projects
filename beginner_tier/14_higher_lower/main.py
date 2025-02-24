print("Welcome to higher or lower")
values = {"Neymar": ,
          "Kardashian":,
          "Rihanna":,
          "Shakira":}
# look for the game data file

score=0
correct = True
while correct:
    comparison_a=random.choice(values)
    comparison_b=comparison_a
    while comparison_b == comparison_a:
        comparison_b=random.choice(values)
    guess = input("a or b")
    
    ""
    
print("Your score is {score}")
