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


while len(Player_Deck)<2:
    Player()
    Player_Deck = list(set(Player_Deck))
    
    
        
        

    
print(*Player_Deck)





