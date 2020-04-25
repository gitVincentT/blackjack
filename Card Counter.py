dealer = []

def dealingCards(x):
        for num in range(0,5):
            option = input('Hit or stay? Y/N')
            if option == 'y':
                x += 1
                print(x)
            else:
                print(x)
        print('Ended turns.')
dealingCards(0)
