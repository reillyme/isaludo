class Card:
	# id: integer between 0 and 53
	# face_up: boolean
	# layout: ['stack', 'fan', 'full']
	# suit: ['H', 'D', 'C', 'S'] null for joker
	# value: ['A', '2', '3', '4', '5', '6', '7', '8',
		# '9', '10', 'J', 'Q', 'K', 'jo']

    def __init__(
        self, 
        id,
        suit,
        value,
        face_up = False,
        layout = 'stack'
    ):

    	self.id = id
    	self.suit = suit
    	self.value = value
    	self.face_up = face_up
    	self.layout = layout

    def flip(self):
    	self.face_up = ~self.face_up

