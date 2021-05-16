class Game:

    def __init__(
        self, 
        name, 
        jokers,
        components = [],
        complete = False,
        won = null
    ):
    self.name = name
    self.jokers = jokers
    self.components = components
    self.complete = complete
    self.won = won

    def add_component(self, name, face_up, all_visible, cards, max_cards):
        self.components.append(Component())
        return(self.components)
        
    def remove_component(self, component):
        self.components.remove(component)
        return(self.components)
    
    def check_win_condition(self):
        if False:
            self.complete = True
            self.win = True
        else:
            self.complete = False
            self.win = False
        return(self.complete)
    
    def check_lose_condition(self):
        if False:
            self.complete = True
            self.win = False
        else:
            self.complete = False
            self.win = False
        return(self.complete)
    
    def deal(self):
        pass
    
    def generate_deck(jokers = self.jokers):
        suits = ['H','S','C','D']
        values = range(13)
        labels = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        deck = {}
        
        for i,suit in enumerate(suits):
            for value in values:
                card = (j,suit + labels[j])
                deck{i} = card
        return(deck)