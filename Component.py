class compontent:

    def __init__(
        self, 
        name, 
        face_up,
        all_visible,
        cards = [],
        max_cards = null,
        layout = 0,
        cards = []
    ):
        
        if(len(cards) > max_cards):
            return('too many init cards!')
        
        self.name = name
        self.face_up = face_up
        self.all_visible = all_visible
        self.cards = cards
        self.count = len(self.cards)
        self.max_cards = max_cards
        self.layout = layout
        

    def add_card(self, card):
        self.cards.append(card)
        return(self.cards)
        
    def remove_card(self, card);
        self.cards.remove(card)
        return(self.cards)