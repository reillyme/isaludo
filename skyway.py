from region import Region
from setup import generate_deck
from game import Game
import itertools
import numpy as np

class Skyway(Game):

    def __init__(self):
        super().__init__(
            name='skyway'
        )

        self.add_region('deck')
        self.add_region('market1', layout='fan')
        self.add_region('market2', layout='fan')
        self.add_region('market3', layout='fan')
        self.add_region('play00', layout='fan')
        self.add_region('play01', layout='fan')
        self.add_region('play02', layout='fan')
        self.add_region('play10', layout='fan')
        self.add_region('play11', layout='fan')
        self.add_region('play12', layout='fan')
        self.add_region('play20', layout='fan')
        self.add_region('play21', layout='fan')
        self.add_region('play22', layout='fan')
        self.add_region('discard')

        self.round = 1
        self.regions['deck'].add_deck(
            generate_deck(jokers=False, facecards=False), shuffle=True
            )

        # initial card setup
        self.draw(self.regions['deck'], self.regions['market1'], 2)
        self.draw(self.regions['deck'], self.regions['market2'], 2)
        self.draw(self.regions['deck'], self.regions['market3'], 1)

    def print_play_area(self):
        print('deck: ' + str(len(self.regions['deck'].cards)))
        print('market1: ' + str([x.value + x.suit for x in self.regions['market1'].cards]))
        print('market2: ' + str([x.value + x.suit for x in self.regions['market2'].cards]))
        print('market3: ' + str([x.value + x.suit for x in self.regions['market3'].cards]))
        print('')
        print(str([x.value + x.suit for x in self.regions['play00'].cards]) + '\t\t' +
            str([x.value + x.suit for x in self.regions['play01'].cards]) + '\t\t' +
            str([x.value + x.suit for x in self.regions['play02'].cards]))
        print(str([x.value + x.suit for x in self.regions['play10'].cards]) + '\t\t' +
            str([x.value + x.suit for x in self.regions['play11'].cards]) + '\t\t' +
            str([x.value + x.suit for x in self.regions['play12'].cards]))
        print(str([x.value + x.suit for x in self.regions['play20'].cards]) + '\t\t' +
            str([x.value + x.suit for x in self.regions['play21'].cards]) + '\t\t' +
            str([x.value + x.suit for x in self.regions['play22'].cards]))
        print('discard: ' + str(len(self.regions['discard'].cards)))

    def draft_blueprints(self, market_id, destination):
        '''
        given a selected market and destination location, move the cards
        and remove any overflow cards if any exist there
        market_id should be an int [1,2,3]
        destination should be the name of a region ('play13')
        '''

        self.yank(
            self.regions['market' + str(market_id)], 
            self.regions[destination], 
            len(self.regions['market' + str(market_id)].cards)
        )

        if len(self.regions[destination].cards) > 3:
            n_discard = len(self.regions[destination].cards) - 3
            self.yank(self.regions[destination], self.regions['discard'], n_discard)

        self.reset_market()
        self.print_play_area()

    def trigger_new_round(self):
        self.round += 1
        if self.round >= 4:
            self.check_win_condition()
        else:
            n_discard = len(self.regions['discard'].cards)
            self.draw(self.regions['discard'], self.regions['deck'], n_discard)
            self.regions['deck'].shuffle()


    def check_win_condition(self):
        all_cards = []
        for k in self.regions.keys():
            row = int(k[-2:-1])
            col = int(k[-1])
            if(k.startswith('play')):
                for c in s.regions[k].cards:
                    all_cards[k,i] = 
        if 
        self.win=False

    def reset_market(self):
        #self.check_win_condition()
        for r in self.regions:
            if (r == 'market1') & (len(self.regions[r].cards) == 0):
                if self.deck_depleted(self.regions['deck'], 2):
                    self.trigger_new_round()
                self.draw(self.regions['deck'], self.regions[r], 2)

            if (r == 'market2') & (len(self.regions[r].cards) == 0):
                if self.deck_depleted(self.regions['deck'], 2):
                    self.trigger_new_round()
                self.draw(self.regions['deck'], self.regions[r], 2)

            if (r == 'market3') & (len(self.regions[r].cards) == 0):
                if self.deck_depleted(self.regions['deck'], 1):
                    self.trigger_new_round()
                self.draw(self.regions['deck'], self.regions[r], 1)



    