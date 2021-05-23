import random

class Region:

    def __init__(
        self, 
        name, 
        max_cards=-1,
        layout='stack'
    ):
        
        self.name = name
        self.cards = []
        self.max_cards = max_cards
        self.layout = layout

    def shuffle(self):
        random.shuffle(self.cards)
        return(self.cards)
        
    def add_deck(self, card_array, shuffle=False):
        for card in card_array:
            self.cards.append(card)
        if shuffle:
            self.shuffle()
        return(self.cards)

    def add_card(self, card):
        self.cards.append(card)
        return(self.cards)
        
    def remove_card(self, card):
        self.cards.remove(card)
        return(self.cards)