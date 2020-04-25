import random

# Need to translate strings to number value and then add. CREATE DICTIONARY
dict ={'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K':10, 'A':11}

#I used this function to generate a dictionary for me. So I wouldn't have to type one out :P 
'''
for num in range (2,11):
    dict.update({str(num):num})
print(dict)
'''
# And then added J thru K manually... gotta do something about Ace tho


# Afterwards add values to produce total
player = []
dealer =[]
deck =[]

def deckSetup():
    for suits in range(0,4):
        for faceCards in ['J','Q','K','A']:
            deck.append(faceCards)
        for numbers in (range(2,11)):
            n = str(numbers)
            deck.append(n)


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


deckSetup()
random.shuffle(deck)
dealingCards(0)
'''


    
           
def cardsToValues():

deckSetup()
'''
