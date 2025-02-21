participants = {}
finished = False
max_bid = -1
while finished is not True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    max_bid = max(bid, max_bid)
    participants[name] = bid
    status = input("Are there any other participants?\n Type yes or no\n")
    finished = status.lower() == "no"
    import os

    os.system("clear")

winners = [bidder for bidder in participants if participants[bidder] == max_bid]
if len(winners) == 1:
    print(f"The winner is {winners[0]} with a bid of {max_bid}")
else:
    print(
        f"No clear winner determined. Please do another round with the following participants: {winners}"
    )
