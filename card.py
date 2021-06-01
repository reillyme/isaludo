class Card:
    '''
    this is a card class
    '''

    def __init__(self, id, suit, value, face_up=False):

        self.id = id
        self.suit = suit
        self.value = value
        self.face_up = face_up
        
        value_map = dict(zip(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],range(13)))
        self.val_int = value_map[self.value]
        
        self.color = None
        if self.suit in ['H','D']:
            self.color = 'red'
        if self.suit in ['S','C']:
            self.color = 'black'

    def flip(self):
        self.face_up = ~self.face_up