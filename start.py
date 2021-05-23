from game import Game

def main():
	name = 'test'

	testgame = Game(
    	name, 
    	jokers = False
	)

	testgame.add_region(
    	'Hand',
    	face_up = True,
    	all_visible = True
    )

	return(testgame)


if __name__ == '__main__':
	main()