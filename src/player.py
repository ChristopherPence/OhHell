import sys
import unittest
import random
from io import StringIO

# Local imports
from card import Card
from pile import Pile
from error import *

# Globals
MAX_SIZE = sys.maxsize

"""=================================================================================
Player Class
================================================================================="""

""" Player Class
Represents a player. Stores identifying information about the player while also storing
	their hand in the game. This class is also responsible for storing the "knowledge" 
	of the player during the game.

@author Chris P.
@created 2020-12-26 YMD
"""
class Player():
	"""__init__
	Default Constructor - Creates a player with the provided name. Also creates the hand
		and knowledge variables
	@param name : String - the name of the player
	@param id : String - a unique player ID in case of overlapping names. In format 
		"name-UNIXtimestamp"
	"""
	def __init__(self, name, id_, max_size=MAX_SIZE):
		self.name = name
		self.id = id_
		self.hand = Pile()
		self.knowledge = []
		self.points = 0

	# ------------------------------------------------------------------------------
	# Public Methods

	""" push(card)
	Push a new card into the player's hand
	@param card : Card - the card to add to the player's hand
	@return : boolean - true if push successful, false if max_size
	"""
	def push(self, card):
		if self.getHandSize() < self.max_size:
			self.hand.push(card)
			return True
		else:
			ERROR.write("Invalid Push: Inserting into player hand would violate max_size.")
			return False


	""" push_sort(card)
	Push a new card into the player's hand and sort the hand
	Postcondition: The player's hand is in sorted order
	@param card : Card - the card to add to the player's hand
	@return : boolean - true if successful, false if max_size
	"""
	def push_sort(self,card):
		result = self.push(card)
		self.hand.sort()
		return result

	""" remove(card)
	Remove the specified card from the player's hand
	Postcondition: card no longer exists in the player's hand
	@param card : Card - the card to remove
	"""
	def remove(self, card):
		self.hand.remove(card)

	""" sort()
	Sort the player's hand pile
	"""
	def sort(self):
		self.hand.sort()

	def getID(self):
		return self.id

	def getName(self):
		return self.name

	def getPoints(self):
		return self.points

	def getHandSize(self):
		return len(self.hand)

	def getKnowledge(self):
		return self.knowledge

	def hand_tostr(self):
		return str(self.hand)

	# ------------------------------------------------------------------------------
	# Python Methods

	def __len__(self):
		return len(self.hand)

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.id

	""" __contains__(other)
	Checks if other (a card Object...) is contained within the pile
	Precondition: type(other) == Card
	@param other : Card - the card to check the presence of.
	"""
	def __contains__(self, other):
		if type(other) != type(Card(2,0)): # confirm other is a Card
			return False
		elif other in self.hand: #Check if the card is contained
			return True
		else:
			return False

	def __iter__(self):
		return self.hand.__iter__()

	def __next__(self):
		return self.hand.__next__()

	def __eq__(self, other):
		return self.getID() == other.getID()