class Card:
	suits = ("hearts", "clubs", "diamonds", "spades")
	values = (None, None, 2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace")
	
	#value is int type 2-14
	#suite is int type 0-4
	def __init__ (self, value, suit):
		self.value = value
		self.suit = suit
	
	#prints out card type
	def __repr__(self):
		return "{} of {}".format(self.values[self.value], self.suits[self.suit])
		
	def __lt__(self, card):		
		if(self.value < card.value):			
			return True
		else:
			return False
			
	def __gt__(self, card):
		if(self.value > card.value):
			return True
		else:
			return False
