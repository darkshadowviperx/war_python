import deck
import player

class War:
	#initialize war object
	def __init__(self):
		self.player1 = None 
		self.player2 = None		
		self.stake_stack = deck.Deck()		
		
	#distribute cards to player1 and player2 from stack			
	def distribute_cards(self):
		stack = deck.Deck()
		stack.init_standard_deck()
		
		for i in range(len(stack.cards)):
			if( i%2 == 0):
				self.player1.deck.add_card(stack.remove_top_card())
			else:
				self.player2.deck.add_card(stack.remove_top_card())
	
	#empty the stake_stack deck to a players deck
	def add_stake_stack(self,player):		
		for i in range(len(self.stake_stack.cards)):						
			player.deck.add_card(self.stake_stack.remove_top_card())
				
	# compare card from player1 and player2 stack
	# see if tie breaker is necessary
	def war(self, tie_breaker):		
		
		# in case of tie breaker
		if(tie_breaker):
			print("Tie Breaker Time!\nCards at Stake:")
			print(self.stake_stack)
			if(self.check_win()):
				print("Uh Oh! Someone has no cards left!\n")
				return
		
		player1_card = self.player1.deck.remove_top_card()
		player2_card = self.player2.deck.remove_top_card()
	
		self.stake_stack.add_card(player1_card)
		self.stake_stack.add_card(player2_card)
			
		self.print_name_card_msg(self.player1.name, player1_card)
		print("VS.")
		self.print_name_card_msg(self.player2.name, player2_card)
		input("")
				
		if(player1_card < player2_card):
			self.print_win_msg(self.player2.name)
			self.add_stake_stack(self.player2)								
		elif(player1_card > player2_card):
			self.print_win_msg(self.player1.name)
			self.add_stake_stack(self.player1)			
		else:					
			self.war(True)	
			
	#print player name with card
	def print_name_card_msg(self, name, card):
		print("{} card: {}".format(name, card))
	
	#print battle win msg 
	def print_win_msg(self, name):
		print("{} Win!\n______________________________\n".format(name))
	
	#check if winner
	def check_win(self):
		if(len(self.player1.deck.cards) > 0 and len(self.player2.deck.cards) > 0):
			return False
		else:
			return True
	
	#play the game!	
	def play(self):
		print("Welcome to War")
		num_players = 0
		while(num_players != "1" and num_players != "2"):
			num_players = input("1 or 2 players? Type 1 or 2 and press enter:")
			if(num_players == "1"):
				self.player1 = player.Player(input("Type name for player1 and then press enter:"))
				self.player2 = player.Player("Computer")
			elif(num_players == "2"):
				self.player1 = player.Player(input("Type name for player1 and then press enter:"))
				self.player2 = player.Player(input("Type name for player2 and then press enter:"))
			else:
				print("Error: Must use 1 or 2 players")	
		
		while True:
			input("\nLet's go to War!\n")
			
			#initialize decks
			self.player1.deck.reset_deck()
			self.player2.deck.reset_deck()
			self.stake_stack.reset_deck()
			self.distribute_cards()
				
			while(not self.check_win()):
				self.war(False)
			
			if(len(self.player1.deck.cards) > 0):
				print("{} won the war!!!".format(self.player1.name))
			else:
				print("{} won the war!!!".format(self.player2.name))
				
			if( input("Would you like to play again? Type Y").lower() != "y" ):
				break

