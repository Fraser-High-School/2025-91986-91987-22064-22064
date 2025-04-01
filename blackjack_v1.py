import random
Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Suits = ["♥", "♦", "♣", "♠"]
Player_Deck = []
Dealer_Deck = []

#function to give cards to players hand
def Player():
    
    #randomises the cards
    Player_Cards = random.choice(Cards)
    if Player_Cards == 11:
        Card_Suit = "J" +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
    if Player_Cards == 12:
        Card_Suit = "Q" +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
    if Player_Cards == 13:
        Card_Suit = "K" +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
    if Player_Cards == 1:
        Card_Suit = "A" +  random.choice(Suits)
        Player_Deck.append(Card_Suit)
    if Player_Cards >= 2 and Player_Cards <= 10:
        Card_Suit = str(Player_Cards) +  random.choice(Suits)
        Player_Deck.append(Card_Suit)

#function to give cards to dealers hand
def Dealer():
    Dealer_Cards = random.choice(Cards)
    if Dealer_Cards == 11:
        Card_Suit = "J" +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
    if Dealer_Cards == 12:
        Card_Suit = "Q" +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
    if Dealer_Cards == 13:
        Card_Suit = "K" +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
    if Dealer_Cards == 1:
        Card_Suit = "A" +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)
    if Dealer_Cards >= 2 and Dealer_Cards <= 10:
        Card_Suit = str(Dealer_Cards) +  random.choice(Suits)
        Dealer_Deck.append(Card_Suit)


#check for any duplicates
while len(Player_Deck)<2:
    Player()
    Player_Deck = list(set(Player_Deck))

#check for any duplicates
while len(Dealer_Deck)<2:
    Dealer()
    Dealer_Deck = list(set(Dealer_Deck))

if set(Dealer_Deck) == set(Player_Deck):
    Dealer()
else:
    print(*Dealer_Deck)
    print(*Player_Deck)








