import sys
import unittest
from io import StringIO
from abc import ABC, abstractmethod 

# Local imports
from card import Card
from pile import Pile
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

	def function():
		pass

	# ------------------------------------------------------------------------------
	# Gamestate - ActionFactory interactions

	def revertLastAction(self):
		self.history.pop().revert()

	def storeAction(self, action):
		self.history.append(action)


	# ------------------------------------------------------------------------------
	# Gamestate - Action interactions

	""" setGameAttribute(key, value)
	Adds or edits a key/value pair in the self.attributes dictionary. If the key exists
		it updates to the new value
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

	""" removeGameAttribute(key, value)
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