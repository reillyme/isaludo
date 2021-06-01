class Card:
    '''
    this is a card class
    '''

    def __init__(self, id, suit, value, face_up=False):

        self.id = id
        self.suit = suit
        self.value = value
        self.face_up = face_up

    def flip(self):
        self.face_up = ~self.face_up
