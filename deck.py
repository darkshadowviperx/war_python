import card
from random import shuffle

class Deck:
	
	#deck holds array of empty cards
	def __init__(self):
		self.cards = []
	
	def init_standard_deck(self):
		for i in range(4):
			for j in range(2,15):
				self.cards.append( card.Card(j, i))
		shuffle(self.cards)
	
	def add_card(self, card):
		self.cards.append(card)

	def remove_top_card(self):
		return self.cards.pop(0)
	
	def __repr__(self):
		for card in self.cards:
			print(card)
		return ''
	
	def reset_deck(self):
		self.cards = []