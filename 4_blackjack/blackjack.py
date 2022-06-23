'''
deal cards
check black jack
player hit or stand, check sum
banker hit or stand
return win or loose
'''

import sys
import random

# deal card
def deal_card():
    return random.choice(cards)

# total points
def points_total(x):
    return sum(x)

# check bust
def bust(x):
    if x > 21:
        return True
    else:
        return False

def points_check(banker,player):
    if banker > player:
        print(f"Player hand: {player_hand}")
        print("Banker Wins!")
        sys.exit()
    if banker < player:
        print(f"Player hand: {player_hand}")
        print("Player Wins!")
        sys.exit()
    if banker == player:
        print(f"Player hand: {player_hand}")
        print("Push")
        sys.exit()

# initialize variable
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_hand=[]
banker_hand =[]

# deal 2 cards
for _ in range(2):
    player_hand.append(deal_card())
    banker_hand.append(deal_card())

# check black jack
if points_total(banker_hand) == 21:
    print(f"Banker hand: {banker_hand}")
    print(f"Player hand: {player_hand}")
    print("Banker Wins!")
    sys.exit()
elif points_total(player_hand) == 21:
    print(f"Banker hand: {banker_hand}")
    print(f"Player hand: {player_hand}")
    print("Player Wins!")
    sys.exit()

# Player play
play = True
while play:
    print(f"Banker hand: {banker_hand[1]}")
    print(f"Player hand: {player_hand}, Total: {points_total(player_hand)}\n")
    if bust(points_total(player_hand)):
        play = False
        print("Player busted.\nBanker Wins!")
        sys.exit()
    hit = input("Would you like to hit? ")
    if (hit == 'yes') | (hit =='y'):
        player_hand.append(deal_card())
    else:
        play = False

# Banker play
banker_play = True
while banker_play:
    print(f"Banker hand: {banker_hand}, Total: {points_total(banker_hand)}")
    if bust(points_total(banker_hand)):
        play = False
        print("Banker busted.\nPlayer Wins!")
        sys.exit()

    if points_total(banker_hand) > points_total(player_hand):
        print(f"Player hand: {player_hand}, Total: {points_total(player_hand)}")
        print("Banker Wins!")
        sys.exit()
    elif points_total(banker_hand) < 17:
        banker_hand.append(deal_card())
    elif points_total(banker_hand) > 16:
        points_check(points_total(banker_hand),points_total(player_hand))
