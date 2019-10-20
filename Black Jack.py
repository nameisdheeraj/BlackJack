# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:09:52 2019

@author: Dheeraj
"""
import random

dealer_cards = []

player_cards = []

while len(dealer_cards) < 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

while len(player_cards) < 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You have ", player_cards)        

if sum(player_cards) == 21:
    print("You have a BlackJack!")
elif sum(player_cards) > 21:
    print("You are busted") 

while sum(player_cards) < 21:
    print("You have a total of " + str(sum(player_cards)) + " with", player_cards)
    action = str(input("Do you want to stay or hit :"))
    if action == "hit":
        player_cards.append(random.randint(1,11))
        if sum(player_cards) == 21:
            print("You have a BlackJack!", player_cards)
            while sum(dealer_cards) < 17:
                dealer_cards.append(random.randint(1,11))
                if sum(dealer_cards) > 21:
                    print("Dealer has busted " + str(sum(dealer_cards)) + " with",dealer_cards)
                    print("You win!")
                elif sum(dealer_cards) > sum(player_cards):
                    print("Dealer has a total of " + str(sum(dealer_cards)) + " with",dealer_cards)
                    print("You lose!")
                elif sum(dealer_cards) == sum(player_cards):
                    print("Dealer has a total of " + str(sum(dealer_cards)) + " with",dealer_cards)
                    print("Dealer and you have the same total")
                else:
                    print("Dealer has a total of " + str(sum(dealer_cards)) + " with",dealer_cards)
                    print("You Win!")
        elif sum(player_cards) > 21:
            print("You are busted with", player_cards) 
       
        
    elif action == "stay":
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.randint(1,11))
        if sum(dealer_cards) > 21:
            print("Dealer has busted " + str(sum(dealer_cards)) + " with",dealer_cards)
            print("You win!")
        elif sum(dealer_cards) > sum(player_cards):
            print("Dealer has a total of " + str(sum(dealer_cards)) + " with",dealer_cards)
            print("You lose!")
        elif sum(dealer_cards) == sum(player_cards):
            print("Dealer has a total of " + str(sum(dealer_cards)) + " with",dealer_cards)
            print("Dealer and you have the same total")
        else:
            print("Dealer has a total of " + str(sum(dealer_cards)) + " with",dealer_cards)
            print("You Win!")
        break
        
        
        
        
        
