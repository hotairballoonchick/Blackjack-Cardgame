# Amy Cannon
# CS1400 - 001
# Assignment 7

#import stuff
from time import sleep
from deck import Deck
from card import Card

#Define Main function
def main():
    print("Welcome to Blackjack!")

    players = []
    hand = []
    playerNum = eval(input("How many players (1-5)? "))
    #dealer is the first player in list
    players.append([])
    hand.append([])
    #adding players to list and adding money to player's accounts
    for i in range(1, playerNum + 1):
        players.append([])
        players[i].append(100)
        #starting bet is zero. Two-dimensional list
        players[i].append(0)
        #make hand
        hand.append([])
        players[i].append(str(input("Enter Player" + str(i) + "'s name: " ).title()))

    #Begin game
    game = True
    while game:
        deck = Deck()
        #Deal hand
        deal(hand, deck)

        #Start bets
        for i in range(1, playerNum +1):
            print()
            #If they have no money left
            if players[i][0] == 0:
                print("Sorry, " + str(players[i][2]) + " you are out of money and cannot play.")
                continue
            #Player needs to see the dealer's second card and their own balance
            print("The second card of the dealer is: " + str(hand[0][0]) + "\n"
             + str(players[i][2]) + "'s Account balance: $" + str(players[i][0]))
            #If they have less than 5 money set account to bet amount
            if players[i][0] < 5:
                players[i][0] = players[i][1]
                print("You have less than the minimum bet in your account. Your bet amount was: " + str(players[i][1]))
            #Asking for player's bet
            else:
                betAmount = eval(input("How much do you want to bet?(The minimum bet is $5): "))
                #Checking whether or not Player's input is valid
                while betAmount < 5 or betAmount > players[i][0]:
                    print("The minimum bet is $5 and the maximum bet is " + str(players[i][0]) + ".")
                    betAmount = eval(input("How much do you want to bet?: "))
                players[i][1] = betAmount

        #Start playing the game
        for i in range(1, playerNum + 1):
            print()
            # If they have no money left
            if players[i][0] == 0:
                print("Sorry, " + str(players[i][2]) + " you are out of money and cannot play.")
                continue
        for i in range(1, playerNum +1):
            print()
            print("It is " + str(players[i][2]) + "'s turn.")
            #show player's hand
            print("Cards in your hand: " + str(hand[i]))
            #Hit or hold menu
            keepGoing = True
            while keepGoing == True:
                hitOrHold = eval(input("Would you like to: \n (1) Hit \n or \n (2) Hold"))
                if hitOrHold == 1:
                    hand[i].append(deck.draw())
                    print("Cards in your hand: " + str(hand[i]))
                    if bust(hand[i]):
                        keepGoing = False
                        print("You bust!")
                else:
                    keepGoing = False
                    print(str(players[i][2]) + " holds.")

        #Dealer's turn
        print()
        dealerPlay = True
        while dealerPlay == True:
            #Dealer playing
            if handValue(hand[0]) <= 17:
                print("Dealer's hand: " + str(hand[0]))
                print("Dealer hits!")
                sleep(1)
                hand[0].append(deck.draw())
            #If dealer busts
            elif bust(hand[0]):
                print("Dealer's hand: " + str(hand[0]))
                print("Dealer busted!")
                dealerPlay = False
            else:
                print("Dealer's hand: " + str(hand[0]))
                dealerPlay = False
                print("Dealer holds")

        #Who won? Where oh where does the money go?
        for i in range(1, playerNum + 1):
            print()
            # If they have no money left
            if players[i][0] == 0:
                continue
            #Case if the dealer loses
            if bust(hand[0]):
                if bust(hand[i]):
                    players[i][0] -= players[i][1]
                    print(str(players[i][2]) + "'s account: $" + str(players[i][0]))
                else:
                    players[i][0] += players[i][1]
                    print(str(players[i][2]) + "'s account: $" + str(players[i][0]))
            #Case if player busts
            elif bust(hand[i]):
                players[i][0] -= players[i][1]
                print(str(players[i][2]) + "Too bad. You lose.")
                print(str(players[i][2]) + "'s account: $" + str(players[i][0]))
            #Oh dang it's a tie
            elif handValue(hand[0]) == handValue(hand[i]):
                print("It was a tie.")
                print(str(players[i][2]) + "'s account: $" + str(players[i][0]))
                continue
            #Player beats the dealer
            elif handValue(hand[0]) < handValue(hand[i]):
                print("You win! Winner winner chicken dinner!")
                players[i][0] += players[i][1]
                print(str(players[i][2]) + "'s account: $" + str(players[i][0]))
            #Player loses to dealer
            elif handValue(hand[0]) > handValue(hand[i]):
                print("You lost. Maybe next time.")
                players[i][0] -= players[i][1]
                print(str(players[i][2]) + "'s account: $" + str(players[i][0]))

        #Play again?
        print()
        playAgain = eval(input("Would you like to play again?: \n (1) Heck yeah! \n or \n (2) Naw, I'm good."))
        if playAgain == 1:
            hand = []
            for i in hand:
                hand[i].append(deck.draw())
        else:
            print("\nThank you for playing.")
            sortMoneyAmounts(players)
            game = False

#Deal a hand
def deal(hand, deck):
    for i in range(len(hand)):
        hand[i].append(deck.draw())
        hand[i].append(deck.draw())
#Define a bust
def bust(hand):
    if handValue(hand) >= 22:
        return True
    else:
        return False

def handValue(hand):
    value = 0
    aces = 0
    #for aces
    for i in range(0,len(hand)):
        if hand[i].getCardValue() == 1:
            aces += 1
        #for non royalty
        elif hand[i].getCardValue() <= 10:
            value += hand[i].getCardValue()
        #for royalty
        else:
            value += 10
    #What on earth is the ace going to be?
    if aces >= 1:
        value += aces
        if value <= 11:
            value += 10
            return value
        else:
            return value
    else:
        return value
#bubble sort
def sortMoneyAmounts(players):
    for i in range(1, len(players) - 1):
        if players[i][0] > players[i + 1][0]:
            players[i], players[i + 1] = players[i + 1], players[i]
    for i in range(1, len(players)):
        print(str(players[i][2]) + "'s account: $" + str(players[i][0]))



main()
