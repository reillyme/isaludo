from card import Card

def generate_deck(
    jokers=False, 
    facecards=True, 
    color='both'
):

    if color == 'red':
        suits = ['H', 'D']
    elif color == 'black':
        suits = ['C', 'S']
    else:
        suits = ['H', 'D', 'C', 'S']
    if facecards:
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    else:
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        

    deck = []

    counter = 0
    for i in range(len(suits)):
        suit = suits[i]
        for j in range(len(values)):
            value = values[j]
            tmp = Card(counter, suit, value)
            deck.append(tmp)
            counter += 1

    if jokers:
        joker1 = Card(counter + 1, suit=null, value='jo1')
        joker2 = Card(counter + 2, suit=null, value='jo2')
        deck.append(joker1)
        deck.append(joker2)

    return(deck)