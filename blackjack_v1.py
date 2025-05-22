"""This is a recreation of Blackjack 21."""
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
Ace = []
Win = []
Loss = []


def Player():
    """Gathers cards and values for player hand."""
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
        Ace.append(Player_Cards)
    if Player_Cards[:-1] == "2" or Player_Cards[:-1] == "3" or Player_Cards[:-1] == "4" or Player_Cards[:-1] == "5" or Player_Cards[:-1] == "6" or Player_Cards[:-1] == "7" or Player_Cards[:-1] == "8" or Player_Cards[:-1] == "9" or Player_Cards[:-1] == "10":
        Player_Deck.append(Player_Cards)
        Player_Value.append(int(Player_Cards[:-1]))


def Dealer():
    """Gathers cards and values for dealer hand."""
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
        Ace.append(Dealer_Cards)
    if Dealer_Cards[:-1] == "2" or Dealer_Cards[:-1] == "3" or Dealer_Cards[:-1] == "4" or Dealer_Cards[:-1] == "5" or Dealer_Cards[:-1] == "6" or Dealer_Cards[:-1] == "7" or Dealer_Cards[:-1] == "8" or Dealer_Cards[:-1] == "9" or Dealer_Cards[:-1] == "10":
        Dealer_Deck.append(Dealer_Cards)
        Dealer_Value.append(int(Dealer_Cards[:-1]))


def Yes_No(question):
    """Corrects any other responses apart from yes(y) or no(n)."""
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")


def Hit_Stand(question):
    """Corrects any other responses apart from hit(h) or stand(s)."""
    while True:
        response = input(question).lower()

        if response == "hit" or response == "h":
            return "hit"
        elif response == "stand" or response == "s":
            return "stand"
        else:
            print("Please enter hit (h) or stand (s).\n")


def Ace_Value(question):
    """Corrects any other responses apart from 11 or 1."""
    while True:
        response = input(question).lower()

        if response == "11":
            return "11"
        elif response == "1":
            return "1"
        else:
            print("Please enter 1 or 11.\n")


def Restart():
    """Restarts the Player and Dealer hands and values."""
    Player_Deck.clear()
    Dealer_Deck.clear()
    Player_Value.clear()
    Dealer_Value.clear()

    for cards in range(len(Removed_Cards)):
        Cards.insert(0, Removed_Cards[0])
        Removed_Cards.remove(Removed_Cards[0])


def Bet_Amount(question):
    """Corrects any other values apart from ones the player can bet."""
    while True:

        try:
            response = int(input(question))
            if response <= Chips:
                return response
            elif response >= Chips:
                print("You don't have that much chips.\n")
        except(ValueError):
            print("Please enter a valid number.\n")


print("===============================================================")
print("====================Welcome to Blackjack 21====================")
print("===============================================================\n")

# asks user if they want instructions
Instructions = Yes_No("Would you like to know the rules of Blackjack 21?\n")
# if answer = yes the game prints instructions
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

# if answer = no the game doesn't print instructions
elif Instructions == "no":
    print("")

# while true to loop the entire game
while True:
    # ask user if they are ready to start
    Start = Yes_No("Are you ready to start?\n")

    # if answer = yes the game will start
    if Start == "yes":
        # gets players bet
        print("")
        print(f"You have ${Chips} in Chips")
        Bet = Bet_Amount("How much would you like to bet?\n")

        # gets the chip amount
        Chips = Chips - Bet
        print("")
        print(f"You bet ${Bet}")
        print(f"Remaining Chips are ${Chips}")
        # gives the dealer and player 2 cards to start
        for card in range(2):
            Player()
            Dealer()
    else:
        print("Play again when you're ready")
        break

    # current game progress
    while len(Dealer_Deck) < 3:
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

    # while true to loop the current game
    while True:
        # while loop and seperate ace list to continue asking what the ace will equal if it is in player deck
        while "A♥" in Ace or "A♦" in Ace or "A♣" in Ace or "A♠" in Ace:
            # removes ace after being used
            Ace.remove(Ace[0])
            # if statement for player with ace
            if "A♥" in Player_Deck or "A♦" in Player_Deck or "A♣" in Player_Deck or "A♠" in Player_Deck:

                # ask user what they want the ace to equal
                Ace_Card = Ace_Value("Would you like the Ace to equal 1 or 11? \n")
                # if player value is equal to or over 11 it will not let player choose 11 because they will bust
                if Ace_Card == "11" and sum(Player_Value) >= 11:
                    print("Sorry you can't choose 11 because you will bust.")
                    Player_Value.append(1)
                    print("=============================")
                    print("Dealer hand -")
                    print(f"{Dealer_Deck[0]} ██")
                    print(f"{Dealer_Value[0]}")
                    print("=============================")
                    print("Player hand -")
                    print(*Player_Deck)
                    print(sum(Player_Value))
                    print("=============================\n")
                # if input is 11 and player value less than or equal to 10 it will append 11
                elif Ace_Card == "11" and sum(Player_Value) <= 10:
                    Player_Value.append(11)
                    print("=============================")
                    print("Dealer hand -")
                    print(f"{Dealer_Deck[0]} ██")
                    print(f"{Dealer_Value[0]}")
                    print("=============================")
                    print("Player hand -")
                    print(*Player_Deck)
                    print(sum(Player_Value))
                    print("=============================\n")
                    break
                # if input is 1 and player value less than or equal to 20 it will append 1
                elif Ace_Card == "1" and sum(Player_Value) <= 20:
                    Player_Value.append(1)
                    print("=============================")
                    print("Dealer hand -")
                    print(f"{Dealer_Deck[0]} ██")
                    print(f"{Dealer_Value[0]}")
                    print("=============================")
                    print("Player hand -")
                    print(*Player_Deck)
                    print(sum(Player_Value))
                    print("=============================\n")
                    break
                else:
                    print("Sorry you must enter 1 or 11.")

            # if statement for dealer with ace
            if "A♥" in Dealer_Deck or "A♦" in Dealer_Deck or "A♣" in Dealer_Deck or "A♠" in Dealer_Deck:
                if sum(Dealer_Value) <= 10:
                    Dealer_Value.append(11)
                    break
                elif sum(Dealer_Value) >= 11:
                    Dealer_Value.append(1)
                    break

        # checks for blackjack
        if sum(Player_Value) == 21 and len(Player_Deck) == 2:
            Chips = Chips + Bet + Bet*1.5
            print("Congratulations you got Blackjack")
            Win.append(1)
            Restart()
            break

        # checks is player doesn't bust
        if sum(Player_Value) < 21:
            # ask user to hit or stand
            Player_Move = Hit_Stand("Would you like to Hit or Stand?\n")
            # if player hit it will add another card
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
            # if player stand it will move on to dealer value
            elif Player_Move == "stand" or sum(Player_Value) == 21:
                # while dealer value less than or equal to 16 it will add another card to dealer
                while sum(Dealer_Value) <= 16:
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
                # if dealer value greater than 16 it will show the second dealer card
                if sum(Dealer_Value) > 16 and len(Dealer_Deck) == 2:
                    print("=============================")
                    print("Dealer hand -")
                    print(*Dealer_Deck)
                    print(sum(Dealer_Value))
                    print("=============================")
                    print("Player hand -")
                    print(*Player_Deck)
                    print(sum(Player_Value))
                    print("=============================\n")
                # if player greater than dealer while player not busting the player wins
                if sum(Player_Value) > sum(Dealer_Value) and sum(Player_Value) <= 21:
                    Chips = Chips + Bet*2
                    print(f"You Win!\nThe Player had a higher hand.\nYou have ${Chips} remaining.")
                    Win.append(1)
                    Restart()
                # if dealer busts the player wins
                if sum(Dealer_Value) > 21:
                    Chips = Chips + Bet*2
                    print(f"Dealer busted!\nYou Win!\nYou have ${Chips} remaining.")
                    Win.append(1)
                    Restart()
                    break
                # if dealer and player equal each other its a tie
                if sum(Dealer_Value) == sum(Player_Value):
                    Chips = Chips + Bet
                    print(f"It's a Tie!\nYou have ${Chips} remaining.")
                    Restart()
                    break
                # if dealer greater than player while dealer not busting the dealer wins 
                if sum(Dealer_Value) > sum(Player_Value) and sum(Dealer_Value) <= 21:
                    print(f"You Lose!\nThe Dealer had a higher hand.\nYou have ${Chips} remaining.")
                    Loss.append(1)
                    Restart()
                    break
                # if player = 21 and dealer doesn't = player the player wins
                if sum(Player_Value) == 21 and len(Player_Deck) >= 3 and sum(Dealer_Value) != sum(Player_Value):
                    Chips = Chips + Bet*2
                    print(f"You Win!\nThe Player had a higher hand.\nYou have ${Chips} remaining.")
                    Win.append(1)
                    Restart()
                # if player = 21 and dealer does = player it's a tie
                if sum(Player_Value) == 21 and len(Player_Deck) >= 3 and sum(Dealer_Value) == sum(Player_Value):
                    Chips = Chips + Bet
                    print(f"It's a Tie!\nYou have ${Chips} remaining.")
                    Restart()
                    break
        # checks if player busts
        elif sum(Player_Value) > 21:
                print(f"You busted!\nYou have ${Chips} remaining.")
                Loss.append(1)
                Restart()
                break
    # if user runs out of chips the game will end
    if Chips == 0:
        print("Well Done!\nYou have lost all your chips by gambling.\n")
        print(f"Wins - {Win}, Losses - {Loss}")
        exit()
    print(f"Wins - {sum(Win)}, Losses - {sum(Loss)}")
