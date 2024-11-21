print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip_size = int(input("How much tip would you like to give? 10, 12, 15, 20? "))
people = int(input("How may people to split the bill? "))

bill_with_tip = bill * (100 + tip_size) / 100
bill_per_person = bill_with_tip / people

print(f"Each person should pay {round(bill_per_person, 2)} $")
