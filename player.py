import deck

class Player:
	def __init__(self, name):
		self.deck = deck.Deck()
		self.num_win = 0
		self.name = name
	
	def __repr__(self):
		return "{} has {} wins".format(self.name, self.num_win)
