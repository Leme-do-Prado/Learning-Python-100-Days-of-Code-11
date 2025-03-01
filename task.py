import random

print("Welcome to the Blackjack program! This program is a simple Blackjack game between the computer and yourself.\n Let's start!")

cards = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "Joker": 10, "Queen": 10, "King": 10,
    "Ace": 11
}

player_bank=2000
dealer_bank=2000
dealer_hand = {}
player_hand = {}

def get_random_card(hand):
    sorted_card = random.choice(list(cards.keys()))
    hand[sorted_card] = cards.pop(sorted_card)

def show_hand(hand, player):
    if len(hand)>1:
        for key,value in hand.items():
            print(f"the {player}'s hand has a {key}, with the value of {value}!")
    else:
        key, value = next(iter(hand.items()))
        print(f"the {player}'s hand has a {key}, with the value of {value}!")

def calculate_score(hand):
    score = 0
    for key in hand:
        score+=hand[key]
    return score

bet = int(input("What's your bet?\n"))

while player_bank != 0:
    print("\nLET'S START!\n")
    get_random_card(dealer_hand)
    show_hand(dealer_hand, "dealer")
    get_random_card(dealer_hand)
    get_random_card(player_hand)
    get_random_card(player_hand)
    show_hand(player_hand, "player")
    print(f"Your score is {calculate_score(player_hand)}")
    player_choice = input("Do you wish to draw one more card?/\nType YES or NO\n")
    if player_choice=="YES":
        get_random_card(player_hand)
    if "Ace" in player_hand:
        player_hand["Ace"]=1
    if (calculate_score(dealer_hand) < calculate_score(player_hand) < 21):
            show_hand(dealer_hand, "dealer")
            print(f"DEALER TOTAL is {calculate_score(dealer_hand)}")
            show_hand(player_hand, "player")
            print(f"PLAYER TOTAL is {calculate_score(player_hand)}")
            print("Congratulations!\nYou have won!\n")
            player_bank += bet
            dealer_bank -= bet
    elif calculate_score(player_hand)==calculate_score(dealer_hand):
            show_hand(dealer_hand, "dealer")
            print(f"DEALER TOTAL is {calculate_score(dealer_hand)}")
            show_hand(player_hand, "player")
            print(f"PLAYER TOTAL is {calculate_score(player_hand)}")
            print("Close!\nIt was a draw!\n")
    else:
            show_hand(dealer_hand, "dealer")
            print(f"DEALER TOTAL is {calculate_score(dealer_hand)}")
            show_hand(player_hand, "player")
            print(f"PLAYER TOTAL is {calculate_score(player_hand)}")
            print("What a shame! You lose!\n")
            player_bank -= bet
            dealer_bank += bet

    print(f"You currently have {player_bank} in your bank.")
    bet = int(input("Do you wish to continue?\nIf so, what's your bet?\nType 0 if you wish to stop playing.\n"))
    dealer_hand = {}
    player_hand = {}

print("\n..........GAME OVER!")