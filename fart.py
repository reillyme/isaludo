from game import Game
from region import Region
from setup import generate_deck

class Fart(Game):

    def __init__(self):
        super().__init__(
            name='fart'
        )
        
        self.round=0
        
        self.add_region('deck_aliens', layout='stack')
        self.add_region('deck_defenders', layout='stack')
        self.add_region('defenders', layout='complete')
        self.add_region('discard', layout='stack')
        self.add_region('attackers', layout='complete')
        
        self.regions['deck_aliens'].add_deck(
            generate_deck(jokers=False, facecards=True, color='red'), shuffle=True
            )        
        self.regions['deck_defenders'].add_deck(
            generate_deck(jokers=False, facecards=True, color='black'), shuffle=True
            )
        
        self.draw(self.regions['deck_defenders'], self.regions['defenders'], 6)
        self.draw(self.regions['deck_aliens'], self.regions['attackers'], 3)
    
    def check_win_condition(self):
        return(self.win)
    
    def check_lose_condition(self):
        return(self.win)

    def print_play_area(self):
        print('Alien deck: ' + str(len(self.regions['deck_aliens'].cards)))
        print('Defender deck: ' + str(len(self.regions['deck_defenders'].cards)))
        print('Defenders: ' + str([x.value + x.suit for x in self.regions['defenders'].cards]))
        print('Attackers: ' + str([x.value + x.suit for x in self.regions['attackers'].cards]))
        print('Discard: ' + str(len(self.regions['discard'].cards)))
        
    def reset_defenders(self):
        if deck_depleted(self.regions['defenders'], 6):
            draw_need = 6 - len(self.regions['defenders'].cards)
            self.draw(self.regions['deck_defenders'], self.regions['defenders'], draw_need)
        if deck_depleted(self.regions['attackers'], 1):
            self.round += 1
            discard = self.regions['discard'].cards
            self.regions['deck_defenders'].add_deck(discard, shuffle=True)
            self.regions['discard'].cards = []
        self.win = check_win_condition()
    
    def check_win_condition(self):
        if deck_depleted(self.regions['attackers'], 1) & self.round > 1:
            return(True)
        elif deck_depleted(self.regions['defenders'], 1):
            return(False)
        else:
            return(None)
        
    def dual_attack(self, card1, card2):
        if card1.val_int + card2.val_int + 1 == \
            self.regions['attackers'].cards[0].val_int:
            self.yank(self.regions['attackers'], self.regions['discard'], 1)
            if round > 0:
                # discard any defender whose color matches attacker
            self.print_play_area()
            return(True)
        else:
            self.print_play_area()
            return(False)
        
    def single_attack(self, card):
        current_attacker = self.regions['attackers'].cards[0]
        if card.color == current_attacker.color:
            self.print_play_area()
            return(False)
        elif card.val_int <= current_attacker.val_int:
            self.print_play_area()
            return(False)
        else:
            replace_index = self.regions['defenders'].cards.index(card)
            self.regions['defenders'].remove_card(card)
            self.regions['discard'].add_card(card)
            self.regions['attackers'].remove_card(current_attacker)
            self.regions['defenders'].cards.insert(replace_index, current_attacker)
            return(True)
            self.print_play_area()
            
    def sacrifice(self, card):
        current_attcker = self.regions['attackers'].cards[0]
        self.regions['defenders'].remove_card(card)
        self.regions['attackers'].cards.insert(0, current_attacker)
        self.regions['discard'].add_card(card)
        return(True)
    
    def trigger_endgame(self):
        print('GAME OVER')
        if self.win:
            print('YOU WIN :)')
        else:
            print('Better luck next time.')






    