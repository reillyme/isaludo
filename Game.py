from region import Region
from setup import generate_deck

class Game:

    def __init__(
        self, 
        name, 
        regions = {},
        complete = False,
        win = None
    ):
        self.name = name
        self.regions = regions
        self.win = win

    def add_region(self, name, max_cards=-1, layout='stack'):
        r = Region(
            name=name,
            max_cards=max_cards,
            layout=layout
        )
        self.regions[name] = r
        return(r)
    
    def check_win_condition(self):
        return(self.win)
    
    def check_lose_condition(self):
        return(self.win)
    
    def deck_depleted(self, deck_region, n_required):
        if len(deck_region.cards) < n_required:
            return(True)
        else:
            return(False)

    def draw(self, region_from, region_to, n_cards, face_up=True):
        if self.deck_depleted(region_from, n_cards):
            return(False)
        for i in range(n_cards):
            card = region_from.cards.pop()
            card.face_up = face_up
            region_to.cards.append(card)
        return(True)

    def yank(self, region_from, region_to, n_cards, face_up=True):
        ''' same as draw, but from the bottom of the pile (beginning of the array)'''
        if self.deck_depleted(region_from, n_cards):
            return(False)
        for i in range(n_cards):
            card = region_from.cards[0]
            card.face_up = face_up
            region_to.cards.append(card)
            region_from.cards.remove(card)
        return(True)

    def print_play_area(self):
        pass






    