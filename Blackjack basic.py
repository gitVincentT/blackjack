import random

#deck starts off with nothing
deck = []
dealer = []
player = []
dict ={'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K':10, 'A':11}

#4 Suits, 4 Face Cards, and 9 Numbers = 52 possibilties.
def deckSetup():
    for suits in range(0,4):
        for faceCards in ['J','Q','K','A']:
            deck.append(faceCards)
        for numbers in (range(2,11)):
            n = str(numbers)
            deck.append(n)

#Every time a card is dealt, it should increase the card count. 
def dealingCards(x):
    for cards in range(0,2):
        player.append(deck[x])
        x += 1
    dealer.append(deck[x])
    x += 1
    dt = dict.get(dealer[0]) 
    pt = dict.get(player[0]) + dict.get(player[1])
    
    print('Dealer\'s hand is ' + str(dealer)+'                 TOTAL:'+ str(dt))
    print('Your hand is     ' + str(player)+ '            TOTAL:' + str(pt))


    q = input('Hit or stand?(h/s)')
    if q  == 'h':
        x += 1
        player.append(deck[x])
        print('You chose to hit. \n Your hand is ' + str(player) + '                TOTAL: ')
    elif q == 's':
        print('You chose to stay.')
    else:
        print('Hmm, you didn\'t press the right option.')


#Game Results
'''
PT > 21 = BUST! You Lose...
DT > 21 = BUST! You Win!!!
(pt > dt) AND (pt< 21 and dt<21) = WIN!
(dt > pt) AND (pt< 21 and dt<21) = Lose...
pt == dt = Push
'''
deckSetup()
random.shuffle(deck)
dealingCards(0)



