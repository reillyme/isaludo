from region import Region
from setup import generate_deck
from game import Game
from card import Card
import itertools
import numpy as np
from pandas import value_counts


def check_wrap_subtraction(card1, card2, card3):
    value_ids = [card1.val_int, card2.val_int, card3.val_int]
    value_ids.sort()
    value_ids.append(value_ids[0] + 13)
    value_ids.sort()
    diffs = [value_ids[x] - value_ids[x-1] for x in [1,2,3]]
    
    if any(value_counts(diffs) > 1):
        return(True)
    else:
        return(False)
        
def check_sandwich(card1, card2, card3):
    '''
    test whether the 3-card sandwich is valid
    and return the number of new cards to be dealt
    '''
    suits = [card1.suit, card2.suit, card3.suit]
    print(suits)
    values = [card1.value, card2.value, card3.value]
    print(values)

    num_deal = 2
    if len(set(suits)) == 1:
        num_deal = 4
    elif (set(suits) == {'D', 'H'}) | (set(suits) == {'C', 'S'}):
        num_deal = 3
    print(num_deal)

    if check_wrap_subtraction(card1, card2, card3):
        return(num_deal)
    else:
        return(0)

class Sandwich(Game):

    def __init__(self):
        super().__init__(
            name='sandwich'
        )

        self.add_region('deck')
        self.add_region('hand', layout='complete')
        self.add_region('discard')

        self.round = 1
        self.regions['deck'].add_deck(
            generate_deck(jokers=False, facecards=True), shuffle=True
            )

        # initial card setup
        self.draw(self.regions['deck'], self.regions['hand'], 8)

    def print_play_area(self):
        print('deck: ' + str(len(self.regions['deck'].cards)))
        print('hand: ' + str([x.value + x.suit for x in self.regions['hand'].cards]))
        print('discard: ' + str(len(self.regions['discard'].cards)))


    def discard_sandwich(self, i1, i2, i3):
        '''
        check and discard the selected sandwich
        '''
        card1 = self.regions['hand'].cards[i1]
        card2 = self.regions['hand'].cards[i2]
        card3 = self.regions['hand'].cards[i3]
        count_new = check_sandwich(card1, card2, card3)

        if count_new == 0:
            self.print_play_area()
            return(False)

        self.regions['hand'].cards.remove(card1)
        self.regions['hand'].cards.remove(card2)
        self.regions['hand'].cards.remove(card3)

        self.regions['discard'].cards.append(card1)
        self.regions['discard'].cards.append(card2)
        self.regions['discard'].cards.append(card3)

        self.reset_hand(count_new)
        self.print_play_area()
        return(True)
    
    def out_of_options(self):
        hand = self.regions['hand'].cards
        all_selections = itertools.combinations(enumerate(hand), 3)
        all_results = []
        for x in all_selections:
            if check_sandwich(x[0][1], x[1][1], x[2][1]) > 0:
                return(False)
        return(True)

    def reset_hand(self, count_new):
        self.draw(
            self.regions['deck'], 
            self.regions['hand'], 
            np.min([count_new, 8 - len(self.regions['hand'].cards)])
        )
        
        if self.deck_depleted(self.regions['deck'], 1):
            self.win = True
            if self.out_of_options():
                self.trigger_endgame()
        elif self.out_of_options():
            self.win = False
            self.trigger_endgame()

    