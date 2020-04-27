import random

#Setting up containers
deck = []
dealer = []
player = []
dict ={'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K':10, 'A':11}
soft ={'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K':10, 'A':1}
#Setting up the 52 cards: (4 Face + 9 Numbers) * 4 Siots 
def deckSetup():
    for suits in range(0,4):
        for faceCards in ['J','Q','K','A']:
            deck.append(faceCards)
        for numbers in (range(2,11)):
            n = str(numbers)
            deck.append(n)

#soft and hard statements reveal card count.
#"cards' for loop adds cards to each player.

def dealingCards(x):
    def softStatement():
        print('Dealer\'s hand is ' + str(dealer)+'                 TOTAL:'+ str(dt))
        print('Your hand is     ' + str(player)+ '            TOTAL:' + str(pst) + '/' + str(pt))
        
    def hardStatement():
        print('Dealer\'s hand is ' + str(dealer)+'                 TOTAL:'+ str(dt))
        print('Your hand is     ' + str(player)+ '            TOTAL:' + str(pt))

    for cards in range(0,2):
        player.append(deck[x])
        x += 1
    dealer.append(deck[x])
    x += 1

    #player.append('A')
    #player.append('3')
    #dealer.append('10')

    dt = dict.get(dealer[0]) 
    pt = dict.get(player[0]) + dict.get(player[1])

   
#Test cards to troubleshoot certain card situations. 



#This assigns hard value for cards.
#Trying to get this function to work, but I can't because dt is considered a local variable!
    '''
def playerHas21():
        while dt < 17: 
            x += 1
            dealer.append(deck[x])
            dt = dt + dict.get(deck[x])
            if pt == dt:
                print('PUSH')
            else:
                hardStatement()
                print('YOU WIN!')
    '''

#If player gets Ace(s)in first two cards. 
    if  player.count('A') == 2:
        pst = soft.get(player[0]) + soft.get(player[1])
        pt = 12
        softStatement()
    elif 'A' in player and pt < 21:
        pst = soft.get(player[0]) + soft.get(player[1])
        softStatement()
    else: 
        hardStatement()

    if pt == 21:
        print('*************BLACKJACK!***********')
        while dt < 17: 
            x += 1
            dealer.append(deck[x])
            dt = dt + dict.get(deck[x])
        if pt == dt:
            print('PUSH')
        else:
            hardStatement()
            print('YOU WIN!')
#Player can stay if less than 21.
    while pt < 21:
        z = input('Hit or stand?(h/s)') #PROMPT
        if z == 'q': #QUIT
            print('You quit. Cya next time!')
            break
        elif z == 'h': #HIT 
            x += 1
            player.append(deck[x])
#If someone gets an Ace from a hit.
#Situation where player gets an Ace dealt and another Ace from a hit.
            if deck[x] == 'A':
               pst = soft.get(player[0]) + soft.get(player[1])
               pt = 12 + dict.get(deck[x])
            if 'A' in player and pt < 21:
                pt = pt + dict.get(deck[x])
                pst = pst + soft.get(deck[x])
                if pt > 21:
                    pt = pst 
                    print('You chose to hit. \n Your hand is ' + str(player) + '                TOTAL:' + str(pst))
                else:
                    hardStatement()
         
            else:
                pt = pt + dict.get(deck[x])
                print('You chose to hit. \n Your hand is ' + str(player) + '                TOTAL:' + str(pt))
            if pt > 21:
                print('BUST! Sorry you lose.')# lose
            if pt == 21:
                while dt < 17: 
                    x += 1
                    dealer.append(deck[x])
                    dt = dt + dict.get(deck[x])
                if pt == dt:
                    hardStatement()
                    print('PUSH')
                else:
                    hardStatement()
                    print('YOU WIN!')
        elif z == 's': #STAY
            print('You chose to stay.')
    #dealer hits until 17 or up:
            while dt < 17: 
                x += 1
                dealer.append(deck[x])
                dt = dt + dict.get(deck[x])
            if dt > 21:
                hardStatement()
                print('Dealer BUST. YOU WIN!') # win
              
            elif dt > pt:
                hardStatement()
                print('Sorry, you lose.')#lose
            
            elif dt < pt:
                hardStatement()
                print('YOU WIN!')#win
                
            if dt == pt:
                hardStatement() #tie 
                print('PUSH')
            break
                
        else:
            print('Hmm, you didn\'t press the right option. Try again.')    

            #Retry decision.
            #I want to make this into a function. But if I do,
            #I can't reference dt, since it's not a global variable.

#Game Results
'''
Win conditions:
(PT > DT) AND (PT<21 & DT<21)
DT > 21 = BUST! You Win!!!
(PT > DT) AND PT == 21
Lose conditions: 
PT > 21 = BUST! You Lose...

(pt > dt) AND (pt< 21 and dt<21) = WIN!
(dt > pt) AND (pt< 21 and dt<21) = Lose...
pt == dt = Push
'''

print('Welcome to Blackjack! Win big or go home. \nQuit anytime by pressing q.\n')

deckSetup()
random.shuffle(deck)
dealingCards(0)





