import random
Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Suits = ["♥", "♦", "♣", "♠"]
Player_Deck = []
Dealer_Deck = []
Chips = 1000
Player_Value = []
Dealer_Value = []

#function to give cards to players hand
def Player():
    
    #randomises the cards
    Player_Cards = random.choice(Cards)
    if Player_Cards == 11:
        Card_Suit = "J" +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
        Player_Value.append(10)
    if Player_Cards == 12:
        Card_Suit = "Q" +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
        Player_Value.append(10)
    if Player_Cards == 13:
        Card_Suit = "K" +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
        Player_Value.append(10)
    if Player_Cards == 1:
        Card_Suit = "A" +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
    if Player_Cards >= 2 and Player_Cards <= 10:
        Card_Suit = str(Player_Cards) +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
        Player_Value.append(Player_Cards)

#function to give cards to dealers hand
def Dealer():
    Dealer_Cards = random.choice(Cards)
    if Dealer_Cards == 11:
        Card_Suit = "J" +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
        Dealer_Value.append(Dealer_Cards)
    if Dealer_Cards == 12:
        Card_Suit = "Q" +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
        Dealer_Value.append(Dealer_Cards)
    if Dealer_Cards == 13:
        Card_Suit = "K" +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
        Dealer_Value.append(Dealer_Cards)
    if Dealer_Cards == 1:
        Card_Suit = "A" +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
    if Dealer_Cards >= 2 and Dealer_Cards <= 10:
        Card_Suit = str(Dealer_Cards) +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
        Dealer_Value.append(Dealer_Cards)

#function to check if user enters yes (y) or no (n)
def Yes_No(question):
    
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

#function to check if user enters hit (h) or stand (s)
def Hit_Stand(question):

    while True:
        response = input(question).lower()

        if response == "hit" or response == "h":
            return "hit"
        elif response == "stand" or response == "s":
            return "stand"
        else:
            print("Please enter hit (h) or stand (s).\n")

#function to check if user enters 1 or 11 for the Ace
def Ace_Value(question):

    while True:
        response = input(question).lower()

        if response == "11":
            return "11"
        elif response == "1":
            return "1"
        else:
            print("Please enter 1 or 11.\n")


#while True loop to endlessly make sure there aren't duplicates
while True:
    #gives the player 2 cards that aren't duplicates
    while len(Player_Deck)<2:
        Player()
        Player_Deck = list(set(Player_Deck))
        continue
    #gives the dealer 2 cards that aren't duplicates
    while len(Dealer_Deck)<2:
        Dealer()
        Dealer_Deck = list(set(Dealer_Deck))
        continue
    
    #if True there is a duplicate in both hands
    Deck = bool(set(Player_Deck) & set(Dealer_Deck))

    #clears cards in dealers hand and give them another 2 and repeats until there isn't any duplicates
    if Deck == True:
        Dealer_Deck.clear()
    #breaks the loop since there aren't any duplicate cards
    elif Deck == False:
        break


print("===============================================================")
print("====================Welcome to Blackjack 21====================")
print("===============================================================")
print("")



Instructions = Yes_No("Would you like to know the rules of Blackjack 21?\n")
if Instructions == "yes":
    print("")
    print("=============================Rules=============================")
    print("Goal: Get closer to 21 than the dealer without going over.")
    print("")
    print("Cards:")
    print(" - Ace = 1 or 11")
    print(" - Face cards = 10")
    print(" - Others = face value")
    print("")
    print("Your Turn:")
    print(" - Hit = Take another card")
    print(" - Stand = Keep your hand")
    print("")
    print("Win if:")
    print(" - Your total > dealer's (without busting)")
    print(" - Dealer busts")
    print(" - Blackjack (Ace + 10) = instand 3:2 payout (unless dealer also has it)")
    print("")
    print("Lose if:")
    print(" - You bust (go over 21)")
    print(" - Dealer's total > yours")
    print("===============================================================")
    print("")

elif Instructions == "no":
    print("")
    
#ask user if they are ready to start
Start = Yes_No("Are you ready to start?\n")
if Start == "yes":
    #gets players bet
    print("")
    print(f"You have ${Chips} in Chips")
    Bet = int(input("How much would you like to bet?\n"))

    Chips = Chips - Bet
    print("")
    print(f"You bet ${Bet}")
    print(f"Remaining Chips are ${Chips}")
else:
    print("Play again when you're ready")
    exit()


#current game progress
print("=============================")
print("Dealer hand -")
print(f"{Dealer_Deck[0]} ██")
print("=============================")
print("Player hand -")
print(*Player_Deck)
print("=============================")
print("")



while "A♥" in Player_Deck or "A♦" in Player_Deck or "A♣" in Player_Deck or "A♠" in Player_Deck:
    Ace = Ace_Value("Would you like the Ace to equal 1 or 11?\n")
    if Ace == "11":
        Player_Value.append(11)
        break
    elif Ace == "1":
        Player_Value.append(1)
        break

while True:
    if sum(Player_Value) < 21:
        break
    elif Player_Value[0] + Player_Value[1] == 21:
        print("Congratulations you got Blackjack")
        


while True:
    while len(Player_Deck)<3:
        Player_Move = Hit_Stand("Would you like to Hit or Stand?\n")
        if Player_Move == "hit":
            Player()
            print(*Player_Deck)
            if sum(Player_Value) > 21:
                print(f"You Lose\nYour Hand value was {Player_Value}")
                exit
            elif sum(Player_Value)< 21:
                continue
        elif Player_Move == "stand":
            print(*Player_Deck)
            break
    if Player_Move == "stand":
        break
    elif Player_Move == "hit":
        continue

    while len(Player_Deck)<4:
        Player_Move = Hit_Stand("Would you like to Hit or Stand?\n")
        if Player_Move == "hit":
            Player()
            print(*Player_Deck)
            if sum(Player_Value) > 21:
                print(f"You Lose\nYour Hand value was {Player_Value}")
                exit
        elif Player_Move == "stand":
            print(*Player_Deck)
            break
    if Player_Move == "stand":
        break



print(Player_Deck)










