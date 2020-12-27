import sys
import unittest
from io import StringIO
from abc import ABC, abstractmethod 

# Local imports
from card import Card
from pile import Pile
from deck import Deck
from player import Player
from error import *

# Globals
MAX_SIZE = sys.maxsize

"""=================================================================================
Gamestate Class
================================================================================="""

""" Gamestate Class
The definitive source of truth for a given game. Stores all the information related
	to the game being played like players and what cards are where. It also stores
	the history of actions taken to get to that point in time.

@author Chris P.
@created 2020-12-26 YMD
"""
class Gamestate():

	""" __init__
	Default constructor - creates a gamestate object with given deck and player array. 
		Also create the empty array of piles. 
	@param deck : Deck - the full deck of cards to start the game with.
	@param players[] : Array of Player objects. These are the players in the current game
	"""
	def __init__(self, deck, players):
		self.deck = deck
		self.players = players
		self.piles = []
		self.history = []
		self.turns = 0
		self.rounds = 0
		self.attributes = {} # A dictionary of attributes unique to each game eg. which suit is trump

	# ------------------------------------------------------------------------------
	# Gamestate - ActionFactory interactions

	def revertLastAction(self):
		self.history.pop().revert()

	def storeAction(self, action):
		self.history.append(action)

	# TODO
	def getPlayers(self):
		pass

	# TODO
	def getPileNumbers(self):
		pass

	# ------------------------------------------------------------------------------
	# Gamestate - Action interactions

	""" setGameAttribute(key, value)
	Adds or edits a key/value pair in the self.attributes dictionary. If the key exists
		it updates the pair with the new value.
	Postcondition self.attributes.get(key) == value
	@param key : String - the key to search for in the dictionary
	@param value : Any - the value to associate with key in the dictionary
	@return : Any - returns None if new entry, previous value if key already existed
	"""
	def setGameAttribute(self, key, value):
		# !! Check game validity
		# In this case there is nothing to check

		# !! Make Change
		old = self.attributes.get(key)
		self.attributes.update({key:value})
		return old

	""" removeGameAttribute(key)
	Removes a key value pair from self.attributes. Returns the value of the removed pair.
		Returns nothing if the key didn't exist
	Postcondition self.attributes.get(key) == None
	@param key : String - the key of the pair to remove from the dictionary
	@return : Any - Returns the associated value of the removed key or None if
		key didn't exist
	"""
	def removeGameAttribute(self, key):
		# !! Check game validity
		# In this case there is nothing to check

		# !! Make Change
		if self.attributes.get(key) == None:
			return None
		else:
			return self.attributes.pop(key)

	"""	deckToPlayer(card, player)
	Deal a card from the deck to the player. Will return false if the deck doesn't contain
		the card
	Precondition (card in self.deck) and (player in self.players)
	Postcondition (card not in self.deck) and (card in player)
	@param card : Card - the card to move from the deck to the player hand
	@param player : Player - the player who should recieve the card
	@return : boolean - True is the operation is successful, False is the card isn't in
		the deck or the player doesn't exist
	"""
	def deckToPlayer(self, card, player):
		# !! Check game validity
		if card not in self.deck:
			return False
		if player not in self.players:
			return False

		# !! Make Change
		self.deck.remove(card)
		for p in self.players:
			if p == player:
				p.push(card)
				break
		return True




	

	""" Methods Set

	! add/edit a game attribute
	! Remove a game attribute

	Deck deals to a player
	Player puts card back into deck

	Player plays a card to a pile
	A player picks up a card from a pile

	Deck moves a card into a pile
	Pile moves a card into the deck

	Reset all game attributes
	All cards are reset
	Player earns a point
	A pile is removed 
	A card is removed
	New turn
	New round
	"""


	# ------------------------------------------------------------------------------
	# Python Methods

	def __str__(self):
		output = "Summary: {} actions. {} turns. {} rounds.\n".format(len(self.history), self.turns, self.rounds)
		for key,value in self.attributes.items():
			output += "{}: {}\n".format(key, str(value))
		for i,item in enumerate(self.piles):
			output += "Pile {} has {} cards: {}\n".format(i, len(item), str(item))
		for item in self.players:
			output += "Player {} has {} cards: {}\n".format(item.getName(), item.getHandSize(), item.hand_tostr())
		output += "{} cards in deck: {}\n".format(len(self.deck), str(self.deck))
		return output



"""=================================================================================
Gamestate Class Unit Tests
=================================================================================""" 

class TestGamestateClass(unittest.TestCase):

	def setUp(self):
		# Build the deck
		regular_deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
		deck = Deck(52)
		deck2 = Deck(104)
		for i in regular_deck:
			deck.append(Card.fromID(i))
			deck2.append(Card.fromID(i))
			deck2.append(Card.fromID(i))

		# Build the players
		self.players = [Player("Arron","A-1"), Player("Becky","B-1"), Player("Chris", "C-1"), Player("Danny", "D-1",2)]
		self.single = Gamestate(deck, self.players)
		self.double = Gamestate(deck2, self.players)

	# ------------------------------------------------------------------------------
	# Gamestate - ActionFactory interactions

	def test_revertLastAction(self):
		pass

	def test_storeAction(self):
		pass

	def test_getPlayers(self):
		pass

	# ------------------------------------------------------------------------------
	# Gamestate - Action interactions

	def test_setGameAttribute(self):
		pass

	def test_removeGameAttribute(self):
		pass

	def test_deckToPlayer(self):
		# Test dealing post conditions
		test1 = self.single.deckToPlayer(Card(2,2), self.players[0])
		test2 = self.single.deckToPlayer(Card(2,2), self.players[0])
		test3 = self.single.deckToPlayer(Card(3,3), Player("Zulu", "Z-1"))
		self.assertTrue(test1)
		self.assertFalse(test2)
		self.assertFalse(test3)
		self.assertTrue(Card(2,2) not in self.single.deck)
		self.assertTrue(Card(2,2) in self.players[0])
		self.assertTrue(Card(3,3) in self.single.deck)

		# Test dealing same card with 2 decks
		test4 = self.double.deckToPlayer(Card(2,2), self.players[0])
		test5 = self.double.deckToPlayer(Card(2,2), self.players[0])
		self.assertTrue(test4)
		self.assertTrue(test5)

	def test_playerToDeck(self):
		# Test moving a card from the deck to the player and back with error
		test1 = self.single.deckToPlayer(Card(2,2), self.players[0])
		self.assertTrue(Card(2,2) not in self.single.deck)
		self.assertTrue(Card(2,2) in self.players[0])
		test2 = self.single.playerToDeck(self.players[0], Card(2,2))
		test3 = self.single.playerToDeck(self.players[0], Card(2,2))
		self.assertTrue(test1)
		self.assertTrue(test2)
		self.assertFalse(test3)
		self.assertTrue(Card(2,2) in self.single.deck)
		self.assertTrue(Card(2,2) not in self.players[0])

		# Test dealing same card with 2 decks
		test4 = self.double.deckToPlayer(Card(2,2), self.players[0])
		test5 = self.double.deckToPlayer(Card(2,2), self.players[0])
		self.assertTrue(test4)
		self.assertTrue(test5)
		test6 = self.double.playerToDeck(self.players[0], Card(2,2))
		test7 = self.double.playerToDeck(self.players[0], Card(2,2))
		self.assertTrue(test6)
		self.assertTrue(test7)

	def test_pileToPlayer(self):
		# Setup piles
		self.single.piles[0] = Pile(max_size=2)
		self.single.piles[1] = Pile(enforce_order=True)
		self.single.piles[0].push(Card(2,1))
		self.single.piles[1].push(Card(2,2))
		self.single.piles[1].push(Card(2,3))

		# Pile doesn't exist
		test1 = self.single.pileToPlayer(2, self.players[0], Card(2,1))
		self.assertFalse(test1)
		self.assertTrue(Card(2,1) not in self.players[0])

		# Player doesn't exist
		test2 = self.single.pileToPlayer(0, Player("Zulu", "Z-1"), Card(2,1))
		self.assertFalse(test2)
		self.assertTrue(Card(2,1) in self.single.piles[0])

		# Card doesn't exist
		test3 = self.single.pileToPlayer(0, self.players[0], Card(2,0))
		self.assertFalse(test3)
		self.assertTrue(Card(2,0) not in self.players[0])
		self.assertTrue(Card(2,0) not in self.single.piles[0])

		# Player with max_size
		test3 = self.single.pileToPlayer(0, self.players[4], Card(2,1))
		test4 = self.single.pileToPlayer(1, self.players[4], Card(2,2))
		test5 = self.single.pileToPlayer(1, self.players[4], Card(2,3))
		self.assertTrue(test3)
		self.assertTrue(test4)
		self.assertFalse(test5)
		self.assertTrue(Card(2,1) in self.players[4])
		self.assertTrue(Card(2,2) in self.players[4])
		self.assertTrue(Card(2,3) not in self.players[4])
		self.assertTrue(Card(2,1) not in self.single.piles[0])
		self.assertTrue(Card(2,2) not in self.single.piles[1])
		self.assertTrue(Card(2,3) in self.single.piles[1])

		# Postconditions
		test6 = self.single.pileToPlayer(1, self.players[0], Card(2,3))
		self.assertTrue(test6)
		self.assertTrue(Card(2,3) in self.players[0])
		self.assertTrue(Card(2,3) not in self.single.piles[1])

	def test_playerToPile(self):
		# Setup piles
		self.single.piles[0] = Pile(max_size=2)
		self.single.piles[1] = Pile(enforce_order=True)
		self.single.players[0].push(Card(2,1))
		self.single.players[1].push(Card(2,2))
		self.single.players[1].push(Card(2,3))
		self.single.players[0].push(Card(14,3))

		# Pile doesn't exist, card should move!
		test1 = self.single.playerToPile(self.players[0], 3, Card(14,3))
		self.assertTrue(test1)
		self.assertTrue(Card(14,3) not in self.players[0])
		self.assertTrue(Card(14,1) in self.single.piles[3])
		self.assertTrue(self.single.piles[2] == None)

		# Player doesn't exist
		test2 = self.single.playerToPile(Player("Zulu", "Z-1"), 0, Card(2,1))
		self.assertFalse(test2)
		self.assertTrue(Card(2,1) not in self.single.piles[0])

		# Card doesn't exist
		test3 = self.single.playerToPile(self.players[0], 0, Card(2,0))
		self.assertFalse(test3)
		self.assertTrue(Card(2,0) not in self.players[0])
		self.assertTrue(Card(2,0) not in self.single.piles[0])

		# Pile with max_size
		test3 = self.single.playerToPile(self.players[0], 0, Card(2,1))
		test4 = self.single.playerToPile(self.players[1], 0, Card(2,2))
		test5 = self.single.playerToPile(self.players[1], 0, Card(2,3))
		self.assertTrue(test3)
		self.assertTrue(test4)
		self.assertFalse(test5)
		self.assertTrue(Card(2,1) not in self.players[0])
		self.assertTrue(Card(2,2) not in self.players[1])
		self.assertTrue(Card(2,3) in self.players[1])
		self.assertTrue(Card(2,1) in self.single.piles[0])
		self.assertTrue(Card(2,2) in self.single.piles[0])
		self.assertTrue(Card(2,3) not in self.single.piles[0])

		# Postconditions
		test6 = self.single.playerToPile(self.players[1], 1, Card(2,3))
		self.assertTrue(test6)
		self.assertTrue(Card(2,3) in self.players[1])
		self.assertTrue(Card(2,3) not in self.single.piles[1])

	def tearDown(self):
		self.single = None
		self.double = None
		self.players = None



if __name__ == '__main__':
	# Divert stderr so unittest output isn't cluttered
	ERROR = StringIO() 
	unittest.main()