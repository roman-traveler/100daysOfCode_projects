import random
import os

ranks = list(range(1, 11)) + ["J", "Q", "K"]

deck = ranks * 4
value = {rank: 10 if str(rank) in "JQK" else rank for rank in ranks}


def pick_a_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


def handle_ace(hand, score):
    """Make maximum not bust ace score"""
    for card in hand:
        if card == 1:
            if score <= 11:
                score += 10
    return score


def score(hand):
    """Get score, than handle ace special case."""
    score = sum([value[card] for card in hand])
    score = handle_ace(hand, score)
    return score


def reveal_dealer_hand(hand):
    while score(hand) < 17:
        hand = hand + [pick_a_card(deck)]
    print(f"dealer cards: {hand}")
    print(f"dealer score: {score(hand)}")
    return hand


def main_loop():
    done = False
    player_cards = [pick_a_card(deck), pick_a_card(deck)]
    dealer_cards = [pick_a_card(deck), pick_a_card(deck)]
    while not done and score(player_cards) <= 21:
        print(f"Player score: {score(player_cards)}")
        print(f"Player cards: {player_cards}")
        print(f"Dealer cards: {dealer_cards[0]}, Unknown card")
        new_card = input("Draw another card? Type y to draw a card; Type n to stop\n")
        if new_card != "y":
            done = True
            continue
        player_cards += [pick_a_card(deck)]
    if score(player_cards) > 21:
        print(f"Player cards: {player_cards}")
        print(f"Player score: { score(player_cards)}")
        print("Player went Bust; Game over")
    else:
        dealer_cards = reveal_dealer_hand(dealer_cards)
        if score(dealer_cards) > 21:
            print("Dealer went Bust; Player Won!")
        elif score(player_cards) > score(dealer_cards):
            print("Player Won!")
        elif score(dealer_cards) > score(player_cards):
            print("House won; Game Over")
        else:
            print("This is a tie")

    input("Type anything to continue\n")

    os.system("clear")


while True:
    main_loop()
