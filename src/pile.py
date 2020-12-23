from abc import ABC, abstractmethod
import sys
import random

# Local imports
from card import *

# Globals
MAX_SIZE = sys.maxsize
ERROR = sys.stderr

"""=================================================================================
Pile Class
================================================================================="""

""" Pile Class
Abstract class representing a real life "pile" of cards. Has the Deck and Hand classes
	as children. A deck is the main pile of cards while a hand belongs to a player.

@author Chris P.
@created 2020-12-21 YMD
"""
class Pile(ABC):
	# Constructor
	def __init__(self, max_size=MAX_SIZE):
		self.max_size = max_size
		self.hand = []

	# ------------------------------------------------------------------------------
	# Abstract Methods

	# Insert a card into the pile at a specified location, default 0
	@abstractmethod
	def insert(self, card, location=0):
		pass

	# Remove a specified card from the pile
	@abstractmethod
	def remove(self, card):
		pass

	# Push a card to the front of the pile (start of the list)
	@abstractmethod
	def push(self, card):
		pass

	# Pop a card from the front of the pile (start of the list)
	@abstractmethod
	def pop(self):
		pass

	# ------------------------------------------------------------------------------
	# Static Methods

	""" fromList(lis)
	Creates a pile object containing cards with IDs corresponding to the ints in lis
	@param lis : [int] - list of card IDs
	@return a corresponding Pile object
	"""
	@classmethod
	def fromList(cls, lis, max_size=MAX_SIZE):
		output = cls(max_size)
		for i in lis:
			output.push(Card.fromID(i))
		return output

	# ------------------------------------------------------------------------------
	# Public Methods

	""" getSize()
	Returns the size of hand list in a Pile object
	@return length of self.hand
	"""
	def getSize(self):
		return len(self.hand)

	""" shuffle()
	Randomly orders the contents of self.hand 
	"""
	def shuffle(self):
		random.shuffle(self.hand)

	""" sort()
	Numerically sorts the contents of self.hand
	"""
	def sort(self):
		self.hand.sort()

	""" clear()
	Removes all of contents from self.hand
	"""
	def clear(self):
		self.hand.clear()

	# ------------------------------------------------------------------------------
	# Python Methods

	""" __len__()
	Overrides the __len__ method and returns the size of hand list in a Pile object
	@return length of self.hand
	"""
	def __len__(self):
		return self.getSize()

	""" __str__()
	Overrides the __str__ method and returns a string 
	@return string representation of self.hand
	"""
	def __str__(self):
		return self.hand.__str__()

	""" __repr__()
	Overrides the __repr__ method and returns a string 
	@return string representation of self.hand
	"""
	def __repr__(self):
		return self.__str__()



"""=================================================================================
Hand Class
=================================================================================""" 


"""
hand field is a list. The order is representative of a left to right hand. Therefore
0 is the leftmost card and n is the rightmost card. In this case we consider 0 tp be
the start of the list and n to be the end.
"""

class Hand(Pile):

	# Default Constructor - set the value of the card given value and suit
	# @param 	max_size	: int of the maximum number of cards allowed in the hand
	def __init__(self, max_size=sys.maxsize):
		self.max_size = max_size
		self.hand = []






	# Insert before the specified element
	def insert(self, card, location = 0):
		return self.hand.insert(location, card)

	def remove(self, card):
		return


	def push(self, card):
		return self.insert(card,0)

	def pop(self):
		return 




chris = Hand()

chris.push(Card.fromID(47))
chris.push(Card.fromID(24))
chris.push(Card.fromID(36))
chris.push(Card(47,2))

print(chris)