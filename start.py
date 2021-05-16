name = 'test'

testgame = Game(
    name, 
    jokers = False
)

testgame.add_component(
    'Hand',
    face_up = True,
    all_visible = True,
    cards = []
)