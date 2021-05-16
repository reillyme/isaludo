import pandas as pd
import numpy as np

def generate_deck(jokers=False):

	suits = ['H', 'D', 'C', 'S']
	values = ['A', '2', '3', '4', '5', '6', '7',
		'8', '9', '10', 'J', 'Q', 'K']

	deck = []

	counter = 0
	for i in range(len(suits)):
		suit = suits[i]
		for j in range(len(values)):
			value = values[j]
			card = Card(counter, suit, value)
			counter += 1
			deck.append(card)

	if jokers:
		deck.append(Card(counter + 1, suit=null, value='jo1'))
		deck.append(Card(counter + 2, suit=null, value='jo2'))

	return(deck)