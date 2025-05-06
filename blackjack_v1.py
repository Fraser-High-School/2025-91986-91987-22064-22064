import random
Cards = ["A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
         "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
         "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣",
         "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠"]
Removed_Cards = []
Player_Deck = []
Dealer_Deck = []
Chips = 1000
Player_Value = []
Dealer_Value = []

#function to give cards to players hand
def Player():
    
    #randomises the cards
    Player_Cards = random.choice(Cards)
    Cards.remove(Player_Cards)
    Removed_Cards.append(Player_Cards)
    if Player_Cards[:-1] == "J":
        Player_Deck.append(Player_Cards)
        Player_Value.append(10)
    if Player_Cards[:-1] == "Q":
        Player_Deck.append(Player_Cards)
        Player_Value.append(10)
    if Player_Cards[:-1] == "K":
        Player_Deck.append(Player_Cards)
        Player_Value.append(10)
    if Player_Cards[:-1] == "A":
        Player_Deck.append(Player_Cards)
    if Player_Cards[:-1] == "2" or Player_Cards[:-1] == "3" or Player_Cards[:-1] == "4" or Player_Cards[:-1] == "5" or Player_Cards[:-1] == "6" or Player_Cards[:-1] == "7" or Player_Cards[:-1] == "8" or Player_Cards[:-1] == "9" or Player_Cards[:-1] == "10":
        Player_Deck.append(Player_Cards)
        Player_Value.append(int(Player_Cards[:-1]))

#function to give cards to dealers hand
def Dealer():
    Dealer_Cards = random.choice(Cards)
    Cards.remove(Dealer_Cards)
    Removed_Cards.append(Dealer_Cards)
    if Dealer_Cards[:-1] == "J":
        Dealer_Deck.append(Dealer_Cards)
        Dealer_Value.append(10)
    if Dealer_Cards[:-1] == "Q":
        Dealer_Deck.append(Dealer_Cards)
        Dealer_Value.append(10)
    if Dealer_Cards[:-1] == "K":
        Dealer_Deck.append(Dealer_Cards)
        Dealer_Value.append(10)
    if Dealer_Cards[:-1] == "A":
        Dealer_Deck.append(Dealer_Cards)
    if Dealer_Cards[:-1] == "2" or Dealer_Cards[:-1] == "3" or Dealer_Cards[:-1] == "4" or Dealer_Cards[:-1] == "5" or Dealer_Cards[:-1] == "6" or Dealer_Cards[:-1] == "7" or Dealer_Cards[:-1] == "8" or Dealer_Cards[:-1] == "9" or Dealer_Cards[:-1] == "10":
        Dealer_Deck.append(Dealer_Cards)
        Dealer_Value.append(int(Dealer_Cards[:-1]))


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


print("===============================================================")
print("====================Welcome to Blackjack 21====================")
print("===============================================================\n")


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
    

while True:
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
        for card in range(2):
            Player()
            Dealer()
    else:
        print("Play again when you're ready")
        break


    while len(Dealer_Deck)<3:
        #current game progress
        print("=============================")
        print("Dealer hand -")
        print(f"{Dealer_Deck[0]} ██")
        print(Dealer_Value[0])
        print("=============================")
        print("Player hand -")
        print(*Player_Deck)
        print(sum(Player_Value))
        print("=============================")
        print("")
        break

    while True:
        if "A♥" in Player_Deck or "A♦" in Player_Deck or "A♣" in Player_Deck or "A♠" in Player_Deck:
            Ace = Ace_Value("Would you like the Ace to equal 1 or 11?\n")  
            if Ace == "11" and sum(Player_Value) >=11:
                print("Sorry you can't choose 11 because you will bust.")
            elif Ace == "11" and sum(Player_Value) <=10:
                Player_Value.append(11)
                break
            elif Ace == "1" and sum(Player_Value) <=20:
                Player_Value.append(1)
                break
            else:
                break

        if "A♥" in Dealer_Deck or "A♦" in Dealer_Deck or "A♣" in Dealer_Deck or "A♠" in Dealer_Deck:
            if sum(Dealer_Value) <=10:
                Dealer_Value.append(11)
                break
            elif sum(Dealer_Value) >=11:
                Dealer_Value.append(1)
                break

        
        if sum(Player_Value) == 21 and len(Player_Deck) == 2:
            print("Congratulations you got Blackjack")
            break

        
                
        if sum(Player_Value) < 21:
            Player_Move = Hit_Stand("Would you like to Hit or Stand?\n")
            if Player_Move == "hit":
                Player()
                print("=============================")
                print("Dealer hand -")
                print(f"{Dealer_Deck[0]} ██")
                print(f"{Dealer_Value[0]}")
                print("=============================")
                print("Player hand -")
                print(*Player_Deck)
                print(sum(Player_Value))
                print("=============================\n")

            elif Player_Move == "stand":
                while sum(Dealer_Value) <=16:
                    Dealer()
                    print("=============================")
                    print("Dealer hand -")
                    print(*Dealer_Deck)
                    print(sum(Dealer_Value))
                    print("=============================")
                    print("Player hand -")
                    print(*Player_Deck)
                    print(sum(Player_Value))
                    print("=============================\n")
                if sum(Dealer_Value) > sum(Player_Value) and sum(Dealer_Value) <=21:
                    print(f"You Lose!\nYou have ${Chips} remaining.")
                    
                if sum(Dealer_Value) >=21:
                    print(f"Dealer busted!\nYou Win!")
                    break

        if sum(Player_Value) == 21 and len(Player_Deck) >= 3:
            if sum(Dealer_Value) == sum(Player_Value):
                Chips = Chips + Bet
                print(f"It's a Tie!\nYou have ${Chips} remaining.")
        
        if sum(Dealer_Value) > sum(Player_Value) and sum(Dealer_Value) <=21:
            print(f"You Lose! The Dealer had a higher hand.\nYou have ${Chips} remaining.")

        if sum(Player_Value) > 21:
            print(f"You busted!\nYou have ${Chips} remaining.")
            break

        



        #elif sum(Player_Value)< 21:
            #continue
    #elif Player_Move == "stand":
        #print(*Player_Deck)
        #break




#if sum(Player_Value) > 21:
            #print(f"You Lose\nYour Hand value was {Player_Value}")
            #exit


#print(Player_Deck)










